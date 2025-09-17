from tkinter import *

def clicked():
    rost_get = rost_input.get()
    mas_get = mas_input.get()
    r = (float(rost_get))/100
    m = (float(mas_get))
    imt = round(m / (r ** 2), 2)
    otv.configure(text=(f'Индекс - '+ str(imt)))
    try:
        with open('Резулльтаты индекса масс тела.txt', 'a', encoding='utf-8') as file:
            file.write('Индекс массы тела при росте ' + str(r) + '(м) и весе' + str(m) + '(кг) равен ' + (str(imt)) + '\n')
    except:
        otv.configure(text='Ошибка при работе с файлом')
root = Tk()
root.title('Расчет индекча массы тела')
root.geometry('400x200')
lbl=Label(root , text='Привет это приложение длдя расчета индекса массы тела')
lbl.grid(column=0, row=0)
rost=Label(root , text='Введи сюда свой рост  ')
rost_input= Entry(root,width=10)
mas=Label(root , text='А сюда свой вес  ')
mas_input= Entry(root,width=10)
rasch=Button(root , text='Расчитать индекс массы тела', command = clicked)
otv=Label(root , text='индекс - ?')


lbl.pack()
rost.pack()
rost_input.pack()
mas.pack()
mas_input.pack()
rasch.pack(pady=10)
otv.pack(pady=10)
root.mainloop()