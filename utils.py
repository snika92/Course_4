import json
from api import HeadHunterAPI
from api import SuperJobAPI
from vacancy import Vacancy
from vacancy_file_manager import JSONSaver


def get_vacancy_from_hh_data(vacancies):
    for vacancy in vacancies['items']:
        id = vacancy['id']
        name = vacancy['name']
        if vacancy['salary']:
            if vacancy['salary']['from']:
                salary = vacancy['salary']['from']
            else:
                salary = 0
        else:
            salary = 0
        url = vacancy['alternate_url']
        city = vacancy['area']['name']
        try:
            employer = vacancy['employer']['name']
        except KeyError:
            employer = None
        vacancy_instance = Vacancy(id, name, salary, url, city, employer)
        JSONSaver.add_vacancy(vacancy_instance)


def get_vacancy_from_sj_data(vacancies):
    for vacancy in vacancies['objects']:
        id = vacancy['id']
        name = vacancy['profession']
        salary = vacancy['payment_from']
        url = vacancy['link']
        city = vacancy['town']['title']
        try:
            employer = vacancy['client']['title']
        except KeyError:
            employer = None
        vacancy_instance = Vacancy(id, name, salary, url, city, employer)
        JSONSaver.add_vacancy(vacancy_instance)


def user_interaction():
    # Функцию для взаимодействия с пользователем
    # Открывает файл или создает при его отсутствии и записывает в него пустой список
    with open("vacancies.json", "w", encoding="utf-8") as json_file:
        content = []
        json.dump(content, json_file)

    print("Добрый день!")
    result = input("Введите ключевое слово:\n")
    # Создаем объект класса и получаем вакансии с сайта HeadHunter
    hh = HeadHunterAPI()
    hh_result = hh.get_vacancies(result)
    get_vacancy_from_hh_data(hh_result)
    # Создаем объект класса и получаем вакансии с сайта SuperJob
    sj = SuperJobAPI()
    sj_result = sj.get_vacancies(result)
    get_vacancy_from_sj_data(sj_result)

    # Запускаем цикл с выбором аргумента для поиска по вакансиям
    while True:
        user_choice = input(f"""Выберите действие:
1) Выборка по городу
2) Выборка по зарплате
3) Все найденные
4) Вывести топ N вакансий по зарплате
5) Завершить работу программы\n""")
        print()
        if user_choice == "1":
            city = input("Введите город:\n")
            print()
            # Вызываем функцию поиска по городам
            vacancies_by_city = JSONSaver()
            list_of_vacancies = vacancies_by_city.get_vacancies_by_city(city)
            for vacancy in list_of_vacancies:
                print(vacancy)
        elif user_choice == "2":
            salary = input("Введите минимальный порог зарплаты:\n")
            print()
            # Вызываем функцию поиска по минимальной зарплате
            vacancies_by_salary = JSONSaver()
            list_of_vacancies = vacancies_by_salary.get_vacancies_by_salary(salary)
            for vacancy in list_of_vacancies:
                print(vacancy)
        elif user_choice == "3":
            # Вызываем функцию для отображения всех найденных вакансий по ключевому слову
            all_vacancies = JSONSaver()
            list_of_vacancies = all_vacancies.get_vacancies()
            for vacancy in list_of_vacancies:
                print(vacancy)
        elif user_choice == "4":
            top = input("Введите количество вакансий, которое нужно вывести:\n")
            print()
            # Вызываем функцию вывода определенного количества вакансий, отсортированных по минимальной зарплате
            top_vacancies = JSONSaver()
            list_of_vacancies = top_vacancies.get_top_vacancies(top)
            for vacancy in list_of_vacancies:
                print(vacancy)
        elif user_choice == "5":
            break
        else:
            continue
        answer = input("<Конец выборки>\n\nНажмите 'n' для выхода или любую другую клавишу, чтобы продолжить\n")
        if answer == "n":
            break
        else:
            continue
