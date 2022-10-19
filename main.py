from pprintpp import pprint as pp
from db.escolaDB import EscolaDB


dao = EscolaDB()

while 1:
    option = input('1. Criar professor \n2. Criar materia\n3. Ler todos os nos \n4. Criar relacionamento\n')

    if option == '1':
        nome = input('  Nome: ')
        idade = input('   Idade : ')
        area = input('  Area : ')
        professor = {
            'nome': nome,
            'idade': idade,
            'area': area
        }
        aux = dao.create_professor(professor)
    elif option == '2':
        assunto = input('  Assunto: ')
        horario = input('   Horario : ')

        materia = {
            'assunto': assunto,
            'horario': horario
        }
        aux = dao.create_materia(materia)
    elif option == '3':
        aux = dao.read_all_nodes()
        pp(aux)

    elif option == '4':
        professor = input('  Professor: ')
        materia = input('   Materia : ')
        ano = input('   Ano : ')

        professor1 = { 'nome': professor }
        materia1 = { 'assunto': materia }
        aux = dao.create_relation(professor1, materia1, ano)

    else:
        break

dao.db.close()
