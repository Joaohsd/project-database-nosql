# Database
from database.database import Database

# Entity
from entity.person import Person

class PersonDB:
    def __init__(self, database:Database):
        self.__db = database

    def __check_if_cpf_is_registered(self, cpf):
        query = "MATCH (p:Person{cpf:$cpf}) RETURN p.cpf AS cpf LIMIT 1"
        parameter = {"cpf": cpf}
        results = self.__db.execute_query(query, parameter)
        if results:
            return True
        else:
            return False
    
    def __execute_query(self, query, parameters, query_type):
        if self.__check_if_cpf_is_registered(parameters['cpf']):
            if query_type == 'create':
                return 'There is already a person registered with this cpf'
            elif query_type == 'read':
                return self.__db.execute_query(query, parameters)
            else:
                self.__db.execute_query(query, parameters)
                return 'Query done successfully'
        else:
            if query_type == 'create':
                self.__db.execute_query(query, parameters)
                return 'Query done successfully'
            else:
                return 'CPF not registered'
                
    def create_person(self, parameters):
        query = "CREATE (:Person {name: $name, cpf:$cpf, email:$email, password:$password, age:$age, address:$address})"
        parameters = {"name": parameters['name'], "cpf": parameters['cpf'], "email": parameters['email'], "password": parameters['password'], "age": parameters['age'], "address": parameters['address']}
        return self.__execute_query(query, parameters, 'create')

    def read_person_by_cpf(self, parameters):
        query = "MATCH (p:Person{cpf:$cpf}) RETURN p.name AS name, p.email AS email, p.cpf AS cpf, p.address AS address, p.age AS age LIMIT 1"
        parameter = {"cpf": parameters['cpf']}
        results = self.__db.execute_query(query, parameter)
        if results:
            persons = []
            for result in results:
                person = Person(result['name'], result['cpf'], result['email'], '', result['age'], result['address'])
                persons.append(person)
            return persons
        else:
            return []

    def read_person_contact(self, parameters):
        query = "MATCH (p:Person{cpf:$cpf}) RETURN p.name AS name, p.email AS email, p.cpf AS cpf LIMIT 1"
        parameter = {"cpf": parameters['cpf']}
        results = self.__execute_query(query, parameter, 'read')
        if isinstance(results, str):
            return results
        else:
            return [[result["name"], result["email"], result["cpf"]] for result in results]
    
    def read_person_age(self, cpf):
        query = "MATCH (p:Person{cpf:$cpf}) RETURN p.name AS name, p.age AS age LIMIT 1"
        parameter = {"cpf": cpf['cpf']}
        results = self.__execute_query(query, parameter, 'read')
        if isinstance(results, str):
            return results
        else:
            return [[result["name"], result["age"]] for result in results]
    
    def update_person_address(self, parameters):
        query = "MATCH (p:Person {cpf: $cpf}) SET p.address = $new_address"
        parameters = {"cpf": parameters['cpf'], "new_address": parameters['address']}
        return self.__execute_query(query, parameters, 'update')
    
    def update_person_password(self, parameters):
        query = "MATCH (p:Person {cpf: $cpf}) SET p.password = $new_password"
        parameters = {"cpf": parameters['cpf'], "new_password": parameters['password']}
        return self.__execute_query(query, parameters, 'update')

    def delete_person(self, cpf):
        query = "MATCH (p:Person {cpf: $cpf}) DETACH DELETE p"
        parameters = {"cpf": cpf['cpf']}
        return self.__execute_query(query, parameters, 'delete')
    
    def create_confirmation_in_event(self, parameters):
        query = "MATCH (p:Person{cpf:$cpf}),(e:Event{name:$event_name}) CREATE (p)-[:CONFIRMADO_EM]->(e)"
        parameters = {"cpf": parameters["cpf"], "event_name": parameters["name"]}
        self.__db.execute_query(query, parameters)