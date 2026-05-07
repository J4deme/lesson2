from registry import add_student, add_grade, get_average, get_all_students

MENU = """
╔══════════════════════════════╗
║      Student Registry        ║
╠══════════════════════════════╣
║  1. Додати студента          ║
║  2. Додати оцінку            ║
║  3. Середня оцінка           ║            ║
║  4. Всі студенти             ║
║  0. Вийти                    ║
╚══════════════════════════════╝
"""


def handle_add_student() -> None:
    name = input("  Ім'я: ").strip()
    print(add_student(name))


def handle_add_grade() -> None:
    name = input("  Ім'я: ").strip()
    raw = input("  Оцінка: ").strip()

    print(add_grade(name, int(raw)))


def handle_average() -> None:
    name = input("  Ім'я: ").strip()
    avg = get_average(name)
    print(f"  Середнє {name}: {avg:.1f}")


def handle_all() -> None:
    students = get_all_students()

    if not students:
        print("  Реєстр порожній.")
        return

    print(f"\n  {'Студент':<15} {'Оцінки'}")
    print(f"  {'-'*15} {'-'*25}")
    for name, grades in students.items():
        grades_str = ", ".join(map(str, grades)) if grades else "—"
        print(f"  {name:<15} {grades_str}")


ACTIONS: dict[str, callable] = {
    "1": handle_add_student,
    "2": handle_add_grade,
    "3": handle_average,
    "4": handle_all,
}


def main() -> None:
    print("Вітаємо в Student Registry!")

    while True:
        print(MENU)
        choice = input("Ваш вибір: ").strip()

        if choice == "0":
            print("До побачення!")
            break

        action = ACTIONS.get(choice)

        if action is None:
            print("  Невідома команда. Спробуйте ще раз.")
            continue

        try:
            action()
        except (Exception) as e:
            print(f"  Помилка: {e}")
        except ValueError:
            print("  Помилка: невірний формат даних.")

if __name__ == "__main__":
    main()
