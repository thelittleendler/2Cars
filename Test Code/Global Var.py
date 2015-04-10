__author__ = 'John Choo'
variable = 4

def printer():
    global variable
    variable += 1
    print variable

printer()