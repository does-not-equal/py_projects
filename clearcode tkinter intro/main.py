import tkinter as tk
from tkinter import ttk


def button_func():
    print('The butt was touched!')


def button_two_func():
    print('hello')


# create a window
window = tk.Tk()
window.title('Tkinter Intro')
window.geometry('640x480')

# ttk label
label = ttk.Label(master=window, text='This is a test.')
label.pack()

# tk text
text = tk.Text(master=window)
text.pack()

# ttk entry
entry = ttk.Entry(master=window)
entry.pack()

# exercise 1 label
label_two = ttk.Label(master=window, text='My label.')
label_two.pack()

# ttk button
button = ttk.Button(master=window, text='butt', command=button_func)
button.pack()

# exercise 1 button
button_two = ttk.Button(master=window, text='button', command=button_two_func)
button_two.pack()


# run
window.mainloop()  # updates the gui and checks for events (button clicks, mouse movement, closing the window)

