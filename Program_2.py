# Author: Michael Beaudet
# Title: Week 11 Program 2
# Date: 4/8/25

import tkinter 
import tkinter.messagebox

def main():
    root = tkinter.Tk()
    root.title("my info")

    label = tkinter.Label(root, text="")
    label.pack()

    show_button = tkinter.Button(root, text="show info", command=info)
    show_button.pack()

    quit_button = tkinter.Button(root, text="quit", command=root.quit)
    quit_button.pack()

    root.mainloop()

    def info():
        tkinter.messagebox.showinfo('Info', 'Michael Beaudet, 123 Code Street')


if __name__ == "__main__":
    main()