# Database
from database.database import Database

# Entity
from entity.event import Event
from entity.person import Person

import json

class EventDB:
    def __init__(self, database:Database):
        self.__db = database

    def create_event(self, parameters):
        label = parameters['label']
        query = f'CREATE (:Event:{label}{{name: $name, date:$date, location:$location}})'
        parameters = {'name': parameters['name'], 'date': parameters['date'], 'location': json.dumps(parameters['location'])}
        self.__db.execute_query(query, parameters)
    
    def read_event_by_name(self, parameters):
        query = 'MATCH (e:Event{name:$name}) RETURN e.name AS name, e.date AS date, e.location AS location LIMIT 1'
        parameters = {'name': parameters['name']}
        results = self.__db.execute_query(query, parameters)
        if results:
            events = []
            result = results[0]
            event = Event(result['name'], result['date'], json.loads(result['location']))
            events.append(event)
            return events
        return None
    
    def read_event_by_theme(self, parameters):
        label = parameters['label']
        query = f'MATCH (e:{label}) RETURN e.name AS name, e.date AS date, e.location AS location ORDER BY e.name'
        results = self.__db.execute_query(query)
        if results:
            events = []
            print(results)
            for result in results:
                event = Event(result['name'], result['date'], json.loads(result['location']))
                events.append(event)
            return events
        return []
    
    def update_event_date(self, parameters):
        query = 'MATCH (e:Event{name: $name}) SET e.date = $date'
        parameters = {'name':parameters['name'], 'date':parameters['date']}
        self.__db.execute_query(query, parameters)
    
    def update_event_location(self, parameters):
        query = 'MATCH (e:Event{name: $name}) SET e.location = $location'
        parameters = {'name':parameters['name'], 'location':json.dumps(parameters['location'])}
        self.__db.execute_query(query, parameters)

    def delete_event_by_name(self, parameters):
        query = 'MATCH (e:Event {name: $name}) DETACH DELETE e'
        parameters = {'name': parameters['name']}
        self.__db.execute_query(query, parameters)

    def read_num_persons_in_event(self, parameters):
        query = "MATCH (p:Person)-[:CONFIRMADO_EM]->(e:Event{name:$event_name}) RETURN COUNT(p) AS number"
        parameters = {"event_name": parameters["name"]}
        results = self.__db.execute_query(query, parameters)
        if results:
            personsConfirmed = []
            for result in results:
                personsConfirmed.append(f"Number of persons confirmed in event: {result['number']}")
            return personsConfirmed
        else:
            return []
    
    def read_persons_in_event(self, parameters):
        query = "MATCH (p:Person)-[:CONFIRMADO_EM]->(e:Event{name:$event_name}) RETURN p.name AS name, p.email AS email, p.cpf AS cpf, p.address AS address, p.age AS age "
        parameters = {"event_name": parameters["name"]}
        results = self.__db.execute_query(query, parameters)
        if results:
            personsConfirmed = []
            for result in results:
                person = Person(result['name'], result['cpf'], result['email'], '', result['age'], result['address'])
                personsConfirmed.append(person)
            return personsConfirmed
        else:
            return []
        