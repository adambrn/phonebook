from tkinter import *
from tkinter import ttk
from gui_function import *

def gui_view(people):

    root = Tk()     # создаем корневой объект - окно
    root.title('Телефонный справочник')     # устанавливаем заголовок окна
    root.geometry('1000x500')    # устанавливаем размеры окна
    root.resizable(False, False)

    #меню
    menubar = Menu()
    file_menu = Menu(tearoff=0)
    file_menu.add_command(label='Импорт', command=lambda:import_file(tree))
    file_menu.add_command(label='Экспорт в txt', command=lambda:export_to_txt())
    file_menu.add_command(label='Экспорт в csv', command=lambda:export_to_csv())
    menubar.add_cascade(label='Файл',menu=file_menu)
    menubar.add_command(label='Выход',command=root.quit)

    root.config(menu=menubar)

    #поиск
    top_frame = Frame(root)
    top_frame.pack()

    Label(top_frame, text = 'Поиск').grid(row = 1, column = 1, sticky = N)
    search_entry = ttk.Entry(top_frame, width = 40)
    search_entry.grid(row = 1, column = 2)
    ttk.Button(top_frame, text = 'Найти',command=lambda:search(search_entry,tree)).grid(row = 1, column = 3)
    ttk.Button(top_frame, text = 'Очистить поиск',command=lambda:update_tree(tree,db_get(path,'people'))).grid(row = 1, column = 4)
    
    #таблица

    # определяем столбцы
    columns = ('id','name','father_name','last_name', 'phone', 'comment')
    
    tree = ttk.Treeview(columns=columns, show='headings')
    tree.pack(fill=BOTH, expand=1)
    
    # определяем заголовки
    tree.heading('id', text='№')
    tree.column('id',minwidth=0,width=30)
    tree.heading('name', text='Имя')
    tree.heading('father_name', text='Отчество')
    tree.heading('last_name', text='Фамилия')
    tree.heading('phone', text='Телефон')
    tree.heading('comment', text='Примечание')
    
    # добавляем данные
    for person in people:
        tree.insert('', END, values=person)

    #кнопки записей
    bottom_frame = Frame(root)
    bottom_frame.pack()

    ttk.Button(bottom_frame, text = 'Добавить',command=lambda: add(tree)).grid(row = 1, column = 1)
    ttk.Button(bottom_frame, text = 'Редактировать',command=lambda: edit(tree)).grid(row = 1, column = 2)
    ttk.Button(bottom_frame, text = 'Удалить',command=lambda: delete(tree)).grid(row = 1, column = 3)
    root.mainloop()