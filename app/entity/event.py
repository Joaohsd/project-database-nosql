from neo4j.time import Date

class Event:
    def __init__(self, name:str, date:Date, location:dict):
        self.__name = name
        self.__date = date
        self.__location = location

    def get_name(self) -> str:
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_date(self) -> Date:
        return self.__date

    def set_date(self, date):
        self.__date = date

    def get_location(self) -> dict:
        return self.__location

    def set_location(self, location):
        self.__location = location

    def __str__(self) -> str:
        return f"Event(Name: {self.__name}, Date: {self.__date}, Location: {self.__location['country']}, {self.__location['state']}, {self.__location['city']})"
