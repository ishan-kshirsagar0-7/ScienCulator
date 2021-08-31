from tkinter import *
import math
import tkinter.messagebox as tmsg
import time
from idlelib.tooltip import Hovertip

root = Tk()
root.config(bg='black')
width = 705
height = 540
root.geometry(f'{width}x{height}')
root.maxsize(705, 540)
root.minsize(705, 540)
root.title('ScienCulator™')
scvalue = StringVar()
scvalue.set('')
screen = Entry(root, highlightthickness=3, highlightbackground='dark orange', text=scvalue, font='Digital-7 53', takefocus=0)
screen.grid(row=0, column=0, columnspan=7, pady=10, padx=(10, 10), ipadx=8)
screen.config(state=DISABLED)


def restrict(event):
    screen.config(state=DISABLED)


screen.bind('<Button-1>', restrict)


class Calculator:
    def __init__(self):
        self.total = 0
        self.current = ''
        self.input_value = True
        self.check_sum = False
        self.op = ''
        self.result = False

    def blit(self, value):
        screen.delete(0, END)
        screen.insert(0, value)

    def equals_to(self, *event):
        self.result = True
        self.current = float(self.current)
        if self.check_sum:
            self.valid_func()
        else:
            self.total = float(screen.get())

    def valid_func(self):
        if self.op == '+':
            self.total += self.current
        if self.op == '-':
            self.total -= self.current
        if self.op == '*':
            self.total *= self.current
        if self.op == '/':
            try:
                self.total /= self.current
            except ZeroDivisionError:
                tmsg.showerror('ScienCulator™', 'Division by 0 is not defined!')
        if self.op == '%':
            self.total = (self.total*self.current)/100
        if self.op == 'xn':
            self.total = self.total**float(self.current)
        if self.op == 'yrtx':
            self.total = self.total**float(1/int(self.current))
        self.input_value = True
        self.check_sum = False
        self.blit(self.total.__round__(2))
        button_add.config(bg='dark orange')
        button_sub.config(bg='dark orange')
        button_mult.config(bg='dark orange')
        button_div.config(bg='dark orange')
        button_perc.config(bg='grey')
        button_xn.config(bg='grey')
        button_yrtx.config(bg='grey')

    def clear(self, *event):
        self.result = False
        self.current = '0'
        self.blit(0)
        self.input_value = True
        self.total = 0
        button_add.config(bg='dark orange')
        button_sub.config(bg='dark orange')
        button_mult.config(bg='dark orange')
        button_div.config(bg='dark orange')
        button_perc.config(bg='grey')
        button_xn.config(bg='grey')
        button_yrtx.config(bg='grey')
        screen.config(state=DISABLED)

    def cubed(self, *event):
        self.result = False
        self.current = float(screen.get())**3
        self.blit(self.current)

    def squared(self, *event):
        self.result = False
        self.current = float(screen.get())**2
        self.blit(self.current)

    def plus_minus(self, *event):
        self.result = False
        self.current = -float(screen.get())
        self.blit(self.current)

    def factorial(self, *event):
        try:
            if screen.get().endswith('.0'):
                new = screen.get().replace('.0', '')
                self.result = False
                self.current = math.factorial(int(new))
                self.blit(self.current)
            else:
                self.result = False
                self.current = math.factorial(int(screen.get()))
                self.blit(self.current)
        except:
            tmsg.showerror('ScienCulator™', 'Factorials of float-type integers are not defined!')

    def sqrt(self, *event):
        self.result = False
        if '-' in screen.get():
            self.current = -float(screen.get())
            self.current = math.sqrt(self.current)
            self.blit(f'{self.current.__round__(2)} iota')
        else:
            self.current = math.sqrt(float(screen.get()))
            self.blit(self.current)

    def ex(self, *event):
        self.result = False
        self.current = math.e**float(screen.get())
        self.blit(self.current)

    def ln(self, *event):
        try:
            self.result = False
            self.current = math.log(float(screen.get()), math.e)
            self.blit(self.current)
        except:
            tmsg.showerror('ScienCulator™', 'The Logarithm function does not accept negative values or 0 in its domain!')

    def log(self, *event):
        try:
            self.result = False
            self.current = math.log10(float(screen.get()))
            self.blit(self.current)
        except:
            tmsg.showerror('ScienCulator™', 'The Logarithm function does not accept negative values or 0 in its domain!')

    def trigo(self, angle, *event):
        self.result = False
        if angle == 'sin':
            self.current = math.sin(math.radians(float(screen.get())))
            self.blit(self.current.__round__(2))
        if angle == 'cos':
            self.current = math.cos(math.radians(float(screen.get())))
            self.blit(self.current.__round__(2))
        if angle == 'tan':
            if float(screen.get()) % 90 == 0 and float(screen.get()) != 0 and float(screen.get()) % 180 != 0:
                screen.delete(0, END)
                screen.insert(0, 'NOT DEFINED')
            else:
                self.current = math.tan(math.radians(float(screen.get())))
                self.blit(self.current.__round__(2))
        if angle == 'csc':
            if float(screen.get()) == 0 or float(screen.get()) % 180 == 0:
                screen.delete(0, END)
                screen.insert(0, 'NOT DEFINED')
            else:
                self.current = 1/(math.sin(math.radians(float(screen.get()))))
                self.blit(self.current.__round__(2))
        if angle == 'sec':
            if float(screen.get()) % 90 == 0 and float(screen.get()) != 0 and float(screen.get()) % 180 != 0:
                screen.delete(0, END)
                screen.insert(0, 'NOT DEFINED')
            else:
                self.current = 1/(math.cos(math.radians(float(screen.get()))))
                self.blit(self.current.__round__(2))
        if angle == 'cot':
            if float(screen.get()) == 0 or float(screen.get()) % 180 == 0:
                screen.delete(0, END)
                screen.insert(0, 'NOT DEFINED')
            self.current = 1/(math.tan(math.radians(float(screen.get()))))
            self.blit(self.current.__round__(2))

    def operation(self, op):
        self.current = float(self.current)
        if self.check_sum:
            self.valid_func()
        elif not self.result:
            self.total = self.current
            self.input_value = True
        self.check_sum = True
        self.op = op
        self.result = False
        if op == '+':
            button_add.config(bg='red')
            button_sub.config(bg='dark orange')
            button_mult.config(bg='dark orange')
            button_div.config(bg='dark orange')
            button_perc.config(bg='grey')
            button_xn.config(bg='grey')
            button_yrtx.config(bg='grey')
        if op == '-':
            button_sub.config(bg='red')
            button_add.config(bg='dark orange')
            button_mult.config(bg='dark orange')
            button_div.config(bg='dark orange')
            button_perc.config(bg='grey')
            button_xn.config(bg='grey')
            button_yrtx.config(bg='grey')
        if op == '*':
            button_mult.config(bg='red')
            button_sub.config(bg='dark orange')
            button_add.config(bg='dark orange')
            button_div.config(bg='dark orange')
            button_perc.config(bg='grey')
            button_xn.config(bg='grey')
            button_yrtx.config(bg='grey')
        if op == '/':
            button_div.config(bg='red')
            button_sub.config(bg='dark orange')
            button_mult.config(bg='dark orange')
            button_add.config(bg='dark orange')
            button_perc.config(bg='grey')
            button_xn.config(bg='grey')
            button_yrtx.config(bg='grey')
        if op == '%':
            button_perc.config(bg='red')
            button_sub.config(bg='dark orange')
            button_mult.config(bg='dark orange')
            button_add.config(bg='dark orange')
            button_div.config(bg='dark orange')
            button_xn.config(bg='grey')
            button_yrtx.config(bg='grey')
        if op == 'xn':
            button_xn.config(bg='red')
            button_sub.config(bg='dark orange')
            button_mult.config(bg='dark orange')
            button_add.config(bg='dark orange')
            button_div.config(bg='dark orange')
            button_perc.config(bg='grey')
            button_yrtx.config(bg='grey')
        if op == 'yrtx':
            button_yrtx.config(bg='red')
            button_sub.config(bg='dark orange')
            button_mult.config(bg='dark orange')
            button_add.config(bg='dark orange')
            button_div.config(bg='dark orange')
            button_perc.config(bg='grey')
            button_xn.config(bg='grey')

    def number_enter(self, num):
        screen.config(state=NORMAL)
        self.result = False
        first_number = screen.get()
        second_number = str(num)
        if self.input_value:
            self.current = second_number
            self.input_value = False
        else:
            if second_number == '.':
                if second_number in first_number:
                    return
            self.current = first_number + second_number
        self.blit(self.current)


