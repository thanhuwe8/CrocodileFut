from tkinter import ttk
import tkinter as tk
import ttkbootstrap as tb
from ttkbootstrap.constants import *

from Views.Archive import *




# root = tk.Tk()
# root.iconbitmap("main.ico")
# root.title("CrocodileFutTrading")
# root.columnconfigure(0, weight=1)
# root.rowconfigure(0, weight=1)
# root.geometry("300x400")

# # a = SnipeView(master=root)
# # a.CreateSnipeView()



# b = ttk.Button(master= root, bootstyle="Primary")
# b['text'] = 'xxx'
# b.grid(row=0,column=0, sticky='nsew')

# c = ttk.Button(master=root, bootstyle="Secondary")
# c['text'] = 'dick'
# c.grid(row=1,column=0, sticky='nsew')

# counter = 0
# def changer():
#     global counter
#     counter += 1
#     if counter % 2 == 0:
#         my_label.config(text="Hello World!")
#     else:
#         my_label.config(text="Goodbye World!")



root = tb.Window(themename='superhero')
root.title("Crocodile Fut Trading")
root.geometry('500x350')

# my_label = tb.Label(text='Hello World!',font=("Helvetica",28), bootstyle="danger, inverse")
# my_label.pack(pady=50)

# my_button = tb.Button(text="Click Me!", bootstyle="success, outline", command=changer)
# my_button.pack(pady=20)

# Check button
# def checker():
#     if var1.get() == 1:
#         my_label.config(text="Checked!")
#     else:
#         my_label.config(text="Unchecked")

# my_label = tb.Label(text='Click the checkbutton below', font=("Helvetica", 20))
# my_label.pack(pady=(40,10))

# var1 = tk.IntVar()
# my_check = tb.Checkbutton(bootstyle="primary", text="Check Me Out!",
#                             variable=var1,
#                             onvalue=1,
#                             offvalue=0,
#                             command=checker)

# my_check.pack(pady=10)



# # Toolbutton
# var2 = tk.IntVar()
# my_check2 = tb.Checkbutton(bootstyle="danger, toolbutton",
#                             text="TOOLBUTTON",
#                             variable=var2,
#                             onvalue=1,
#                             offvalue=0,
#                             command=checker)
# my_check2.pack(pady=10)

# # outline ToolBUTTON
# var3 = tk.IntVar()
# my_check3 = tb.Checkbutton(bootstyle="danger, toolbutton, outline",
#                             text="OUTLINE TOOL BUTTON",
#                             variable=var3,
#                             onvalue=1,
#                             offvalue=0,
#                             command=checker)
# my_check3.pack(pady=10)

# # Round toggle button
# var4 = tk.IntVar()
# my_check4 = tb.Checkbutton(bootstyle="success, round-toggle ",
#                             text="Round Toggle!!!",
#                             variable=var4,
#                             onvalue=1,
#                             offvalue=0,
#                             command=checker)
# my_check4.pack(pady=10)


# # Squared toggle button
# var5 = tk.IntVar()
# my_check5 = tb.Checkbutton(bootstyle="warning, square-toggle ",
#                             text="Squared Toggle!!!",
#                             variable=var5,
#                             onvalue=1,
#                             offvalue=0,
#                             command=checker)
# my_check5.pack(pady=10)


# Style
# my_style = tb.Style()
# my_style.configure('success.Outline.TButton', font=("Helvetica", 18))


# my_button = tb.Button(text="Hello World", 
#                         bootstyle="success", 
#                         style="success.Outline.TButton",
#                         width=20)
# my_button.pack(pady=10)


# combo boxes

# # Create button click function
# def clicker():
#     my_label.config(text=f"You clicked on {my_combo.get()}!")

# # create binding function
# def click_bind(e):
#     my_label.config(text=f"You clicked on {my_combo.get()}!")

# my_label = tb.Label(root, text="Hello World", font=("Helvetica", 18))
# my_label.pack(pady=30)

# # Create Dropdown options
# days = ["Monday","Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# my_combo = tb.Combobox(root, bootstyle="success", values=days)
# my_combo.pack(pady=20)

# # set combo default
# my_combo.current(0)

# # create a button
# my_button = tb.Button(root, text="Click Me!", command=clicker, bootstyle="danger")
# my_button.pack(pady=20)

# # Bind the combobox
# my_combo.bind("<<ComboboxSelected>>", click_bind)

# def speak():
#     my_label.config(text=f'You Typed: {my_entry.get()}')

# my_entry = tb.Entry(root, bootstyle="success", 
#                     font=("Helvetica", 18),
#                     foreground="blue",
#                     width=19)

# my_entry.pack(pady=50)

# # Create Button
# my_button = tb.Button(root, bootstyle="danger outline", 
#                         text="Click Me!", 
#                         command=speak)
# my_button.pack(pady=20)

# my_label = tb.Label(root, text="Hello World!")
# my_label.pack(pady=20)

# my_gauge = tb.Floodgauge(root, bootstyle="success", font=("Helvetica",18),
#                         #  mask=f"Pos: {}")


# root.mainloop()

