


import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as messagebox
import ttkbootstrap as ttk
import customtkinter as ctk
from ttkbootstrap.toast import ToastNotification
import random

# Global variable to keep track of the number of moves
move_count = 0

def move_cancel_button():
    global move_count
    move_count += 1
    if move_count >= 5:
        messagebox.showinfo("):", "میخوای از نمره دادن فرار کنی؟")
        move_count = 0  # Reset move_count to 0
    else:
        new_x = random.randint(15, 200)
        new_y = random.randint(15, 200)
        cancel_button.place(x=new_x, y=new_y)

# Function to display a second message box when the user presses "OK" and exit the app
def show_second_message_and_exit():
    messagebox.showinfo(":)", "آفرین آقای فیروزی")
    root.quit()  # Close the main window

# Create the main window
root =  ttk.Window(themename= 'superhero')
root.title("Mister Programmer")

# Create and place a header label
header_label = tk.Label(root, text="اگه نمره ندی مرد نیستی", font=("Lalezar", 22))
header_label.pack()

# Create and place OK button with green background
ok_button = tk.Button(root, text="باشه نمره میدم", bg="green", fg="#fff", command=show_second_message_and_exit)
ok_button.pack()

# Create and place Cancel button with red background
cancel_button = tk.Button(root, text="نمره نمیدم", bg="red", fg="#fff")
cancel_button.pack()

# Bind the move_cancel_button function to the hover event
cancel_button.bind("<Enter>", lambda e: move_cancel_button())






toast = ToastNotification(
    title='Hello, Professor Firuzi ',
    message= 'لطف کن استاد این نمره ما بده تا بریم ... دما گرم',
    duration= 4000,
    bootstyle= 'warning' , 
    position= (50 , 100 , 'ne') , 
    alert= True

)





ttk.Button(root, text='Show Toast', command=toast.show_toast).pack(pady=10)






# Run the Tkinter main loop
root.mainloop()





