added_value = Calculator()


# Row 1
button_cube = Button(root, bg='grey', fg='black', text='x³', padx=18, pady=9, font='Helvetica 23', activebackground='grey', command=added_value.cubed)
button_cube.grid(row=1, column=0)
button_square = Button(root, bg='grey', fg='black', text='x²', padx=19, pady=9, font='Helvetica 23', activebackground='grey', command=added_value.squared)
button_square.grid(row=1, column=1)
button_xn = Button(root, bg='grey', fg='black', text='xⁿ', padx=24, pady=9, font='Helvetica 23', activebackground='grey', command=lambda: added_value.operation('xn'))
button_xn.grid(row=1, column=2)
button_c = Button(root, bg='grey', fg='black', text='C', padx=16, pady=9, font='Helvetica 23', activebackground='grey', command=added_value.clear)
button_c.grid(row=1, column=3)
button_pm = Button(root, bg='grey', fg='black', text='+/-', padx=16, pady=9, font='Helvetica 23', activebackground='grey', command=added_value.plus_minus)
button_pm.grid(row=1, column=4)
button_perc = Button(root, bg='grey', fg='black', text='%', padx=16, pady=9, font='Helvetica 23', activebackground='grey', command=lambda: added_value.operation('%'))
button_perc.grid(row=1, column=5)
button_div = Button(root, bg='dark orange', fg='black', text='÷', padx=16, pady=9, font='Helvetica 23', activebackground='dark orange', command=lambda: added_value.operation('/'))
button_div.grid(row=1, column=6)

