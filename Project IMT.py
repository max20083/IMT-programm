from tkinter import *
from tkinter import Toplevel
login='Admin'
password='12345'


def clicked_auto():
    global rost_input,mas_input,otv
    if login_entry.get()==login and password_entry.get()==password:
     root = Toplevel(sign)
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
     status_lbl.configure(text='Успешный вход', fg='green')
     Autoriz_button.destroy()




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
     status_lbl.configure(text='Успешный вход', fg='green')

    else:
        status_lbl.configure(text='Неверный логин или пароль', fg='red')

def clicked():
    rost_get = rost_input.get()
    mas_get = mas_input.get()
    if rost_get==str or mas_get==str:
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


sign = Tk()
sign.title('Авторизация')
sign.geometry('300x200')
frame_login=Frame(sign)
frame_login.pack()
login_lbl = Label(frame_login, text='логин')
login_lbl.pack(side=LEFT,padx=0,pady=5)
login_entry = Entry(frame_login , width=10)
login_entry.pack(side=LEFT,padx=10,pady=5)
frame_password=Frame(sign)
frame_password.pack()
password_lbl = Label(frame_password, text='пароль')
password_lbl.pack(side=LEFT,padx=0,pady=0)
password_entry=Entry(frame_password , width=10)
password_entry.pack(side=LEFT,padx=10,pady=0)
frame_auto=Frame(sign)
frame_auto.pack()
Autoriz_button = Button(frame_auto, text='Войти', width=10,command=clicked_auto)
Autoriz_button.pack(side=LEFT, pady=30, padx=100)
frame_status=Frame(sign)
frame_status.pack()
status_lbl = Label(frame_status, text='')
status_lbl.pack(side=LEFT,padx=0,pady=0)


sign.mainloop()
