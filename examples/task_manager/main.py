from contextlib import asynccontextmanager
from pathlib import Path

from fastapi import FastAPI, HTTPException, Response
from fastapi.exceptions import RequestValidationError
from fastapi.responses import FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, ConfigDict, field_validator

from . import db


@asynccontextmanager
async def lifespan(app):
    db.init_db()
    yield


app = FastAPI(title="Gerenciador de tarefas Herdr", lifespan=lifespan)
STATIC = Path(__file__).parent / "static"
app.mount("/static", StaticFiles(directory=STATIC), name="static")

VALIDATION_MESSAGES = {
    "missing": "Este campo é obrigatório",
    "string_type": "O valor deve ser texto",
    "bool_type": "O valor deve ser booleano",
    "extra_forbidden": "Campos adicionais não são permitidos",
    "int_parsing": "O valor deve ser um número inteiro",
}


@app.exception_handler(RequestValidationError)
async def validation_error(request, exc):
    details = []
    for error in exc.errors():
        context = error.get("ctx") or {}
        if error["type"] == "value_error" and "error" in context:
            message = str(context["error"])
        else:
            message = VALIDATION_MESSAGES.get(error["type"], "Valor inválido")
        details.append({"loc": error.get("loc", []), "msg": message, "type": error.get("type", "validation_error")})
    return JSONResponse(status_code=422, content={"detail": details})



class CreateTask(BaseModel):
    model_config = ConfigDict(extra="forbid", strict=True)
    title: str
    description: str = ""

    @field_validator("title")
    @classmethod
    def title_valid(cls, value):
        if not value.strip():
            raise ValueError("O título da tarefa não pode ficar em branco")
        return value.strip()


class PatchTask(BaseModel):
    model_config = ConfigDict(extra="forbid", strict=True)
    title: str | None = None
    description: str | None = None
    completed: bool | None = None

    @field_validator("title", "description", "completed")
    @classmethod
    def explicit_null_invalid(cls, value):
        if value is None:
            raise ValueError("Valores null explícitos não são aceitos")
        return value

    @field_validator("title")
    @classmethod
    def title_valid(cls, value):
        return CreateTask.title_valid(value)


@app.get("/")
def index():
    return FileResponse(STATIC / "index.html")


@app.get("/api/tasks")
def list_tasks():
    return db.get_tasks()


@app.get("/api/tasks/{task_id}")
def get_task(task_id: int):
    task = db.get_task(task_id)
    if task is None:
        raise HTTPException(404, "Tarefa não encontrada")
    return task


@app.post("/api/tasks", status_code=201)
def create_task(body: CreateTask):
    return db.create_task(**body.model_dump())


@app.patch("/api/tasks/{task_id}")
def update_task(task_id: int, body: PatchTask):
    task = db.update_task(task_id, **body.model_dump(exclude_unset=True))
    if task is None:
        raise HTTPException(404, "Tarefa não encontrada")
    return task


@app.delete("/api/tasks/{task_id}", status_code=204)
def delete_task(task_id: int):
    if not db.delete_task(task_id):
        raise HTTPException(404, "Tarefa não encontrada")
    return Response(status_code=204)
