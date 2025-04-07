# Author: Michael Beaudet
# Title: Program 1 Week 11
# Date: 4/7/25

import tkinter 

def main():
    root = tkinter.Tk()
    root.title("Favorite Quote")

    label = tkinter.Label(root, text= "I can do all things through Christ which strengtheneth me.")
    label.pack()

    root.mainloop()

if __name__ == "__main__":
    main()