from datetime import date

class Event:
    def __init__(self, name:str, date:date, location:dict):
        self._name = name
        self._date = date
        self._location = location

    def get_name(self) -> str:
        return self._name

    def set_name(self, name):
        self._name = name

    def get_date(self) -> date:
        return self._date

    def set_date(self, date):
        self._date = date

    def get_location(self) -> dict:
        return self._location

    def set_location(self, location):
        self._location = location

    def __str__(self) -> str:
        return f"Event(Name: {self._name}, Date: {self._date.strftime('%Y-%m-%d')}, Location: {self._location['city']}, {self._location['state']}-{self._location['country']})"
