import tkinter as tk
import random
from tkinter import messagebox
t=tk.Tk()
t.title("1xbet(beta)")
v6="₽:"
v1=100
v2="Твоя сумма:"
v3="₽:"
v4=100
v5="Сумма противника:"
b2=tk.Entry(width=30,fg='Green',font=30,bg="light yellow")
b1=tk.Label(width=30,fg='Green',font=30,bg="light yellow",text="")
b3=tk.Label(width=30,text=f"{v2}{v6}{v1}",fg='blue',font=30)
b4=tk.Label(width=30,text=f"{v5}{v3}{v4}",fg='red',font=30)
def qw():
    global v1
    global v4
    r = random.randint(0, 100)
    v=random.randint(1,2)
    b1.configure(text=r)
    if v==1:
        n=float(b2.get())
        n2 = float(b1["text"])
        v1+=n
        v4-=n2

        b3.configure(text=f"{v2}{v6}{v1}")
        b4.configure(text=f"{v5}{v3}{v4}")
        messagebox.askokcancel("Молодец","Ты выйграл")
    if v==2:
        n=float(b1["text"])
        n1=float(b2.get())

        v4+=n
        v1-=n1
        b3.configure(text=f"{v2}{v6}{v1}")
        b4.configure(text=f"{v5}{v3}{v4}")
        messagebox.askokcancel("Молодец", "Ты проиграл")
    if v4<=0:
     messagebox.showwarning("Молодец", "Ты выйграл соперника")
     quit()
    if v1<=0:
     messagebox.showwarning("Молодец", "Тебя соперник выйграл")
     quit()



b=tk.Button(text="ставка",width=30,height=2,fg='Green',font=30,command=qw)



b.place(x=500,y=660)
b2.place(x=0,y=330)
b1.place(x=1090,y=330)
b3.place(x=0,y=280)
b4.place(x=1090,y=280)
t.mainloop()