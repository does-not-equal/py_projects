import tkinter as tk
from tkinter import ttk


def button_func():
    print(string_var.get())
    string_var.set('button pressed')


# window
window = tk.Tk()
window.title('Tkinter Variables')

# tkinter variable
string_var = tk.StringVar()
exer_var = tk.StringVar(value='Start Value')

# widgets
label = ttk.Label(master=window, text='Label', textvariable=string_var)
label.pack()

entry = ttk.Entry(master=window, textvariable=string_var)
entry.pack()

button = ttk.Button(master=window, text='button', command=button_func)
button.pack()

# exercise section
ent1 = ttk.Entry(master=window, textvariable=exer_var)
ent2 = ttk.Entry(master=window, textvariable=exer_var)
lab1 = ttk.Label(master=window, textvariable=exer_var)
ent1.pack()
ent2.pack()
lab1.pack()

# run
window.mainloop()
