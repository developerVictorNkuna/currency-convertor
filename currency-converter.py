from tkinter import ttk
import requests
from tkinter import *
from tkinter import  messagebox
root=Tk()
root.title("Currency convertor")
root.configure(background="deep sky blue")
root.geometry("1359x750+0+0")

root.resizable()
# Create welcome to Real Time Currency Convertor label
# headlabel = Label(root, text='Currency Convertor Application',
#                       fg="black", bg="deep sky blue",font=("Arial",25,"bold"))
# label1 = Label(root, text="Amount :",
#                    fg='black', bg= "deep sky blue",font=("Arial",25,"bold"),anchor='nw', justify='left')
# label2 = Label(root, text="From Currency:",
#                fg='black', bg='deep sky blue', font=("Arial", 25, "bold"))
# Create a "To Currency: " label
# label3 = Label(root, text="To Currency :",
#                    bg="deep sky blue",fg='black',font=("Arial",25,"bold"))

# Create a "Converted Amount :" label
# label4 = Label(root, text="Converted Amount ",fg='black', bg="deep sky blue",font=("Arial",25,"bold"),anchor='nw', justify='left')
# def clear_all():
#     Amount1_field.delete(0, END)
#     Amount2_field.delete(0, END)

def convert():
    T=CurrencyTo.get()
    F=Currencyfrom.get()
    list1 = thisdictcurrency
    for x1 in list1:
        x=list1[T]
        y=list1[F]
    mylabel1.config(text=str(y))
    mylabel2.config(text=str( x))




def clear_all():
    Amount1_field.delete(0, END)
    Amount2_field.delete(0, END)
def callback():
    exit_button["text"]="You pressed Enter"

def exit():
    if messagebox.askyesno(title="Exit",message="Are you certain you want to exit the currency converter system?")==True:
        root.destroy()
    else:
        root.bind("<Return>",callback)

# Where USD is the base currency you want to use
url = 'https://prime.exchangerate-api.com/v5/d15f5d23ca3cd1c7094c5e89/latest/USD'
# Making our request
response = requests.get(url)
data = response.json()
# Your JSON object
thisdictcurrency=(data['conversion_rates'])
print(thisdictcurrency)
#print (data['conversion_rates']["ZAR"])
my_dict=list(thisdictcurrency.keys())
n= StringVar()

Currencyfrom=ttk.Combobox(root, width=27, textvariable=n)
Currencyfrom['values'] = my_dict
Currencyfrom.set(my_dict[0])
Currencyfrom.grid(column=1, row=5)
k= StringVar()
CurrencyTo=ttk.Combobox(root, width=27, textvariable=k)
CurrencyTo['values'] = my_dict

CurrencyTo.grid(column=100, row=5)

mylabel1 = Label(root, font=40, bd=10, anchor='nw', justify='left')
mylabel1.grid(column=10, row=10)
mylabel2 = Label(root, font=40, bd=10, anchor='nw', justify='left')
mylabel2.grid(column=100, row=10)

myclearButton = Button(root, text="Calculate",  fg='gray', bg="deep sky blue",font=("Arial",25,"bold"), command=convert)
myclearButton.grid(column=90, row=400)
Amount1_field = Entry(root)
Amount2_field = Entry(root)


# headlabel.grid(column=0, row=0, sticky=W)
# label1.grid(column=93, row=400, sticky=W)
# label2.grid(column=94,row=400, sticky=W)
# label3.grid(column=95, row=400, sticky=W)
# label4.grid(column=96, row=400, sticky=W)

Amount1_field.grid(row=5,column=2,ipadx="25")
Amount1_field.grid(row=5,column=3,ipadx="25")

exit_button = Button(root,text="Exit",fg='gray', bg="deep sky blue",font=("Arial",25,"bold"), command=exit)
exit_button.grid(column=91,row=400)


clear_button = Button(root,text="Clear",fg='gray', bg="deep sky blue",font=("Arial",25,"bold"), command=clear_all)
clear_button.grid(row=400,column=97)
root.mainloop()