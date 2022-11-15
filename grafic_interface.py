from tkinter import *
from tkinter import ttk
root = Tk()     # создаем корневой объект - окно
root.title('Телефонный справочник')     # устанавливаем заголовок окна
root.geometry('1000x500')    # устанавливаем размеры окна
root.resizable(False, False)

#меню
menubar = Menu()
file_menu = Menu(tearoff=0)
file_menu.add_command(label='Импорт')
file_menu.add_command(label='Экспорт')
menubar.add_cascade(label='Файл',menu=file_menu)
menubar.add_command(label='Выход',command=root.quit)

root.config(menu=menubar)

#поиск
top_frame = Frame(root)
top_frame.pack()

Label(top_frame, text = 'Поиск').grid(row = 1, column = 1, sticky = N)
ttk.Entry(top_frame, width = 40).grid(row = 1, column = 2)
ttk.Button(top_frame, text = 'Найти',).grid(row = 1, column = 3)
#таблица
# определяем данные для отображения
people = [('Иван','Иванович','Иванов','222-333','первый'),('Иван','Иванович','Иванов','222-555','второй')]
 
# определяем столбцы
columns = ('name','father_name','last_name', 'phone', 'comment')
 
tree = ttk.Treeview(columns=columns, show='headings')
tree.pack(fill=BOTH, expand=1)
 
# определяем заголовки
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

ttk.Button(bottom_frame, text = 'Добавить',).grid(row = 1, column = 1)
ttk.Button(bottom_frame, text = 'Редактировать',).grid(row = 1, column = 2)
ttk.Button(bottom_frame, text = 'Удалить',).grid(row = 1, column = 3)
root.mainloop()