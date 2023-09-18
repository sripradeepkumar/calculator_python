from tkinter import *
import math as m

window = Tk()

window.minsize(650, 340)
window.maxsize(340, 720)

window.title("SCIENTIFIC CALCULATOR")

sri = StringVar()
sri = Entry(window, width=31, textvariable=sri, relief=SUNKEN, font="Roboto 20")
sri.grid(row=0, column=0, columnspan=10, padx=11, pady=12)

def sciCal(event):
    key = event.widget
    text = key['text']
    val = sri.get()
    sri.delete(0, END)
    if text == "sin":
        sri.insert(0, m.sin(float(val)))
    elif text == "cos":
        sri.insert(0, m.cos(float(val)))
    elif text == "tan":
        sri.insert(0, m.tan(float(val)))
    elif text == "log":
        if (float(val) <= 0.00):
            sri.insert(0, "Not Possible")
        else:
            sri.insert(0, m.log10(float(val)))
    elif text == "ln":
        if (float(val) <= 0.00):
            sri.insert(0, "Not Possible")
        else:
            sri.insert(0, m.log(float(val)))
    elif text == "√":
        sri.insert(0, m.sqrt(float(val)))
    elif text == "!":
        sri.insert(0, m.factorial(int(val)))
    elif text == "rad":
        sri.insert(0, m.radians(float(val)))
    elif text == "deg":
        sri.insert(0, m.degrees(float(val)))
    elif text == "1/x":
        if (val == "0"):
            sri.insert(0, "ꝏ")
        else:
            sri.insert(0, 1 / float(val))
    elif text == "π":
        if val == "":
            ans = str(m.pi)
            sri.insert(0, ans)
        else:
            ans = str(float(val) * (m.pi))
            sri.insert(0, ans)

    elif text == "e":
        if val == "":
            sri.insert(0, str(m.e))
        else:
            sri.insert(0, str(float(val) * (m.e)))


def click(event):
    key = event.widget
    text = key['text']
    oldValue = sri.get()
    sri.delete(0, END)
    newValue = oldValue + text
    sri.insert(0, newValue)


def clr(event):
    sri.delete(0, END)


def backspace(event):
    entered = sri.get()
    length = len(entered) - 1
    sri.delete(length, END)


def calculate(event):
    answer = sri.get()
    if "^" in answer:
        answer = answer.replace("^", "**")
    answer = eval(answer)
    sri.delete(0, END)
    sri.insert(0, answer)


class Calculator:
    def __init__(self, txt, r, c, funcName, color="white"):
        self.var = Button(window, text=txt, padx=3, pady=5, fg="blue", bg=color, width=10, font="Roboto")
        self.var.bind("<Button-1>", funcName)
        self.var.grid(row=r, column=c)


btn0 = Calculator("sin", 1, 0, sciCal, "grey")

btn1 = Calculator("cos", 1, 1, sciCal, "grey")

btn2 = Calculator("tan", 1, 2, sciCal, "grey")

btn3 = Calculator("log", 1, 3, sciCal)

btn4 = Calculator("ln", 1, 4, sciCal)

btn5 = Calculator("(", 2, 0, click)

btn6 = Calculator(")", 2, 1, click)

btn7 = Calculator("^", 2, 2, click)

btn8 = Calculator("π", 2, 3, sciCal)

btn9 = Calculator("!", 2, 4, sciCal)

btn10 = Calculator("π", 3, 0, sciCal, "blue")

btn11 = Calculator("1/x", 3, 1, sciCal)

btn12 = Calculator("deg", 3, 2, sciCal)

btn13 = Calculator("rad", 3, 3, sciCal)

btn14 = Calculator("e", 3, 4, sciCal, "blue")

btn15 = Calculator("/", 4, 0, click, "#DBA800")

btn16 = Calculator("*", 4, 1, click, "#DBA800")

btn17 = Calculator("-", 4, 2, click, "#DBA800")

btn18 = Calculator("+", 4, 3, click, "#DBA800")

btn19 = Calculator("%", 4, 4, click, "#DBA800")

btn20 = Calculator("9", 5, 0, click)

btn21 = Calculator("8", 5, 1, click)

btn22 = Calculator("7", 5, 2, click)

btn23 = Calculator("6", 5, 3, click)

btn24 = Calculator("5", 5, 4, click)

btn25 = Calculator("4", 6, 0, click)

btn26 = Calculator("3", 6, 1, click)

btn27 = Calculator("2", 6, 2, click)

btn28 = Calculator("1", 6, 3, click)

btn29 = Calculator("0", 6, 4, click)

btn30 = Calculator("C", 7, 0, clr, "red")

btn31 = Calculator("⌦", 7, 1, backspace, "red")

btn32 = Calculator("00", 7, 2, click)

btn33 = Calculator(".", 7, 3, click)

btn34 = Calculator("=", 7, 4, calculate)

window.mainloop()
