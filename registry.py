registry: dict[str, list[int]] = {}

def add_student(name: str) -> str:
    if name in registry:
        raise Exception
    registry[name] = []
    return f"Student {name} is added"


def add_grade(name: str, grade: int) -> str:
    if name not in registry:
        raise Exception
    registry[name].append(grade)
    return f"Grade{grade} was added to {name}"

def get_average(name: str ) -> float:
    if name not in registry:
        raise Exception
    grades = registry[name]
    return sum(grades)/len(grades)

def get_all_students():
    return dict(registry)