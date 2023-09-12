from abc import ABC, abstractmethod
import json


class VacancyFileManager(ABC):
    """
    Абстрактный класс, который обязывает реализовать методы для добавления вакансий в файл,
    получения данных из файла по указанным критериям и удаления информации о вакансиях
    """

    @abstractmethod
    def add_vacancy(self):
        pass

    @abstractmethod
    def get_vacancies_by_salary(self):
        pass

    @abstractmethod
    def delete_vacancy(self):
        pass


class JSONSaver(VacancyFileManager):
    """
    Класс для сохранения информации о вакансиях в JSON - файл
    и работы с ней
    """

    @staticmethod
    def add_vacancy(vacancy):
        """
        Открывает файл и добавляет в список экземпляр объекта вакансии

        """
        with open("vacancies.json", "r", encoding="utf-8") as json_file:
            content = json.load(json_file)
        content.append(vacancy.__dict__())
        with open("vacancies.json", "w", encoding="utf-8") as json_file:
            json.dump(content, json_file, ensure_ascii=False, indent=2)

    @staticmethod
    def get_vacancies_by_city(city):
        """
        Открывает файл, фильтрует информацию по значению "city" и
        возвращает список строк в нужном формате
        """
        with open("vacancies.json", "r", encoding="utf-8") as json_file:
            content = json.load(json_file)
        result = filter(lambda x: x['city'] == city, content)
        list_of_vacancies = []
        for vacancy in result:
            list_of_vacancies.append(f"{vacancy['name']}\nЗ/п от: {vacancy['salary']}\nГород: {vacancy['city']}\n"
                                     f"Компания: {vacancy['employer']}\nПолное описание: {vacancy['url']}\n")
        return list_of_vacancies

    @staticmethod
    def get_vacancies_by_salary(salary):
        """
        Открывает файл, сортирует информацию по значению "salary" от меньшего к большему и
        возвращает список строк в нужном формате
        """
        with open("vacancies.json", "r", encoding="utf-8") as json_file:
            content = json.load(json_file)
        list_of_vacancies_for_sort = []
        for vacancy in content:
            if vacancy["salary"] >= int(salary):
                list_of_vacancies_for_sort.append(vacancy)
        sorted_vacancies = sorted(list_of_vacancies_for_sort, key=lambda x: x["salary"])
        list_of_vacancies = []
        for vacancy in sorted_vacancies:
            list_of_vacancies.append(f"{vacancy['name']}\nЗ/п от: {vacancy['salary']}\nГород: {vacancy['city']}\n"
                                     f"Компания: {vacancy['employer']}\nПолное описание: {vacancy['url']}\n")
        return list_of_vacancies

    @staticmethod
    def get_vacancies():
        """
        Открывает файл, получает все вакансии и
        возвращает список строк в нужном формате
        """
        with open("vacancies.json", "r", encoding="utf-8") as json_file:
            content = json.load(json_file)
        list_of_vacancies = []
        for vacancy in content:
            list_of_vacancies.append(f"{vacancy['name']}\nЗ/п от: {vacancy['salary']}\nГород: {vacancy['city']}\n"
                                     f"Компания: {vacancy['employer']}\nПолное описание: {vacancy['url']}\n")
        return list_of_vacancies

    @staticmethod
    def get_top_vacancies(top):
        """
        Открывает файл, сортирует информацию по значению "salary" от большего к меньшему, и
        возвращает список требуемого количества строк в нужном формате
        """
        with open("vacancies.json", "r", encoding="utf-8") as json_file:
            content = json.load(json_file)
        sorted_vacancies = sorted(content, key=lambda x: x["salary"], reverse=True)
        list_of_vacancies = []
        for digit in range(int(top)):
            list_of_vacancies.append(f"""{sorted_vacancies[digit]['name']}
З/п от: {sorted_vacancies[digit]['salary']}
Город: {sorted_vacancies[digit]['city']}
Компания: {sorted_vacancies[digit]['employer']}
Полное описание: {sorted_vacancies[digit]['url']}
""")
        return list_of_vacancies

    @staticmethod
    def delete_vacancy(id):
        """
        Удаляет вакансию из списка в файле по её id
        """
        with open("vacancies.json", "r", encoding="utf-8") as json_file:
            content = json.load(json_file)
        for vacancy in content:
            if vacancy["id"] == id:
                content.pop(vacancy)
        with open("vacancies.json", "w", encoding="utf-8") as json_file:
            json.dump(content, json_file, ensure_ascii=False, indent=2)
