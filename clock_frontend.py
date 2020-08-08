

import sys
from tkinter import *
import time 

root = Tk()

# bottomFrame = Frame(root)
# bottomFrame.pack(side=BOTTOM, expand = "yes")


#  Clock
def times():
    current_time = time.strftime("%H:%M:%S")
    clock.config(text=current_time)
    clock.after(200, times)


def button_save():
    print("to żyje!!!")
#     this function is for testing


# Upper text
top_table = Label(root, text="Czas spędzony na programowaniu", font="times 20 bold")
top_table.grid(row=0, column=2)

# dimensions of the window
root.geometry("600x250")
clock = Label(root, font=("times", 40, "bold"), bg="white")
clock.grid(row=2, column=2, pady=25, padx=100)
times()


# lower text
bottom_table = Label(root, text="całkowity czas spędzony na programowaniu   ", font="times 15 bold")
bottom_table.grid(row=3, column=2)


# Time summary
root.geometry("450x400")
clock = Label(root, font=("times", 40, "bold"), bg="white")
clock.grid(row=4, column=2, pady=25, padx=100)
times()


# exit and the buttons
button2 = Button(root, width=35, height=1, text="Exit", fg="red", command=root.destroy)
button2.grid(row=5, column=2)










root.mainloop()