# Row 2
button_fac = Button(root, bg='grey', fg='black', text='x!', padx=18, pady=9, font='Helvetica 23', activebackground='grey', command=added_value.factorial)
button_fac.grid(row=2, column=0, pady=9)
button_sqrt = Button(root, bg='grey', fg='black', text='√', padx=23, pady=9, font='Helvetica 23', activebackground='grey', command=added_value.sqrt)
button_sqrt.grid(row=2, column=1)
button_yrtx = Button(root, bg='grey', fg='black', text='ⁿ√x', padx=16, pady=9, font='Helvetica 23', activebackground='grey', command=lambda: added_value.operation('yrtx'))
button_yrtx.grid(row=2, column=2)
button_7 = Button(root, bg='silver', fg='black', text='7', padx=19, pady=9, font='Helvetica 23', activebackground='dark grey', command=lambda: added_value.number_enter(7))
button_7.grid(row=2, column=3)
button_8 = Button(root, bg='silver', fg='black', text='8', padx=26, pady=9, font='Helvetica 23', activebackground='dark grey', command=lambda: added_value.number_enter(8))
button_8.grid(row=2, column=4)
button_9 = Button(root, bg='silver', fg='black', text='9', padx=21, pady=9, font='Helvetica 23', activebackground='dark grey', command=lambda: added_value.number_enter(9))
button_9.grid(row=2, column=5)
button_mult = Button(root, bg='dark orange', fg='black', text='x', padx=18, pady=9, font='Helvetica 23', activebackground='dark orange', command=lambda: added_value.operation('*'))
button_mult.grid(row=2, column=6)

