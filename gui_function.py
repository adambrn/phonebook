from tkinter import ttk
from tkinter import *
from tkinter import filedialog
from tkinter.messagebox import showerror
from db_sqlite import db_delete, db_get, db_insert_people, db_insert_peoples, db_update_people
import file_operations
#import crud
path = file_operations.get_db_path()

#обновление списка из переменной
def update_tree(tree,people):
    for child in tree.get_children():
        tree.delete(child)
    for person in people:
        tree.insert('', END, values=person)

#Импорт файла
def import_file(tree):
    file = filedialog.askopenfilename(filetypes = [("csv files","*.csv")])
    people = file_operations.reading_csv(file)
    #file_operations.write_csv(path,people)
    db_insert_peoples(path,people)
    data = db_get(path,'people')
    update_tree(tree,data)

def export():
    file = filedialog.asksaveasfilename(initialfile= 'export_phone.txt',filetypes = [("txt files","*.txt")])
    data = db_get(path,'people')
    file_operations.export_to_txt(file,data)

#Функция удаления записи
def delete(tree):
    if tree.selection():
        selected_item = tree.selection()[0] ## get selected item
        values = tree.item(selected_item, option="values")
        #crud.delete_record(values,people)
        #file_operations.write_csv(path,people)
        db_delete(path,'people',values[0])
        tree.delete(selected_item)
    else:
        showerror(title="Ошибка", message="Выберите запись для удаления!")

#редактирование
def edit(tree):
    if tree.selection():
        selected_item = tree.selection()[0]
    else:
        showerror(title="Ошибка", message="Выберите запись для редактирования!")
        return
    # Всплывающее окно
    win = Toplevel()
    win.title("Редактировать")
    win.attributes("-toolwindow", True)

    values = tree.item(selected_item, option="values")
    edit_index = int(values[0])
    last_name_lable = Label(win, text = "Фамилия: ")
    last_name_entry = Entry(win)
    last_name_entry.insert(0, values[1]) 
    last_name_lable.grid(row = 0, column = 0)
    last_name_entry.grid(row = 0, column = 1)

    name_lable = Label(win, text = "Имя: ")
    name_entry = Entry(win)
    name_entry.insert(0, values[2]) 
    name_lable.grid(row = 1, column = 0)
    name_entry.grid(row = 1, column = 1)

    father_name_lable = Label(win, text = "Отчество: ")
    father_name_entry = Entry(win)
    father_name_entry.insert(0, values[3]) 
    father_name_lable.grid(row = 2, column = 0)
    father_name_entry.grid(row = 2, column = 1)

    phone_lable = Label(win, text = "телефон: ")
    phone_entry = Entry(win)
    phone_entry.insert(0, values[4]) 
    phone_lable.grid(row = 3, column = 0)
    phone_entry.grid(row = 3, column = 1)

    comment_lable = Label(win, text = "Комментарий: ")
    comment_entry = Entry(win)
    comment_entry.insert(0, values[5]) 
    comment_lable.grid(row = 4, column = 0)
    comment_entry.grid(row = 4, column = 1)
    
    
    def confirm_entry(tree, selected_item, entry1, entry2, entry3,entry4,entry5):
        tree.item(selected_item, values = (edit_index,entry1, entry2, entry3,entry4,entry5))
        #crud.update_record(edit_index, (entry1, entry2, entry3,entry4,entry5),people)
        #file_operations.write_csv(path,people)
        db_update_people(path,(entry1, entry2, entry3,entry4,entry5),edit_index)
        return True

    def update_then_destroy():
        if confirm_entry(tree, 
        selected_item,
        last_name_entry.get(), 
        name_entry.get(), 
        father_name_entry.get(), 
        phone_entry.get(),
        comment_entry.get()
        ):
            win.destroy()

    okButt = ttk.Button(win, text = "Сохранить",command=update_then_destroy)
    okButt.grid(row = 5, column = 0)

    canButt = ttk.Button(win, text = "Отмена",command=win.destroy)
    canButt.grid(row = 5, column = 1)

#Добавить
def add(tree):
    
    # Всплывающее окно
    win = Toplevel()
    win.title("Добавить")
    win.attributes("-toolwindow", True)

    last_name_lable = Label(win, text = "Фамилия: ")
    last_name_entry = Entry(win)
    last_name_lable.grid(row = 0, column = 0)
    last_name_entry.grid(row = 0, column = 1)

    name_lable = Label(win, text = "Имя: ")
    name_entry = Entry(win)
    name_lable.grid(row = 1, column = 0)
    name_entry.grid(row = 1, column = 1)

    father_name_lable = Label(win, text = "Отчество: ")
    father_name_entry = Entry(win)
    father_name_lable.grid(row = 2, column = 0)
    father_name_entry.grid(row = 2, column = 1)

    phone_lable = Label(win, text = "телефон: ")
    phone_entry = Entry(win)
    phone_lable.grid(row = 3, column = 0)
    phone_entry.grid(row = 3, column = 1)

    comment_lable = Label(win, text = "Комментарий: ")
    comment_entry = Entry(win)
    comment_lable.grid(row = 4, column = 0)
    comment_entry.grid(row = 4, column = 1)
    
    
    def ConfirmEntry(tree, entry1, entry2, entry3,entry4,entry5):
        if entry1 != '' or entry2 != '' or entry3 != '' or entry4 != '' or entry5 != '':
            values = (entry1, entry2, entry3, entry4, entry5)
            #crud.create_record(values,people)
            #file_operations.write_csv(path,people)
            db_insert_people(path,values)
            data = db_get(path,'people')
            update_tree(tree,data)
            return True
        else:
            showerror(title="Ошибка", message="Введите данные!")

    def addintree():
        if ConfirmEntry(tree, 
        last_name_entry.get(), 
        name_entry.get(), 
        father_name_entry.get(), 
        phone_entry.get(),
        comment_entry.get()
        ):
            win.destroy()

    okButt = ttk.Button(win, text = "Сохранить",command=addintree)
    okButt.grid(row = 5, column = 0)

    canButt = ttk.Button(win, text = "Отмена",command=win.destroy)
    canButt.grid(row = 5, column = 1)

#поиск
def search(search_entry,tree):
    selections = []
    people = db_get(path,'people')
    print(people)
    query = search_entry.get()
    for child in people:
        if query.lower() in ''.join(str(child)).lower():   
            selections.append(child)
    update_tree(tree,selections)

