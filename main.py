from tkinter import*
from tkinter import filedialog
from tkinter import messagebox
from tkinter import colorchooser
m='white'
t=Tk()
t.title("Lili text editor")
t.iconphoto(False,PhotoImage(file='image.png'))
t["bg"]="#000033"
f_text=Frame(t)
f_text['bg']='#000033'

text=Text(f_text,bg="#000033",fg=m,wrap=WORD,insertbackground="lime",selectbackground="#000099",spacing3=10)
def v(vc):
 text["font"]=vc
def save(event):
    filepath = filedialog.asksaveasfilename(title="Save file", initialdir="C:/", defaultextension="txt", initialfile="lilli.txt")
    if filepath != "":
        text1 = text.get("1.0", END)
        with open(filepath, "w") as file:
            file.write(text1)

def openfile(event):
    filepath1=filedialog.askopenfilename(title="Open file", initialdir="C:/", defaultextension="lili.txt", initialfile="")
    if filepath1 != "":
        with open(filepath1, "r") as file:
            text1 = file.read()
            text.insert("1.0", text1)
def help(event):
    messagebox.askokcancel("help Lili editor","up-save down-open alt_r-шрифт alt_l-цвет")
def version(event):
    messagebox.showwarning("version Lili editor", "2024 01.1 release")
def color1(event):
    global m
    rgb,hx=colorchooser.askcolor(title="Выбрать цвет шрифта")
    text['fg']=hx
def color2(event):
    global v
    v2=t.tk.call("tk", "fontchooser", "configure", "-font",text["font"], "-command", t.register(v),"-title","Шрифт текста")
    v1=t.tk.call("tk", "fontchooser", "show")
f_text.pack(fill=BOTH,expand=1)
scroll=Scrollbar(f_text,command=text.yview)
scroll.pack(side=RIGHT,fill=Y)
text.pack(expand=1,fill=BOTH,side=LEFT,pady=10,padx=10)
text.bind("<KeyPress-Up>",save)
text.bind("<KeyPress-Down>",openfile)
text.bind("<KeyPress-Left>",help)
text.bind("<KeyPress-Right>",version)
text.bind("<KeyPress-Alt_L>",color1)
text.bind("<KeyPress-Alt_R>",color2)
text.config(yscrollcommand=scroll.set)
t.event_add('<<Paste>>', '<Control-igrave>')
t.event_add("<<Copy>>", "<Control-ntilde>")
t.mainloop()