# Row 3
button_ex = Button(root, bg='grey', fg='black', text='eˣ', padx=16, pady=9, font='Helvetica 23', activebackground='grey', command=added_value.ex)
button_ex.grid(row=3, column=0, pady=1)
button_ln = Button(root, bg='grey', fg='black', text='ln', padx=20, pady=9, font='Helvetica 23', activebackground='grey', command=added_value.ln)
button_ln.grid(row=3, column=1)
button_l10 = Button(root, bg='grey', fg='black', text='log', padx=16, pady=9, font='Helvetica 23', activebackground='grey', command=added_value.log)
button_l10.grid(row=3, column=2)
button_4 = Button(root, bg='silver', fg='black', text='4', padx=19, pady=9, font='Helvetica 23', activebackground='dark grey', command=lambda: added_value.number_enter(4))
button_4.grid(row=3, column=3)
button_5 = Button(root, bg='silver', fg='black', text='5', padx=26, pady=9, font='Helvetica 23', activebackground='dark grey', command=lambda: added_value.number_enter(5))
button_5.grid(row=3, column=4)
button_6 = Button(root, bg='silver', fg='black', text='6', padx=21, pady=9, font='Helvetica 23', activebackground='dark grey', command=lambda: added_value.number_enter(6))
button_6.grid(row=3, column=5)
button_sub = Button(root, bg='dark orange', fg='black', text='-', padx=20, pady=9, font='Helvetica 23', activebackground='dark orange', command=lambda: added_value.operation('-'))
button_sub.grid(row=3, column=6)

# Row 4
button_sin = Button(root, bg='grey', fg='black', text='sin', padx=10, pady=9, font='Helvetica 23', activebackground='grey', command=lambda: added_value.trigo('sin'))
button_sin.grid(row=4, column=0, pady=9)
button_cos = Button(root, bg='grey', fg='black', text='cos', padx=10, pady=9, font='Helvetica 23', activebackground='grey', command=lambda: added_value.trigo('cos'))
button_cos.grid(row=4, column=1)
button_tan = Button(root, bg='grey', fg='black', text='tan', padx=16, pady=9, font='Helvetica 23', activebackground='grey', command=lambda: added_value.trigo('tan'))
button_tan.grid(row=4, column=2)
button_1 = Button(root, bg='silver', fg='black', text='1', padx=19, pady=9, font='Helvetica 23', activebackground='dark grey', command=lambda: added_value.number_enter(1))
button_1.grid(row=4, column=3)
button_2 = Button(root, bg='silver', fg='black', text='2', padx=26, pady=9, font='Helvetica 23', activebackground='dark grey', command=lambda: added_value.number_enter(2))
button_2.grid(row=4, column=4)
button_3 = Button(root, bg='silver', fg='black', text='3', padx=21, pady=9, font='Helvetica 23', activebackground='dark grey', command=lambda: added_value.number_enter(3))
button_3.grid(row=4, column=5)
button_add = Button(root, bg='dark orange', fg='black', text='+', padx=16, pady=9, font='Helvetica 23', activebackground='dark orange', command=lambda: added_value.operation('+'))
button_add.grid(row=4, column=6)

# Row 5
button_csc = Button(root, bg='grey', fg='black', text='csc', padx=6, pady=9, font='Helvetica 23', activebackground='grey', command=lambda: added_value.trigo('csc'))
button_csc.grid(row=5, column=0, pady=0)
button_sec = Button(root, bg='grey', fg='black', text='sec', padx=10, pady=9, font='Helvetica 23', activebackground='grey', command=lambda: added_value.trigo('sec'))
button_sec.grid(row=5, column=1)
button_cot = Button(root, bg='grey', fg='black', text='cot', padx=16, pady=9, font='Helvetica 23', activebackground='grey', command=lambda: added_value.trigo('cot'))
button_cot.grid(row=5, column=2)
button_0 = Button(root, bg='silver', fg='black', text='0', padx=75, pady=9, font='Helvetica 23', activebackground='dark grey', command=lambda: added_value.number_enter(0))
button_0.grid(row=5, column=3, columnspan=2)
button_dec = Button(root, bg='silver', fg='black', text='.', padx=25, pady=9, font='Helvetica 23', activebackground='dark grey', command=lambda: added_value.number_enter('.'))
button_dec.grid(row=5, column=5, columnspan=1)
button_eq = Button(root, bg='dark orange', fg='black', text='=', padx=16, pady=9, font='Helvetica 23', activebackground='dark orange', command=added_value.equals_to)
button_eq.grid(row=5, column=6)


