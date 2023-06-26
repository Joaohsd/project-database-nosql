from database.personDB import PersonDB

class MenuPerson:
    def __init__(self, person_db:PersonDB):
        self.__person_db = person_db
        
        self.__options = {
            1: 'Create Person',
            2: 'Read Person',
            3: 'Update Person Address',
            4: 'Update Person Password',
            5: 'Delete Person',
            6: 'Confirm presence in event',
            7: 'Exit Person Menu'
        }
        
        self.__parameter_methods = {
            1: self.create_person_parameters,
            2: self.read_person_by_cpf_parameters,
            3: self.update_person_address_parameters,
            4: self.update_person_password_parameters,
            5: self.delete_person_parameters,
            6: self.create_confirmation_in_event_parameters
        }
        
        self.__query_methods = {
            1: self.__person_db.create_person,
            2: self.__person_db.read_person_by_cpf,
            3: self.__person_db.update_person_address,
            4: self.__person_db.update_person_password,
            5: self.__person_db.delete_person,
            6: self.__person_db.create_confirmation_in_event
        }

    def __print_menu(self):
        print('--- Menu ---')
        print()

        for key, value in self.__options.items():
            print (key, '--', value)

        print()
    
    def create_person_parameters(self):
        name = str(input('Type Name: '))
        cpf = str(input('Type CPF: '))
        email = str(input('Type E-mail: '))
        password = str(input('Type PASSWORD: '))
        age = int(input('Type Age: '))
        address = str(input('Type Address: '))
        return {'name':name, 'cpf':cpf, 'email':email, 'password':password, 'age':age, 'address':address}
    
    def read_person_by_cpf_parameters(self):
        cpf = str(input('Type CPF: '))
        return {'cpf':cpf}
    
    def update_person_address_parameters(self):
        cpf = str(input('Type CPF: '))
        address = str(input('Type ADDRESS: '))
        return {'cpf':cpf, 'address': address}
    
    def update_person_password_parameters(self):
        cpf = str(input('Type CPF: '))
        password = str(input('Type PASSWORD: '))
        return {'cpf':cpf, 'password':password}
    
    def delete_person_parameters(self):
        cpf = str(input('Type CPF: '))
        return {'cpf':cpf}
    
    def create_confirmation_in_event_parameters(self):
        cpf = str(input('Type CPF: '))
        event_name = str(input('Type Event Name: '))
        return {'cpf':cpf, 'name':event_name}

    def parameter_query(self, option):
        return self.__parameter_methods[option]()

    def execute_query(self, option):
        parameters = self.parameter_query(option)
        return self.__query_methods[option](parameters)

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
            
