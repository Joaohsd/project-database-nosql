from database.eventDB import EventDB
from neo4j.time import Date

class MenuEvent:
    def __init__(self, event_db:EventDB):
        self.__event_db = event_db
        
        self.__options = {
            1: 'Create Event',
            2: 'Read Event by name',
            3: 'Read Event by theme',
            4: 'Update Event Date',
            5: 'Update Event Location',
            6: 'Delete Event',
            7: 'Exit Event Menu'
        }

        self.__event_options = {
            1: 'Music',
            2: 'Festival',
            3: 'Gastronomy',
            4: 'Congress',
            5: 'Comedy',
            6: 'Religion',
            7: 'Online'
        }
        
        self.__parameter_methods = {
            1: self.create_event_parameters,
            2: self.read_event_by_name_parameters,
            3: self.read_event_by_theme_parameters,
            4: self.update_event_date_parameters,
            5: self.update_event_location_parameters,
            6: self.delete_event_parameters
        }
        
        self.__query_methods = {
            1: self.__event_db.create_event,
            2: self.__event_db.read_event_by_name,
            3: self.__event_db.read_event_by_theme,
            4: self.__event_db.update_event_date,
            5: self.__event_db.update_event_location,
            6: self.__event_db.delete_event_by_name
        }

    def __print_menu(self):
        print('--- Menu ---')
        print()

        for key, value in self.__options.items():
            print (key, '--', value)

        print()
    
    def __print_event_options(self):
        print('--- Menu ---')
        print()

        for key, value in self.__event_options.items():
            print (key, '--', value)

        print()
    
    def create_event_parameters(self):
        self.__print_event_options()
        label = int(input('Type Event theme: '))
        label = self.__event_options[label]
        name = str(input('Type Name: '))
        print('Date of event:')
        day = int(input('Type day of event:'))
        month = int(input('Type month of event (number):'))
        year = int(input('Type year of event:'))
        date = Date(year=year, month=month, day=day)
        print('Location of event:')
        country = str(input('Type country:'))
        state = str(input('Type state:'))
        city = str(input('Type city:'))
        
        location = {}
        location['country'] = country
        location['state'] = state
        location['city'] = city

        return {'label':label, 'name':name, 'date':date, 'location':location}
    
    def read_event_by_name_parameters(self):
        name = str(input('Type name: '))
        return {'name':name}

    def read_event_by_theme_parameters(self):
        self.__print_event_options()
        label = int(input('Type Event theme: '))
        label = self.__event_options[label]
        return {'label':label}
    
    def update_event_date_parameters(self):
        name = str(input('Type Name: '))
        print('Date of event:')
        day = int(input('Type day of event:'))
        month = int(input('Type month of event (number):'))
        year = int(input('Type year of event:'))
        date = Date(year=year, month=month, day=day)
        return {'name':name, 'date':date}
    
    def update_event_location_parameters(self):
        name = str(input('Type Name: '))
        print('Location of event:')
        country = str(input('Type country:'))
        state = str(input('Type state:'))
        city = str(input('Type city:'))
        location = {}
        location['country'] = country
        location['state'] = state
        location['city'] = city
        return {'name':name, 'location':location}
    
    def delete_event_parameters(self):
        name = str(input('Type name: '))
        return {'name': name}

    def parameter_query(self, option):
        return self.__parameter_methods[option]()

    def execute_query(self, option):
        parameters = self.parameter_query(option)
        result = self.__query_methods[option](parameters)
        return result

    def process(self):
        while True:
            self.__print_menu()
            option = -1
            try:
                option = int(input('Enter your choice: '))
                if option == max(self.__options.keys()):
                    break
                elif option in self.__options:
                    results = self.execute_query(option)
                    if option >= 2 and option <= 3:
                        if results:
                            for result in results:
                                print(result)
                        else:
                            print('Nothing found')
                else:
                    print('Enter a valid option.\n')
            except:
                print('Wrong input. Please enter with the correct entry ...\n')