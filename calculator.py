from tkinter import *

def click(event):
    global value
    text = event.widget.cget("text")
    if text == "=":
        if value.get().isdigit():
            evaluate = int(value.get())
        else:
            evaluate = eval(value.get())

        value.set(evaluate)
        screen.update()


    elif text == "C":
        value.set("")
        screen.update()
    else:
        value.set(value.get() + text)
        screen.update()

root = Tk()
root.geometry("644x900")
root.title("calculater")


value = StringVar()
value.set("")

screen = Entry(root, textvariable=value, font="lucida 40 bold")
screen.pack(fill=X, ipadx=8, pady=10, padx=10)

frame1 = Frame(root, bg="grey")
frame1.pack()

# Adding buttons
buttons = [
    '9', '8', '7', '/', '6', '5', '4', '*',
    '3', '2', '1', '-', 'C', '0', '.', '+', '=' , '(' ,')'
]

# Colors for buttons
button_colors = {
    '/': 'lightblue', '*': 'lightblue', '-': 'lightblue', '+': 'lightblue',
    'C': 'lightcoral', '=': 'lightgreen'
}

i = 0
for btn_text in buttons:
    color = button_colors.get(btn_text, 'lightgrey')
    b = Button(frame1, text=btn_text, padx=15, pady=15, font="lucida 35 bold", bg=color, bd=4)
    b.grid(row=i//4, column=i%4, padx=1, pady=2)
    b.bind("<Button-1>", click)
    i += 1

root.mainloop()
