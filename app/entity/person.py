class Person:
    def __init__(self, name:str, cpf:str, email:str, password:str, age:int, address:dict):
        self._name = name
        self._cpf = cpf
        self._email = email
        self._password = password
        self._age = age
        self._address = address

    def get_name(self) -> str:
        return self._name

    def set_name(self, name):
        self._name = name

    def get_cpf(self) -> str:
        return self._cpf

    def set_cpf(self, cpf):
        self._cpf = cpf

    def get_email(self) -> str:
        return self._email

    def set_email(self, email):
        self._email = email

    def get_password(self) -> str:
        return self._password

    def set_password(self, password):
        self._password = password

    def get_age(self) -> int:
        return self._age

    def set_age(self, age):
        self._age = age

    def get_address(self) -> dict:
        return self._address

    def set_address(self, address):
        self._address = address

    def __str__(self) -> str:
        return f"Person(Name: {self._name}, CPF: {self._cpf}, Email: {self._email}, Age: {self._age}, Address: {self._address['city']}, {self._address['state']}, {self._address['country']})"
