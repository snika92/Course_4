class Vacancy:
    """
    Класс для работы с вакансиями
    """

    def __init__(self, id, name, salary, url, city, employer):
        self.id = id
        self.name = name
        self.salary = salary
        self.url = url
        self.city = city
        self.employer = employer

    def __dict__(self):
        return {"id": self.id,
                "name": self.name,
                "salary": self.salary,
                "url": self.url,
                "city": self.city,
                "employer": self.employer}

    def __ge__(self, other):
        return self.salary >= other.salary
