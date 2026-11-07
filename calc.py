from tkinter import  *
import tkinter.messagebox
#=================================setting=====================
root = Tk()
root.geometry('400x200')
root.title('calculator')
root.resizable(width=False,height=False)
color = 'gray'
root.configure(bg=color)
#========================================== variables ================
num1 = StringVar()
num2 = StringVar()
res_value = StringVar()
#==============================frames==========================
top_first = Frame(root, width=400, height=50, bg=color)
top_first.pack(side=TOP)
top_secound = Frame(root, width=400, height=50, bg=color)
top_secound.pack(side=TOP)
top_third = Frame(root, width=400, height=50, bg=color)
top_third.pack(side=TOP)
top_forth = Frame(root, width=400, height=50, bg=color)
top_forth.pack(side=TOP)
#==========================functions==============================
def errormsg(ms):
    if ms == 'error':
        tkinter.messagebox.showerror('Error', 'somethin went wrong')
    elif ms == 'division zero error':
        tkinter.messagebox.showerror('Division Error', 'Can not Diviode By 0')
def plus():
    try:
        value = float(num1.get()) + float(num2.get())
        res_value.set(value)
    except:
        errormsg('error')
def minus():
    try:
        value = float(num1.get()) - float(num2.get())
        res_value.set(value)
    except:
        errormsg('error')
def mul():
    try:
        value = float(num1.get()) * float(num2.get())
        res_value.set(value)
    except:
        errormsg('error')
def div():
    if num2.get() == '0':
        errormsg('division zero error')
    elif num2.get() != '0':
     try:
        value = float(num1.get()) / float(num2.get())
        res_value.set(value)
     except:
        errormsg('error')

#========================================Buttons===========================
btn_plus = Button(top_third , text="+", width=8,
                  highlightbackground=color, command=lambda: plus())
btn_plus.pack(side=LEFT, padx=5, pady=5)
btn_minus = Button(top_third, text="-", width=8,
                   highlightbackground=color, command=lambda: minus())
btn_minus.pack(side=LEFT, padx=5, pady=5)
btn_mul = Button(top_third, text="*", width=8,
                 highlightbackground=color, command=lambda: mul())
btn_mul.pack(side=LEFT, padx=5, pady=5)
btn_div = Button(top_third, text="/", width=8,
                 highlightbackground=color, command=lambda: div())
btn_div.pack(side=LEFT, padx=5, pady=5)
#=================================Entries and Labels==============================
label_first_num = Label(top_first, text="input number 1 :", bg=color)
label_first_num.pack(side=LEFT, pady=5, padx=5)
first_num =Entry(top_first, highlightbackground=color , textvariable=num1)
first_num.pack(side=LEFT)

label_secound_num = Label(top_secound, text="input number 2 :", bg=color)
label_secound_num.pack(side=LEFT, pady=5, padx=5)

secound_num =Entry(top_secound, highlightbackground=color, textvariable=num2)
secound_num.pack(side=LEFT)
res = Label(top_forth, text='result:', bg=color)
res.pack(side=LEFT, pady=5, padx= 5)
res_num = Entry(top_forth, highlightbackground=color, textvariable=res_value)
res_num.pack(side=LEFT)
root.mainloop()

