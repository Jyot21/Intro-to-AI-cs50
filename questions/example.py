# -*- coding: utf-8 -*-
"""
Created on Mon May 25 18:55:17 2020

@author: jyotm
"""

from tkinter import *
from Calculator import *

# window=Tk()
# window.title("Scientific calculator")
# window.configure(background="powder blue")
# window.resizable(width=False, height=False)
# window.geometry('854x608+0+0')

# calc=Frame(window)
# calc.grid()


# #Output Screen Of our Calculator
# txtDisplay=Entry(calc,font=('Times New Roman',20,'bold'),bg="powder blue",bd=30,width=28,justify=RIGHT)
# txtDisplay.grid(row=0,column=0,columnspan=6,pady=1)
# txtDisplay.insert(0,"0.0")

#Creating Object of Calculator class

obj=Calc()

#Creating Buttons


#Simple Buttons of (0-9)
numbers="789456123"
i=0
buttons=[]
for j in range(2,5):
    for k in range(3):
        buttons.append(Button(calc,width=5,height=2,font=('arial',20,'bold'),bd=4,text=numbers[i]))
        buttons[i].grid(row=j,column=k,pady=5)
        buttons[i]["command"]=lambda x=numbers[i]:obj.number(x)
        i+=1
       
#Operation Buttons

Clear=Button(calc,text=chr(67),width=6,height=2,
             font=('arial',20,'bold'),bd=4,bg="blue",
             command=obj.clear_entry).grid(row=1,column=0,pady=5)

Allclear=Button(calc,text=chr(67)+chr(69),width=6,height=2,
                font=('arial',20,'bold'),bd=4,bg="blue",
                command=obj.all_clear_entry).grid(row=1,column=1,pady=5)

SquareRoot=Button(calc,text='√',width=6,height=2,
                  font=('arial',20,'bold'),bd=4,bg="blue",
                  command=obj.square).grid(row=1,column=2,pady=5)

Add=Button(calc,text="+",width=6,height=2,
           font=('arial',20,'bold'),bd=4,bg="blue",
           command=lambda:obj.operation("add")).grid(row=1,column=3,pady=5)

Sub=Button(calc,text="-",width=6,height=2,
           font=('arial',20,'bold'),bd=4,bg="blue",
           command=lambda:obj.operation("sub")).grid(row=2,column=3,pady=5)

Mul=Button(calc,text="*",width=6,height=2,
           font=('arial',20,'bold'),bd=4,bg="blue",
           command=lambda:obj.operation("multi")).grid(row=3,column=3,pady=5)

Div=Button(calc,text=chr(247),width=6,height=2,
           font=('arial',20,'bold'),bd=4,bg="blue",
           command=lambda:obj.operation("divide")).grid(row=4,column=3,pady=5)

Zero=Button(calc,text="0",width=6,height=2,
            font=('arial',20,'bold'),bd=4,bg="blue",
            command=lambda:obj.number(0)).grid(row=5,column=0,pady=5)

Dot=Button(calc,text=".",width=6,height=2,
           font=('arial',20,'bold'),bd=4,bg="blue",
           command=lambda:obj.number(".")).grid(row=5,column=1,pady=5)

PlusMinus=Button(calc,text=chr(177),width=6,height=2,
                font=('arial',20,'bold'),bd=4,bg="blue",
                command=obj.pm).grid(row=5,column=2,pady=5)

Equals=Button(calc,text="=",width=6,height=2,
              font=('arial',20,'bold'),bd=4,bg="blue",
              command=obj.sumoftotal).grid(row=5,column=3,pady=5)

#Scientific Calculator

Pi=Button(calc,text="π",width=6,height=2,
            font=('arial',20,'bold'),bd=4,bg="blue",
            command=obj.pi).grid(row=4,column=4,pady=5)

Sin=Button(calc,text="sin",width=6,height=2,
            font=('arial',20,'bold'),bd=4,bg="blue",
            command=obj.sin).grid(row=2,column=4,pady=5)


Cos=Button(calc,text="cos",width=6,height=2,
           font=('arial',20,'bold'),bd=4,bg="blue",
           command=obj.cos).grid(row=2,column=5,pady=5)

Tan=Button(calc,text="tan",width=6,height=2,
              font=('arial',20,'bold'),bd=4,bg="blue",
              command=obj.tan).grid(row=2,column=6,pady=5)

Sin_inv=Button(calc,text="sin^-1",width=6,height=2,
                 font=('arial',20,'bold'),bd=4,bg="blue",
                 command=obj.asin).grid(row=3,column=4,pady=5)


Cos_inv=Button(calc,text="cos^-1",width=6,height=2,
                 font=('arial',20,'bold'),bd=4,bg="blue",
                 command=obj.acos).grid(row=3,column=5,pady=5)


Tan_inv=Button(calc,text="tan^-1",width=6,height=2,
                 font=('arial',20,'bold'),bd=4,bg="blue",
                 command=obj.atan).grid(row=3,column=6,pady=5)




Two_pi=Button(calc,text="2π",width=6,height=2,
              font=('arial',20,'bold'),bd=4,bg="blue",
              command=obj.tau).grid(row=4,column=5,pady=5)



Mod=Button(calc,text="mod",width=6,height=2,
            font=('arial',20,'bold'),bd=4,bg="blue",
            command=lambda:obj.operation("mod")).grid(row=4,column=4,pady=5)



Exp=Button(calc,text="e^x",width=6,height=2,
            font=('arial',20,'bold'),bd=4,bg="blue",
            command=obj.ex).grid(row=4,column=5,pady=5)



Power=Button(calc,text="x^y",width=6,height=2,
            font=('arial',20,'bold'),bd=4,bg="blue",
            command=lambda:obj.operation("power")).grid(row=4,column=6,pady=5)




E=Button(calc,text="e",width=6,height=2,
         font=('arial',20,'bold'),bd=4,bg="blue",
         command=obj.e).grid(row=1,column=4,pady=5)



log10=Button(calc,text="log10",width=6,height=2,
             font=('arial',20,'bold'),bd=4,bg="blue",
             command=obj.log10).grid(row=1,column=6,pady=5)

ln=Button(calc,text="ln",width=6,height=2,
          font=('arial',20,'bold'),bd=4,bg="blue",
          command=obj.ln).grid(row=1,column=5,pady=5)

Fact=Button(calc,text="x!",width=6,height=2,
          font=('arial',20,'bold'),bd=4,bg="blue",
          command=obj.factprint).grid(row=5,column=4,pady=5)




window.mainloop()