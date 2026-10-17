t=int(input("Give first number :"))
h=int(input("Give second number: "))
z=input("Give me your function(+,-,*,/):")

def add(x,y):
    print("Result",x+y)
if z == "+" :
 add(t,h) 

   
def mul(x,y):
    print("Result:",x*y)
if z == "*" :
 mul(t,h) 
 
def sub(x,y):
    print("Result:",x-y)
if z == "-" :
 sub(t,h) 
 
def div(x,y):
     print("Result:",x/y)
if z == "/" :
  div(t,h) 