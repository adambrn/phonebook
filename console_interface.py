import crud
def view(data):
    
    print('Показать все - 1 ')
    print('Добавить - 2 ')
    print('Редактировать - 3 ')
    print('Удалить - 4 ')
    value = input('Выбирите действие :')
    match value:
        case 1:
            crud.read_record()
        case 2:
            crud.create_record()
        case 3:
            crud.update_record()
        case 4:
            crud.delete_record()