from database.database import Database
from database.personDB import PersonDB

uri = str(input('Type URI: '))
user = str(input('Type USER: '))
password = str(input('Type PASSWORD: '))

db = Database(uri, user, password)

person_db = PersonDB(db)

# Create
person_db.create_person('Pedro Souza', '189.052.396-66', 'teste@gmail.com', 'teste123', 35, 'SRS')
person_db.create_event_producer ('Carlos Silva', '111.111.111-11', 'teste123@gmail.com', 'teste12345', 21, 'Rua Coronel Teste')
# Read
print(person_db.read_person_contact('189.052.396-66'))
# Update
person_db.update_person_address('189.052.396-66', 'Rua Capitão Teste')