def virtual_press(name, *event):
    if name == '7':
        button_7.config(relief=SUNKEN)
        screen.update()
        time.sleep(0.2)
        screen.update()
        button_7.config(relief=RAISED)
        screen.update()
    if name == '8':
        button_8.config(relief=SUNKEN)
        screen.update()
        time.sleep(0.2)
        screen.update()
        button_8.config(relief=RAISED)
        screen.update()
    if name == '9':
        button_9.config(relief=SUNKEN)
        screen.update()
        time.sleep(0.2)
        screen.update()
        button_9.config(relief=RAISED)
        screen.update()
    if name == '4':
        button_4.config(relief=SUNKEN)
        screen.update()
        time.sleep(0.2)
        screen.update()
        button_4.config(relief=RAISED)
        screen.update()
    if name == '5':
        button_5.config(relief=SUNKEN)
        screen.update()
        time.sleep(0.2)
        screen.update()
        button_5.config(relief=RAISED)
        screen.update()
    if name == '6':
        button_6.config(relief=SUNKEN)
        screen.update()
        time.sleep(0.2)
        screen.update()
        button_6.config(relief=RAISED)
        screen.update()
    if name == '1':
        button_1.config(relief=SUNKEN)
        screen.update()
        time.sleep(0.2)
        screen.update()
        button_1.config(relief=RAISED)
        screen.update()
    if name == '2':
        button_2.config(relief=SUNKEN)
        screen.update()
        time.sleep(0.2)
        screen.update()
        button_2.config(relief=RAISED)
        screen.update()
    if name == '3':
        button_3.config(relief=SUNKEN)
        screen.update()
        time.sleep(0.2)
        screen.update()
        button_3.config(relief=RAISED)
        screen.update()
    if name == '0':
        button_0.config(relief=SUNKEN)
        screen.update()
        time.sleep(0.2)
        screen.update()
        button_0.config(relief=RAISED)
        screen.update()
    if name == '.':
        button_dec.config(relief=SUNKEN)
        screen.update()
        time.sleep(0.2)
        screen.update()
        button_dec.config(relief=RAISED)
        screen.update()
    if name == '*':
        button_mult.config(relief=SUNKEN)
        screen.update()
        time.sleep(0.2)
        screen.update()
        button_mult.config(relief=RAISED)
        screen.update()
    if name == '/':
        button_div.config(relief=SUNKEN)
        screen.update()
        time.sleep(0.2)
        screen.update()
        button_div.config(relief=RAISED)
        screen.update()
    if name == '-':
        button_sub.config(relief=SUNKEN)
        screen.update()
        time.sleep(0.2)
        screen.update()
        button_sub.config(relief=RAISED)
        screen.update()
    if name == '+':
        button_add.config(relief=SUNKEN)
        screen.update()
        time.sleep(0.2)
        screen.update()
        button_add.config(relief=RAISED)
        screen.update()
    if name == '%':
        button_perc.config(relief=SUNKEN)
        screen.update()
        time.sleep(0.2)
        screen.update()
        button_perc.config(relief=RAISED)
        screen.update()
    if name == 'xn':
        button_xn.config(relief=SUNKEN)
        screen.update()
        time.sleep(0.2)
        screen.update()
        button_xn.config(relief=RAISED)
        screen.update()
    if name == 'yrtx':
        button_yrtx.config(relief=SUNKEN)
        screen.update()
        time.sleep(0.2)
        screen.update()
        button_yrtx.config(relief=RAISED)
        screen.update()
    if name == '=':
        button_eq.config(relief=SUNKEN)
        screen.update()
        time.sleep(0.2)
        screen.update()
        button_eq.config(relief=RAISED)
        screen.update()
    if name == 'c':
        button_c.config(relief=SUNKEN)
        screen.update()
        time.sleep(0.2)
        screen.update()
        button_c.config(relief=RAISED)
        screen.update()
    if name == 'pm':
        button_pm.config(relief=SUNKEN)
        screen.update()
        time.sleep(0.2)
        screen.update()
        button_pm.config(relief=RAISED)
        screen.update()
    if name == 'cube':
        button_cube.config(relief=SUNKEN)
        screen.update()
        time.sleep(0.2)
        screen.update()
        button_cube.config(relief=RAISED)
        screen.update()
    if name == 'sq':
        button_square.config(relief=SUNKEN)
        screen.update()
        time.sleep(0.2)
        screen.update()
        button_square.config(relief=RAISED)
        screen.update()
    if name == '!':
        button_fac.config(relief=SUNKEN)
        screen.update()
        time.sleep(0.2)
        screen.update()
        button_fac.config(relief=RAISED)
        screen.update()
    if name == 'sqrt':
        button_sqrt.config(relief=SUNKEN)
        screen.update()
        time.sleep(0.2)
        screen.update()
        button_sqrt.config(relief=RAISED)
        screen.update()
    if name == 'ex':
        button_ex.config(relief=SUNKEN)
        screen.update()
        time.sleep(0.2)
        screen.update()
        button_ex.config(relief=RAISED)
        screen.update()
    if name == 'sin':
        button_sin.config(relief=SUNKEN)
        screen.update()
        time.sleep(0.2)
        screen.update()
        button_sin.config(relief=RAISED)
        screen.update()
    if name == 'cos':
        button_cos.config(relief=SUNKEN)
        screen.update()
        time.sleep(0.2)
        screen.update()
        button_cos.config(relief=RAISED)
        screen.update()
    if name == 'tan':
        button_tan.config(relief=SUNKEN)
        screen.update()
        time.sleep(0.2)
        screen.update()
        button_tan.config(relief=RAISED)
        screen.update()
    if name == 'csc':
        button_csc.config(relief=SUNKEN)
        screen.update()
        time.sleep(0.2)
        screen.update()
        button_csc.config(relief=RAISED)
        screen.update()
    if name == 'sec':
        button_sec.config(relief=SUNKEN)
        screen.update()
        time.sleep(0.2)
        screen.update()
        button_sec.config(relief=RAISED)
        screen.update()
    if name == 'cot':
        button_cot.config(relief=SUNKEN)
        screen.update()
        time.sleep(0.2)
        screen.update()
        button_cot.config(relief=RAISED)
        screen.update()
    if name == 'ln':
        button_ln.config(relief=SUNKEN)
        screen.update()
        time.sleep(0.2)
        screen.update()
        button_ln.config(relief=RAISED)
        screen.update()
    if name == 'log':
        button_l10.config(relief=SUNKEN)
        screen.update()
        time.sleep(0.2)
        screen.update()
        button_l10.config(relief=RAISED)
        screen.update()


