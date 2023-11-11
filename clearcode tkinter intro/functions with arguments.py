import tkinter as tk
from tkinter import ttk

# definitions


def button_func(entry_string):
    print('You pressed the button.')
    print(entry_string.get())


# window section
window = tk.Tk()
window.title('Buttons, Functions and Arguments')

# widgets
# entry
entry_string = tk.StringVar(value='test')
entry = ttk.Entry(window, textvariable=entry_string)
entry.pack()
# button
button = ttk.Button(window, text='button', command=lambda: button_func(entry_string))
button.pack()

# run section
window.mainloop()

