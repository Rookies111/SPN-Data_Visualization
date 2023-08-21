from tkinter import *

num = 0

root = Tk()

label = Label(root, font="Timenewroman 64 bold")
label.pack(fill=BOTH, pady=20)

def main():
    global num
    label.config(text = num)
    num = num + 1
    root.after(1000, main)

main()
mainloop()