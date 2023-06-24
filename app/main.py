from database.database import Database
from database.personDB import PersonDB

from cli.menu_person import MenuPerson

menu_options = {
        1: 'Create Person',
        2: 'Read Person Contact',
        3: 'Read Person Age',
        4: 'Update Person Address',
        5: 'Update Person Password',
        6: 'Delete Person',
        7: 'Exit',
}
    
def print_menu():
    print('--- Menu ---')
    print()

    for key in menu_options.keys():
        print (key, '--', menu_options[key] )

    print()

def print_query_answer(query_answer):
    print()
    print('Query Answer: ' + str(query_answer))

def input_query_parameters(query_type):
    if query_type == 'create':
        name = str(input('Type Name: '))
        cpf = str(input('Type CPF: '))
        email = str(input('Type E-mail: '))
        password = str(input('Type PASSWORD: '))
        age = str(input('Type Age: '))
        address = str(input('Type Address: '))
        return (name, cpf, email, password, age, address)
    elif query_type == 'read':
        cpf = str(input('Type CPF: '))
        return cpf
    elif query_type == 'update':
        cpf = str(input('Type CPF: '))
        parameter_to_update = str(input('Type Parameter: '))
        return (cpf, parameter_to_update)
    elif query_type == 'delete':
        cpf = str(input('Type CPF: '))
        return cpf

if __name__ == '__main__':
    uri = str(input('Type URI: '))
    user = str(input('Type USER: '))
    password = str(input('Type PASSWORD: '))

    db = Database(uri, user, password)

    person_db = PersonDB(db)

    menu_person = MenuPerson(person_db)

    while(True):
        print()
        print_menu()
        option = ''
        try:
            option = int(input('Enter your choice: '))
        except:
            print('Wrong input. Please enter a number ...')
        if option == 1:
            name, cpf, email, password, age, address = input_query_parameters('create')
            print_query_answer(person_db.create_person(name, cpf, email, password, age, address))
        elif option == 2:
            cpf = input_query_parameters('read')
            print_query_answer(person_db.read_person_contact(cpf))
        elif option == 3:
            cpf = input_query_parameters('read')
            print_query_answer(person_db.read_person_age(cpf))
        elif option == 4:
            cpf, parameter_to_update = input_query_parameters('update')
            print_query_answer(person_db.update_person_address(cpf, parameter_to_update))
        elif option == 5:
            cpf, parameter_to_update = input_query_parameters('update')
            print_query_answer(person_db.update_person_password(cpf, parameter_to_update))
        elif option == 6:
            cpf = input_query_parameters('delete')
            print_query_answer(person_db.delete_person(cpf))
        elif option == 7:
            print_query_answer('Thanks for using our service!')
            exit()
        else:
            print('Invalid option. Please enter a number between 1 and 7.')