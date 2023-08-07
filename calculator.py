from tkinter import *
root=Tk()
root.title("CALCULATOR")
root.geometry("400x400")

r=Entry(root,width=60,borderwidth=5)
r.grid(columnspan=3,row=0,column=0,padx=5,pady=5)

def onClick(number):
    current=str(r.get())
   #print(current)
    r.delete(0,END)
    r.insert(0,str(current)+str(number))
def cLear():
    r.delete(0,END)
def adds():
    global numo
    numo=r.get()
    global opr
    opr="addition"
    r.delete(0,END)
def mul():
    global numo
    numo=r.get()
    global opr
    opr="multiplication"
    r.delete(0,END)
    
def div():
    global numo
    numo=r.get()
    global opr
    opr="division"
    r.delete(0,END)
    
def sub():
    global numo
    numo=r.get()
    global opr
    opr="subtraction"
    r.delete(0,END)
    

def EqualS():
    secondnum=int(r.get())
    r.delete(0,END)
    if opr=="addition":
        r.insert(0,int(numo)+secondnum)
    elif opr=="multiplication":
        r.insert(0,int(numo)*secondnum)
    elif opr=="division":
        r.insert(0,int(numo)/secondnum)
    elif opr=="subtraction":
        r.insert(0,int(numo)-secondnum)
        
   
   
   

    
    
button1=Button(root,text="1",padx=35,pady=15,command=lambda: onClick(1))
button2=Button(root,text="2",padx=35,pady=15,command=lambda: onClick(2))
button3=Button(root,text="3",padx=35,pady=15,command=lambda:onClick(3))
button4=Button(root,text="4",padx=35,pady=15,command=lambda:onClick(4))
button5=Button(root,text="5",padx=30,pady=15,command=lambda:onClick(5))
button6=Button(root,text="6",padx=30,pady=15,command=lambda:onClick(6))
button7=Button(root,text="7",padx=30,pady=15,command=lambda:onClick(7))
button8=Button(root,text="8",padx=30,pady=15,command=lambda:onClick(8))
button9=Button(root,text="9",padx=30,pady=15,command=lambda:onClick(9))
button0=Button(root,text="0",padx=30,pady=15,command=lambda:onClick(0))
buttonequal=Button(root,text="=",padx=90,pady=15,command=EqualS)
buttonclear=Button(root,text="c",padx=50,pady=15,command=cLear)
buttonadd=Button(root,text="+",padx=20,pady=15,command=adds)
buttonsub=Button(root,text="-",padx=20,pady=15,command=sub)
buttonmul=Button(root,text="*",padx=20,pady=15,command=mul)
buttondiv=Button(root,text="/",padx=20,pady=15,command=div)
button1.grid(column=0,row=1)
button2.grid(column=1,row=1)
button3.grid(column=2,row=1)
button4.grid(column=0,row=2)
button5.grid(column=1,row=2)
button6.grid(column=2,row=2)
button7.grid(column=0,row=3)
button8.grid(column=1,row=3)
button9.grid(column=2,row=3)
button0.grid(column=0,row=4)
buttonsub.grid(column=1,row=4)
buttonclear.grid(column=2,row=4)
buttonadd.grid(column=0,row=5)
buttonmul.grid(column=1,row=5)
buttondiv.grid(column=2,row=5)
buttonequal.grid(row=6)
root.mainloop()