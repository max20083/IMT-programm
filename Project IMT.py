from tkinter import *

def clicked():
    rost_get = rost_input.get()
    mas_get = mas_input.get()
    if rost_get!= float or mas_get != float:
        otv.configure(text='Введите в поле ввода число)')
    else:
     r = (float(rost_get))/100
     m = (float(mas_get))
     imt = round(m / (r ** 2), 2)
     otv.configure(text=(f'Индекс - '+ str(imt)))
     try:
        with open('Резулльтаты индекса масс тела', 'a', encoding='utf-8') as file:
            file.write('Индекс массы тела при росте ' + str(r) + '(м) и весе ' + str(m) + '(кг) равен ' + (str(imt)) + '\n')
            file.close()
     except:
        otv.configure(text='Ошибка при работе с файлом')
def clear_one():
    try:
        with open('Резулльтаты индекса масс тела', 'w', encoding='utf-8') as file:
            file.write(' ')
            file.close()
    except:
        otv.configure(text='ошибка при работе с файлом')

root = Tk()
root.title('Расчет индекча массы тела')
root.geometry('500x200')
lbl=Label(root , text='Привет это приложение длдя расчета индекса массы тела')
lbl.grid(column=0, row=0)
rost=Label(root , text='Введи сюда свой рост  ')
rost_input= Entry(root,width=10)
mas=Label(root , text='А сюда свой вес  ')
mas_input= Entry(root,width=10)
rasch=Button(root , text='Расчитать индекс массы тела', command = clicked)
otv=Label(root , text='индекс - ?')
clear_Button=Button(root, text='Clear data', command=clear_one, width=8, height=8)


lbl.pack()
rost.pack()
rost_input.pack()
mas.pack()
mas_input.pack()
rasch.pack(pady=10)
otv.pack(pady=10)
clear_Button.pack()
clear_Button.place(x=400, y=35)
root.mainloop()
