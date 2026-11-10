"""Contrato compartilhado dos capítulos 2/4/5/6; a classificação por competição usa totais não arredondados."""

from collections.abc import Mapping
from math import isfinite

SUBJECTS = frozenset({"English", "History", "Mathematics"})


def validate_scores(scores):
    if not isinstance(scores, Mapping) or set(scores) != SUBJECTS:
        raise ValueError("scores deve conter exatamente English, History e Mathematics")
    for value in scores.values():
        if isinstance(value, bool) or not isinstance(value, (int, float)):
            raise ValueError("As notas devem ser numéricas, não bool")
        if not isfinite(value) or not 0 <= value <= 100:
            raise ValueError("As notas devem ser finitas e estar entre 0 e 100")
    return scores


def calculate_total(scores):
    return sum(validate_scores(scores).values())


def calculate_average(scores):
    return calculate_total(scores) / 3


def get_grade(average):
    if isinstance(average, bool) or not isinstance(average, (int, float)):
        raise ValueError("A média deve ser numérica")
    if not isfinite(average) or not 0 <= average <= 100:
        raise ValueError("A média deve estar entre 0 e 100")
    return "Aprovado" if average >= 60 else "Reprovado"


def rank_students(students):
    if not isinstance(students, list):
        raise ValueError("students deve ser uma lista")
    rows = []
    for student in students:
        if not isinstance(student, Mapping):
            raise ValueError("Cada estudante deve ser um objeto")
        name = student.get("name")
        if not isinstance(name, str) or not name.strip():
            raise ValueError("O nome do estudante é obrigatório")
        total = calculate_total(student.get("scores"))
        average = total / 3
        rows.append({"name": name.strip(), "scores": dict(student["scores"]),
                     "total": total, "average": average, "grade": get_grade(average)})
    rows.sort(key=lambda row: row["total"], reverse=True)
    previous = None
    rank = 0
    for index, row in enumerate(rows, 1):
        if previous is None or row["total"] != previous:
            rank = index
        previous = row["total"]
        row["rank"] = rank
    return rows
