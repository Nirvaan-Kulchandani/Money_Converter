from tkinter import *
from tkinter import messagebox
# USD - United States Dollar.
# INR - Indian Rupee.
# EUR - Euro.
# GBP - British Pound Sterling.
# CAD - Canadian Dollar.
# JPY - Japanese Yen.
root = Tk()

def convert_amount():
    if amount_get.get() == "":
        messagebox.showerror("Incomplete Data", "Please enter the amount to convert.")
        return
    
    if _from.get() == "" or _to.get() == "":
        messagebox.showerror("Incomplete Data", "Please select both currencies to convert.")
        return
    
    amount = float(amount_get.get())
        
    from_currency = _from.get()
    to_currency = _to.get()
    if from_currency == to_currency:
        result = amount
    elif from_currency == "INR":
        if to_currency == "USD":
            result = amount * 0.012

        elif to_currency =="EUR":
            result = amount * 0.010

        elif to_currency == "GBP":
            result = amount * 0.0087

        elif to_currency == "CAD":
            result = amount * 0.016

        elif to_currency == "JPY":
            result = amount * 1.68

        else:
            result = "Invalid Currency"

    elif from_currency == "USD":
        if to_currency == "INR":
            result = amount * 85.06

        elif to_currency == "EUR":
            result = amount * 0.88

        elif to_currency == "GBP":
            result = amount * 0.74

        elif to_currency == "CAD":
            result = amount * 1.37

        elif to_currency == "JPY":
            result = amount * 142.95

        else:
            result = "Invalid Currency"

    elif from_currency == "EUR":
        if to_currency == "INR":
            result = amount * 96.78

        elif to_currency == "USD":
            result = amount * 1.14

        elif to_currency == "GBP":
            result = amount * 0.84

        elif to_currency == "CAD":
            result = amount * 1.56

        elif to_currency == "JPY":
            result = amount * 162.61

        else:
            result = "Invalid Currency"

    elif from_currency == "GBP":
        if to_currency == "INR":
            result = amount * 115.33

        elif to_currency == "EUR":
            result = amount * 1.19

        elif to_currency == "USD":
            result = amount * 1.36

        elif to_currency == "CAD":
            result = amount * 1.86

        elif to_currency == "JPY":
            result = amount * 193.72

        else:
            result = "Invalid Currency"
    
    elif from_currency == "CAD":
        if to_currency == "INR":
            result = amount * 61.98

        elif to_currency == "EUR":
            result = amount * 0.64

        elif to_currency == "GBP":
            result = amount * 0.54

        elif to_currency == "USD":
            result = amount * 0.73

        elif to_currency == "JPY":
            result = amount * 104.14

        else:
            result = "Invalid Currency"

    elif from_currency == "JPY":
        if to_currency == "INR":
            result = amount * 0.60

        elif to_currency == "EUR":
            result = amount * 0.0061

        elif to_currency == "GBP":
            result = amount * 0.0052

        elif to_currency == "CAD":
            result = amount * 0.0096

        elif to_currency == "USD":
            result = amount * 0.0070

        else:
            result = "Invalid Currency"
        
    money_label.config(text=f"= {result}{to_currency}")


currencies= ["INR", "USD", "EUR", "JPY", "CAD", "GBP"]
_from = StringVar()
_from.set(currencies[0])
_to = StringVar()
_to.set(currencies[0])

l1 = Label(root, text="Enter money and type:", justify="center").grid(row=0, column=0)
amount_get = Entry(root, width=6, justify=CENTER)
amount_get.grid(row=0, column=1)
convert_from = OptionMenu(root, _from, *currencies)
convert_from.grid(row=0, column=2)

l2 = Label(root, text="Convert to:").grid(row=1, column=0)
convert_to = OptionMenu(root, _to, *currencies)
convert_to.grid(row=1, column=2)

submit_btn = Button(root,text="Convert", command=convert_amount)
submit_btn.grid(row=2, column=1)
money_label = Label(root, text=" ", bg="yellow", font=("Comic Sans MS", 15), fg="indigo")
money_label.grid(row=3, column=1)
root.mainloop()