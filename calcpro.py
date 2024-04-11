from tkinter import *
import webbrowser


win=Tk()
win.title("Calculator")
win.geometry("500x675+500+80")
win.resizable(0,0)
win.config(bg="black")
win.iconbitmap("C:\\Users\\Hp\\Downloads\\calcu.ico")

def opensite(url):
    webbrowser.open_new_tab(url)
    

i=0
eq=""

def show(value):
    global i
    global eq
    if value=="%":
        value="/100"
    eq+=value
    res.insert(i,value)
    i=i+1


def clear():
    global eq
    res.delete(0,END)
    eq=""


def calculate():
    global eq
    result=""
    result=eval(eq)
    res.delete(0,END)
    res.insert(0,result)

    

res=Entry(win,font=("arial",42),bg="white",fg="black",bd=4,width=50,justify="right")
res.place(x=0,y=0)

btn1=Button(win,text="C",font=("arial",32,"bold"),bg="red",fg="white",bd=9,width=4,command=clear)
btn1.place(x=0,y=75)

btn2=Button(win,text="%",font=("arial",32,"bold"),bg="grey",fg="white",bd=9,width=4,command=lambda:show("%"))
btn2.place(x=125,y=75)


btn3=Button(win,text="/",font=("arial",32,"bold"),bg="grey",fg="white",bd=9,width=4,command=lambda:show("/"))
btn3.place(x=250,y=75)


btn4=Button(win,text="*",font=("arial",32,"bold"),bg="grey",fg="white",bd=9,width=4,command=lambda:show("*"))
btn4.place(x=375,y=75)


btn6=Button(win,text="7",font=("arial",32,"bold"),bg="black",fg="white",bd=9,width=4,command=lambda:show("7"))
btn6.place(x=0,y=173)

btn7=Button(win,text="8",font=("arial",32,"bold"),bg="black",fg="white",bd=9,width=4,command=lambda:show("8"))
btn7.place(x=125,y=173)

btn8=Button(win,text="9",font=("arial",32,"bold"),bg="black",fg="white",bd=9,width=4,command=lambda:show("9"))
btn8.place(x=250,y=173)

btn9=Button(win,text="-",font=("arial",32,"bold"),bg="grey",fg="white",bd=9,width=4,command=lambda:show("-"))
btn9.place(x=375,y=173)

btn10=Button(win,text="4",font=("arial",32,"bold"),bg="black",fg="white",bd=9,width=4,command=lambda:show("4"))
btn10.place(x=0,y=273)

btn11=Button(win,text="5",font=("arial",32,"bold"),bg="black",fg="white",bd=9,width=4,command=lambda:show("5"))
btn11.place(x=125,y=273)

btn12=Button(win,text="6",font=("arial",32,"bold"),bg="black",fg="white",bd=9,width=4,command=lambda:show("6"))
btn12.place(x=250,y=273)

btn13=Button(win,text="+",font=("arial",32,"bold"),bg="grey",fg="white",bd=9,width=4,command=lambda:show("+"))
btn13.place(x=375,y=273)

btn14=Button(win,text="1",font=("arial",32,"bold"),bg="black",fg="white",bd=9,width=4,command=lambda:show("1"))
btn14.place(x=0,y=373)

btn15=Button(win,text="2",font=("arial",32,"bold"),bg="black",fg="white",bd=9,width=4,command=lambda:show("2"))
btn15.place(x=125,y=373)

btn16=Button(win,text="3",font=("arial",32,"bold"),bg="black",fg="white",bd=9,width=4,command=lambda:show("3"))
btn16.place(x=250,y=373)

btn17=Button(win,text="=",font=("arial",32,"bold"),bg="green",fg="white",bd=9,height=3,width=4,command=calculate)
btn17.place(x=375,y=373)

btn17=Button(win,text="0",font=("arial",32,"bold"),bg="black",fg="white",bd=9,width=9,height=1,command=lambda:show("0"))
btn17.place(x=0,y=473)

btn17=Button(win,text=".",font=("arial",32,"bold"),bg="black",fg="white",bd=9,width=4,height=1,command=lambda:show("."))
btn17.place(x=250,y=473)


label=Label(win,text="www.hubnettech.net",font=("monotype corsiva",36,"bold"),bg="black",fg="white")
label.place(x=80,y=600)
label.bind("<Button-1>",lambda e:opensite("https://www.hubnettech.net"))





 


win.mainloop()
