from database.database import Database
from database.personDB import PersonDB

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
            person_db.create_person(name, cpf, email, password, age, address)
        elif option == 2:
            query_parameters = input_query_parameters('read')
        elif option == 3:
            query_parameters = input_query_parameters('read')
        elif option == 4:
            query_parameters = input_query_parameters('update')
        elif option == 5:
            query_parameters = input_query_parameters('update')
        elif option == 6:
            query_parameters = input_query_parameters('delete')
        elif option == 7:
            print('Thanks for using our service!')
            exit()
        else:
            print('Invalid option. Please enter a number between 1 and 7.')