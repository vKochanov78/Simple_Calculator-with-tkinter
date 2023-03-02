import tkinter as tk
import tkinter.messagebox
from tkinter.constants import SUNKEN

window = tk.Tk()
window.title('Calculator-Simple_version')
window.resizable(False, False)
frame = tk.Frame(master=window, bg='DarkOliveGreen4', padx=10)
frame.pack()
entry = tk.Entry(master=frame, relief=SUNKEN, borderwidth=3, width=30)
entry.grid(row=0, column=0, columnspan=3, ipady=2, pady=2)


def my_click(number):
    entry.insert(tk.END, number)


def equal():
    try:
        y = str(eval(entry.get()))
        entry.delete(0, tk.END)
        entry.insert(0, y)
    except:
        tkinter.messagebox.showinfo("error", "syntax error")


def clear():
    entry.delete(0, tk.END)


#  Number - 1
button_1 = tk.Button(master=frame, text=1, padx=15, pady=5, width=3, command=lambda: my_click(1))
button_1.grid(row=4, column=0, pady=2)

#  Number - 2
button_2 = tk.Button(master=frame, text=2, padx=15, pady=5, width=3, command=lambda: my_click(2))
button_2.grid(row=4, column=1, pady=2)

#  Number - 3
button_3 = tk.Button(master=frame, text=3, padx=15, pady=5, width=3, command=lambda: my_click(3))
button_3.grid(row=4, column=2, pady=2)

#  Number - 4
button_4 = tk.Button(master=frame, text=4, padx=15, pady=5, width=3, command=lambda: my_click(4))
button_4.grid(row=5, column=0, pady=2)

#  Number - 5
button_5 = tk.Button(master=frame, text=5, padx=15, pady=5, width=3, command=lambda: my_click(5))
button_5.grid(row=5, column=1, pady=2)

#  Number - 6
button_6 = tk.Button(master=frame, text=6, padx=15, pady=5, width=3, command=lambda: my_click(6))
button_6.grid(row=5, column=2, pady=2)

#  Number - 7
button_7 = tk.Button(master=frame, text=7, padx=15, pady=5, width=3, command=lambda: my_click(7))
button_7.grid(row=6, column=0, pady=2)

#  Number - 8
button_8 = tk.Button(master=frame, text=8, padx=15, pady=5, width=3, command=lambda: my_click(8))
button_8.grid(row=6, column=1, pady=2)

#  Number - 9
button_9 = tk.Button(master=frame, text=9, padx=15, pady=5, width=3, command=lambda: my_click(9))
button_9.grid(row=6, column=2, pady=2)

#  Number - 0
button_0 = tk.Button(master=frame, text=0, padx=15, pady=5, width=3, command=lambda: my_click(0))
button_0.grid(row=7, column=1, pady=2)

#  Button - Add
button_add = tk.Button(master=frame, text="+", padx=15, pady=5, width=3, command=lambda: my_click("+"))
button_add.grid(row=1, column=0, pady=2)

#  Button - Subtract
button_subtract = tk.Button(master=frame, text="-", padx=15, pady=5, width=3, command=lambda: my_click("-"))
button_subtract.grid(row=1, column=2, pady=2)

#  Button - Multiply
button_multiply = tk.Button(master=frame, text="*", padx=15, pady=5, width=3, command=lambda: my_click("*"))
button_multiply.grid(row=2, column=0, pady=2)

#  Button - Divide
button_divide = tk.Button(master=frame, text="/", padx=15, pady=5, width=3, command=lambda: my_click("/"))
button_divide.grid(row=2, column=2, pady=2)

#  Button - Clear
button_clear = tk.Button(master=frame, text="CE", padx=15, pady=5, width=3, command=clear)
button_clear.grid(row=1, column=1, pady=2)

#  Button - Equal
button_equal = tk.Button(master=frame, text="=", padx=15, pady=5, width=21, command=equal)
button_equal.grid(row=3, column=0, columnspan=3, pady=2)

window.mainloop()