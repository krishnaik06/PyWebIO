# A simple script to do MAthematical calaculation
from pywebio.input import *
from pywebio.output import *
def mathemticaloperation():
    a = input("Enter the firt number：", type=FLOAT)
    b = input("Enter the second number：", type=FLOAT)
    c=0
    operation = radio("Choose one operation", options=['+', '*', '/', '%'])
    operation_name=""
    if operation=="+":
        operation_name="Addition"
        c=a+b
    elif operation=="*":
        operation_name="Multiplication"
        c=a*b
    elif operation=="/":
        operation_name="Division"
        c=a/b
    else:
        operation_name="Modulus"
        c=a%b
        
    put_text('The operation selected is: %s. and the output is: %.1f' % (operation_name, c))
if __name__ == '__main__':
    mathemticaloperation()
    
    
    
    
    