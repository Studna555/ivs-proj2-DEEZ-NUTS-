from mathpack import Mathpack


from tkinter import *
calc = Mathpack()
number=0

def clear():
    txtDisplay.delete(0,END)
    return
def add():
    txtDisplay.insert(number,"+")
    return
def set_operation(oper):
    operation = oper
 
def zero():
    txtDisplay.insert(number,"0")
    return
def one():
    txtDisplay.insert(number,"1")
    return
def two():
    txtDisplay.insert(number,"2")
    return
def three():
    txtDisplay.insert(number,"3")
    return
def four():
    txtDisplay.insert(number,"4")
    return
def five():
    txtDisplay.insert(number,"5")
    return
def six():
    txtDisplay.insert(number,"6")
    return
def seven():
    txtDisplay.insert(number,"7")
    return
def eight():
    txtDisplay.insert(number,"8")
    return
def nine():
    txtDisplay.insert(number,"9")
    return

def eval(numbers, operation):
    if operation == "+":
        calc.add(numbers)
    elif operation == "-":
        calc.substract(numbers)
    elif operation == "*":
        calc.mult(numbers)
    elif operation == "/":
        calc.div(numbers[0], numbers[1])
    elif operation == "!":
        calc.factorial(number[0])
    elif operation == "**":
        calc.pow(numbers[0], numbers[1])
    elif operation == "%":
        calc.modulo(numbers[0], numbers[1])
    return calc.ans

number = []
numbers = []
operation = ""


root = Tk()
frame = Frame(root)
frame.pack()

root.geometry("235x396")

root.title("Calculator")

num1 = StringVar()

topframe = Frame(root)
topframe.pack(side = TOP)

txtDisplay = Entry(frame,textvariable = num1, bd = 15, width=235, insertwidth = 1, font = 30, justify="right", bg="#CCCCE0")
txtDisplay.pack(side = TOP)

frame0 = Frame(root)
frame0.pack(side = TOP)

button1 = Button(frame0, padx = 22, pady = 22, width=1, bd = 2, text = "+", fg="black", bg = "grey", command= set_operation("+"))
button1.pack(side = LEFT)
button2 = Button(frame0, padx = 22, pady = 22, width=1, bd = 2, text = "-", fg="black", bg = "grey", command= set_operation("-") )
button2.pack(side = LEFT)
button3 = Button(frame0, padx = 22, pady = 22, width=1, bd = 2, text = "*", fg="black", bg = "grey")
button3.pack(side = LEFT)
button4 = Button(frame0, padx = 22, pady = 22, width=1, bd = 2, text = "/", fg="black", bg = "grey")
button4.pack(side = LEFT)

frame1 = Frame(root)
frame1.pack (side = TOP)

button1 = Button(frame1, padx = 22, pady = 22, width=1, bd = 2, text = "7", fg="black", command = number.append(7))
button1.pack(side = LEFT)
button2 = Button(frame1, padx = 22, pady = 22, width=1, bd = 2, text = "8", fg="black", command = number.append(8))
button2.pack(side = LEFT)
button3 = Button(frame1, padx = 22, pady = 22, width=1, bd = 2, text = "9", fg="black", command = number.append(9))
button3.pack(side = LEFT)
button4 = Button(frame1, padx = 22, pady = 22, width=1, bd = 2, text = "mod", fg="black", bg = "grey")
button4.pack(side = LEFT)

frame2 = Frame(root)
frame2.pack (side = TOP)

button1 = Button(frame2, padx = 22, pady = 22, width=1, bd = 2, text = "4", fg="black", command = number.append(4))
button1.pack(side = LEFT)
button2 = Button(frame2, padx = 22, pady = 22, width=1, bd = 2, text = "5", fg="black", command = number.append(5))
button2.pack(side = LEFT)
button3 = Button(frame2, padx = 22, pady = 22, width=1, bd = 2, text = "6", fg="black", command = number.append(6))
button3.pack(side = LEFT)
button4 = Button(frame2, padx = 22, pady = 22, width=1, bd = 2, text = "!", bg = "grey", fg="black")
button4.pack(side = LEFT)

frame3 = Frame(root)
frame3.pack (side = TOP)

button1 = Button(frame3, padx = 22, pady = 22, width=1, bd = 2, text = "1", fg="black", command = number.append(1))
button1.pack(side = LEFT)
button2 = Button(frame3, padx = 22, pady = 22, width=1, bd = 2, text = "2", fg="black", command = number.append(2))
button2.pack(side = LEFT)
button3 = Button(frame3, padx = 22, pady = 22, width=1, bd = 2, text = "3", fg="black", command = number.append(3))
button3.pack(side = LEFT)
button4 = Button(frame3, padx = 22, pady = 22, width=1, bd = 2, text = "^", bg = "grey", fg="black")
button4.pack(side = LEFT)

frame4 = Frame(root)
frame4.pack (side = TOP)

button1 = Button(frame4, padx = 22, pady = 22, width=1, bd = 2, text = "0", fg="black", command = number.append(0))
button1.pack(side = LEFT)
button2 = Button(frame4, padx = 22, pady = 22, width=1, bd = 2, text = ".", fg="black")
button2.pack(side = LEFT)
button3 = Button(frame4, padx = 22, pady = 22, width=1, bd = 2, text = "C", bg = "grey", fg="black", command = clear)
button3.pack(side = LEFT)
button4 = Button(frame4, padx = 22, pady = 22, width=1, bd = 2, text = "=", bg = "grey", fg="black", command = eval(numbers,operation))
button4.pack(side = LEFT)


root.mainloop()
