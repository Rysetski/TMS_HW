import json
import csv

json_file_path = "employees.json"
csv_file_path = "employees.csv"


def read_json(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)
    return data


def json_to_csv(json_data, csv_file_path):
    if json_data:
        headers = json_data[0].keys()
    else:
        headers = []

    with open(csv_file_path, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()
        writer.writerows(json_data)


def add_employee_to_json(file_path, new_employee):
    employees = read_json(file_path)
    employees.append(new_employee)
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(employees, file, ensure_ascii=False, indent=4)


def main():
    json_data = read_json(json_file_path)
    json_to_csv(json_data, csv_file_path)
    print(f"Данные успешно преобразованы и сохранены в {csv_file_path}")

    new_employee = {}
    new_employee["name"] = input("Введите имя сотрудника: ")
    new_employee["birthday"] = input("Введите дату рождения (дд.мм.гггг): ")

    while True:
        try:
            new_employee["height"] = float(input("Введите рост (в см): "))
            break
        except ValueError:
            print("Пожалуйста, введите корректное число для роста.")

    while True:
        try:
            new_employee["weight"] = float(input("Введите вес (в кг): "))
            break
        except ValueError:
            print("Пожалуйста, введите корректное число для веса.")

    new_employee["car"] = (
        input("Есть ли у сотрудника автомобиль? (да/нет): ").strip().lower() == "да"
    )

    languages = input("Введите языки программирования через запятую: ")
    new_employee["languages"] = [lang.strip()
                                 for lang in languages.split(",") if lang.strip()]

    add_employee_to_json(json_file_path, new_employee)
    print("Новый сотрудник успешно добавлен в JSON файл.")


if __name__ == "__main__":
    main()
