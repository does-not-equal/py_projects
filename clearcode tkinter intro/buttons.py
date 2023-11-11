import tkinter as tk
from tkinter import ttk
from sys import exit

#              #
# main content #
#              #


# window section #

window = tk.Tk()
window.title('Buttons')
window.geometry('600x480')

# normal button #

button_var = tk.StringVar(value='Quit Program')

button = ttk.Button(

    window,
    text='Exit',
    command=exit,
    textvariable=button_var

                   )
button.pack()

# check button #

checkbutton_var = tk.IntVar(value=100)

check = ttk.Checkbutton(

    window,
    text='Simple Checkbox',
    command=lambda: print(checkbutton_var.get()),
    variable=checkbutton_var,
    onvalue=100,
    offvalue=50

                       )
check.pack()


# radio button #

radio_var = tk.StringVar()

radiobutton_one = ttk.Radiobutton(

    window,
    text='Simple Radio Button One',
    value='radio 1',
    variable=radio_var,
    command=lambda: print(radio_var.get())

                                 )

radiobutton_two = ttk.Radiobutton(

    window,
    text='Simple Radio Button Two',
    value='2',
    variable=radio_var
                                 )
radiobutton_one.pack()
radiobutton_two.pack()


#                  #
# exercise section #
#                  #

# definitions #

def radio_func():
    print(ex_cb_var.get())
    ex_cb_var.set(False)


# exercise radio button A #

ex_var = tk.StringVar()
ex_cb_var = tk.BooleanVar()

ex_rb_A = ttk.Radiobutton(

    window,
    text='Exercise Radiobutton A',
    value='A',
    variable=ex_var,
    command=radio_func,

                         )


# exercise radio button B #

ex_rb_B = ttk.Radiobutton(

    window,
    text='Exercise Radiobutton B',
    value='B',
    variable=ex_var,
    command=radio_func,

                         )
ex_rb_A.pack()
ex_rb_B.pack()


# exercise checkbutton #

ex_cb = ttk.Checkbutton(

    window,
    text='Exercise Checkbutton',
    variable=ex_cb_var,
    command=lambda: print(ex_var.get())

                       )
ex_cb.pack()


#             #
# run section #
#             #

window.mainloop()

#                #
# end of content #
#                #
