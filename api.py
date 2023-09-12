from abc import ABC, abstractmethod
import requests
import json


class API(ABC):
    """
    Абстрактный класс для работы с API сайтов с вакансиями
    """
    @abstractmethod
    def get_vacancies(self, search_query):
        pass


class HeadHunterAPI(API):
    """
    Класс для работы с API сайта с вакансиями HeadHunter
    """
    def get_vacancies(self, search_query):
        """
        Подключается к API и получает вакансии
        """
        params = {
            "text": search_query,
            "per_page": 100,
        }
        response = requests.get('https://api.hh.ru/vacancies/', params=params)
        data = response.content.decode()
        vacancies = json.loads(data)
        return vacancies


class SuperJobAPI(API):
    """
    Класс для работы с API сайта с вакансиями SuperJob
    """
    def get_vacancies(self, search_query):
        """
        Подключается к API и получает вакансии
        """
        headers = {
            "X-Api-App-Id": "v3.r.137800309.b82664b4ec3df1c1ddda1a9e8f50fc00a0cb9968"
                            ".0a48d412d51d6b2172e47fcb660f8c085c82aa2f"
        }
        params = {
            "keyword": search_query,
            "count": 100,
        }
        response = requests.get('https://api.superjob.ru/2.0/vacancies/', headers=headers, params=params)
        data = response.content.decode()
        vacancies = json.loads(data)
        return vacancies