# Binding keys
root.bind('7', lambda e: [added_value.number_enter(7), virtual_press('7')])
root.bind('8', lambda e: [added_value.number_enter(8), virtual_press('8')])
root.bind('9', lambda e: [added_value.number_enter(9), virtual_press('9')])
root.bind('4', lambda e: [added_value.number_enter(4), virtual_press('4')])
root.bind('5', lambda e: [added_value.number_enter(5), virtual_press('5')])
root.bind('6', lambda e: [added_value.number_enter(6), virtual_press('6')])
root.bind('1', lambda e: [added_value.number_enter(1), virtual_press('1')])
root.bind('2', lambda e: [added_value.number_enter(2), virtual_press('2')])
root.bind('3', lambda e: [added_value.number_enter(3), virtual_press('3')])
root.bind('0', lambda e: [added_value.number_enter(0), virtual_press('0')])
root.bind('.', lambda e: [added_value.number_enter('.'), virtual_press('.')])
root.bind('*', lambda e: [added_value.operation('*'), virtual_press('*')])
root.bind('/', lambda e: [added_value.operation('/'), virtual_press('/')])
root.bind('-', lambda e: [added_value.operation('-'), virtual_press('-')])
root.bind('+', lambda e: [added_value.operation('+'), virtual_press('+')])
root.bind('p', lambda e: [added_value.operation('%'), virtual_press('%')])
root.bind('n', lambda e: [added_value.operation('xn'), virtual_press('xn')])
root.bind('y', lambda e: [added_value.operation('yrtx'), virtual_press('yrtx')])
root.bind('<Return>', lambda e: [added_value.equals_to(), virtual_press('=')])
root.bind('<BackSpace>', lambda e: [added_value.clear(), virtual_press('c')])
root.bind('m', lambda e: [added_value.plus_minus(), virtual_press('pm')])
root.bind('u', lambda e: [added_value.cubed(), virtual_press('cube')])
root.bind('q', lambda e: [added_value.squared(), virtual_press('sq')])
root.bind('!', lambda e: [added_value.factorial(), virtual_press('!')])
root.bind('r', lambda e: [added_value.sqrt(), virtual_press('sqrt')])
root.bind('e', lambda e: [added_value.ex(), virtual_press('ex')])
root.bind('l', lambda e: [added_value.ln(), virtual_press('ln')])
root.bind('h', lambda e: [added_value.log(), virtual_press('log')])
root.bind('e', lambda e: [added_value.ex(), virtual_press('ex')])
root.bind('s', lambda e: [added_value.trigo('sin'), virtual_press('sin')])
root.bind('c', lambda e: [added_value.trigo('cos'), virtual_press('cos')])
root.bind('t', lambda e: [added_value.trigo('tan'), virtual_press('tan')])
root.bind('o', lambda e: [added_value.trigo('csc'), virtual_press('csc')])
root.bind('a', lambda e: [added_value.trigo('sec'), virtual_press('sec')])
root.bind('g', lambda e: [added_value.trigo('cot'), virtual_press('cot')])

