#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from tkinter import *
import math

window=Tk()
window.title("Scientific calculator")
window.configure(background="powder blue")
window.resizable(width=False, height=False)
window.geometry('854x608+0+0')

calc=Frame(window)
calc.grid()


#Output Screen Of our Calculator
txtDisplay=Entry(calc,font=('Times New Roman',20,'bold'),bg="powder blue",bd=30,width=28,justify=RIGHT)
txtDisplay.grid(row=0,column=0,columnspan=6,pady=1)
txtDisplay.insert(0,"0.0")



class Calc:
    
    def __init__(self):
        self.total=0
        self.current=""
        self.input_value=True
        self.check_sum=False
        self.op=""
        self.result=False
        
    def number(self,num):
        self.result=False
        fno=txtDisplay.get()
        sno=str(num)
        if self.input_value:
            self.current=sno
            self.input_value=False
        else:
            if sno==".":
                if sno in fno:
                    return
            self.current=fno+sno
        self.display(self.current)
        
    def sumoftotal(self):
        self.result=True
        self.current=float(self.current)
        if self.check_sum==True:
            self.valid_function()
        else:
            self.total=float(txtDisplay.get())
        
    def display(self,value):
        txtDisplay.delete(0,END)
        txtDisplay.insert(0,value)
        
    def valid_function(self):
        if self.op=="add":
            self.total+=self.current
            self.input_value=True
            self.check_sum=False
            self.display(self.total)
        
        if self.op=="sub":
            self.total-=self.current
            self.input_value=True
            self.check_sum=False
            self.display(self.total)
            
        if self.op=="multi":
            self.total*=self.current
            self.input_value=True
            self.check_sum=False
            self.display(self.total)
            
        if self.op=="divide":
            if self.current==0:
                self.input_value=True
                self.check_sum=False
                self.display("Math Error")
            else:
                self.total/=self.current
                self.input_value=True
                self.check_sum=False
                self.display(self.total)
                
                
        if self.op=="mod":
            self.total%=self.current
            self.input_value=True
            self.check_sum=False
            self.display(self.total)
            
        if self.op=="x^y":
            self.total**=self.current
            self.input_value=True
            self.check_sum=False
            self.display(self.total)
            
        
        
        
    def operation(self,op):
        self.current=float(self.current)
        if self.check_sum:
            self.valid_function()
        elif not self.result:
            self.total=self.current
            self.input_value=True
        self.check_sum=True
        self.op=op
        self.result=False
        
    def clear_entry(self):
        self.result=False
        self.current="0"
        self.display(0)
        self.input_value=True
        
    def all_clear_entry(self):
        self.clear_entry()
        self.total=0
        
    def pi(self):
        self.result=False
        self.current=math.pi
        self.display(self.current)
        
    def tau(self):
        self.result=False
        self.current=math.tau
        self.display(self.current)
        
    def e(self):
        self.result=False
        self.current=math.e
        self.display(self.current)
        
    def cos(self):
        self.result=False
        self.current=math.cos(float(txtDisplay.get()))
        self.display(self.current)
    
    def sin(self):
        self.result=False
        self.current=math.sin(math.radians(float(txtDisplay.get())))
        self.display(self.current)
        
    def tan(self):
        self.result=False
        try:
            if(float(txtDisplay.get())%90==0):
                self.display("Math Error")
            else:
                self.current=math.tan(math.radians(float(txtDisplay.get())))
                self.display(self.current)
        except:
            print("Value Error")
     

    def square(self):
        self.result=False
        try:
            if(float(txtDisplay.get())<0.0):
                self.display("Math Error")
            else:
                self.current=math.sqrt(float(txtDisplay.get()))
                self.display(self.current)
        except:
            print("Value Error")
        
    def pm(self):
        self.result=False
        self.current=-(float(txtDisplay.get()))
        self.display(self.current)
        
    def log10(self):
        self.result=False
        if float(txtDisplay.get())!=0:
            self.current=math.log10(float(txtDisplay.get()))
            self.display(self.current)
        else:
            self.display("Math Error")
        
    def ln(self):
        self.result=False
        if float(txtDisplay.get())!=0:
            self.current=math.log(float(txtDisplay.get()))
            self.display(self.current)
        else:
            self.display("Math Error")
        
    def ex(self):
        self.result=False
        self.current=math.exp(float(txtDisplay.get()))
        self.display(self.current)
        
    def power(self):
        self.total=(self.total**self.current)
        
           
    def asin(self):
        
        self.result=False
        if float(txtDisplay.get())<-1 or  float(txtDisplay.get())>1 :
            self.display("Domain Error")
        else:
            self.current=math.asin(float(txtDisplay.get()))
            self.display(self.current)
        
    def acos(self):
        self.result=False
        if float(txtDisplay.get())<-1 or  float(txtDisplay.get())>1 :
            self.display("Domain Error")
        else:
            self.current=math.acos(float(txtDisplay.get()))
            self.display(self.current)
        
    def atan(self):
        self.result=False
        if float(txtDisplay.get())<-1 or  float(txtDisplay.get())>1 :
            self.display("Domain Error")
        else:
            self.current=math.atan(float(txtDisplay.get()))
            self.display(self.current)

    def fact(self,n):
        if n==1 or n==0:
            return 1
        else:
            return n*self.fact(n-1)
        
    def factprint(self):
        self.result=False
        if txtDisplay.get().isnumeric():
            temp=int(txtDisplay.get())
            self.current=str(self.fact(temp))
            self.display(self.current)

        else:
            self.display("Math Errror")
            
            
                                 
           
            
           
           
            
        

    
        
        
