# Database
from database.database import Database

# Entity
from entity.person import Person

class PersonDB:
    def __init__(self, database):
        self.__db = database

    def create_person(self, name, cpf, email, password, age, address):
        query = "CREATE (:Person {name: $name, cpf:$cpf, email:$email, password:$password, age:$age, address:$address})"
        parameters = {"name": name, "cpf": cpf, "email": email, "password": password, "age": age, "address": address}
        self.__db.execute_query(query, parameters)

    def create_event_producer(self, name, cpf, email, password, age, address):
        query = "CREATE (:Person:Organizer {name: $name, cpf:$cpf, email:$email, password:$password, age:$age, address:$address})"
        parameters = {"name": name, "cpf": cpf, "email": email, "password": password, "age": age, "address": address}
        self.__db.execute_query(query, parameters)
    
    def read_person_contact(self, cpf):
        query = "MATCH (p:Person{cpf:$cpf}) RETURN p.name AS name, p.email AS email, p.cpf AS cpf LIMIT 1"
        parameters = {"cpf": cpf}
        results = self.__db.execute_query(query, parameters)
        return [[result["name"], result["email"], result["cpf"]] for result in results]
    
    def read_person_age(self, cpf):
        query = "MATCH (p:Person{cpf:$cpf}) RETURN p.name AS name, p.age AS age LIMIT 1"
        parameters = {"cpf": cpf}
        results = self.__db.execute_query(query, parameters)
        return [[result["name"], result["age"]] for result in results]
    
    def update_person_address(self, cpf, new_address):
        query = "MATCH (p:Person {cpf: $cpf}) SET p.address = $new_address"
        parameters = {"cpf": cpf, "new_address": new_address}
        self.__db.execute_query(query, parameters)
    
    def update_person_password(self, cpf, new_password):
        query = "MATCH (p:Person {cpf: $cpf}) SET p.password = $new_password"
        parameters = {"cpf": cpf, "new_password": new_password}
        self.__db.execute_query(query, parameters)

    def delete_person(self, cpf):
        query = "MATCH (p:Person {cpf: $cpf}) DETACH DELETE p"
        parameters = {"cpf": cpf}
        self.__db.execute_query(query, parameters)