# Displaying Tooltips
Hovertip(button_cube, 'Press "u" to display the cube of the number that has been entered.')
Hovertip(button_square, 'Press "q" to display the square of the number that has been entered.')
Hovertip(button_pm, 'Press "m" to change the sign of the number that has been entered.')
Hovertip(button_c, 'Press "BackSpace" to clear the display.')
Hovertip(button_xn, 'Press "n" and type another number to display the \nnth power of the first number that was entered.')
Hovertip(button_yrtx, 'Press "y" and type another number to display the \nnth root of the first number that was entered.')
Hovertip(button_perc, 'Press "p" and type another number to display the corresponding percentage.')
Hovertip(button_div, 'Press "/" and type another number to display the corresponding quotient.')
Hovertip(button_mult, 'Press "*" and type another number to display the corresponding product.')
Hovertip(button_add, 'Press "+" and type another number to display the corresponding sum.')
Hovertip(button_sub, 'Press "-" and type another number to display the corresponding difference.')
Hovertip(button_eq, 'Press "Enter" to display the total result.')
Hovertip(button_fac, 'Press "!" to display the factorial of the number that has been entered.')
Hovertip(button_sqrt, 'Press "r" to display the square root of the number that has been entered.')
Hovertip(button_sin, 'Press "s" to display the sine of the number that has been entered.')
Hovertip(button_cos, 'Press "c" to display the cosine of the number that has been entered.')
Hovertip(button_tan, 'Press "t" to display the tangent of the number that has been entered.')
Hovertip(button_csc, 'Press "o" to display the cosecant of the number that has been entered.')
Hovertip(button_sec, 'Press "a" to display the secant of the number that has been entered.')
Hovertip(button_cot, 'Press "g" to display the cotangent of the number that has been entered.')
Hovertip(button_ln, 'Press "l" to display the natural logarithm (base e)\nof the number that has been entered.')
Hovertip(button_l10, 'Press "h" to display the logarithm (base 10) of the number that has been entered.')
Hovertip(button_ex, 'Press "e" to display the value of "e" raised to the \npower of the number that has been entered.')

root.mainloop()