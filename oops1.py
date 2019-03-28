'''

OOPS : object oriented programing system (structure)
Advantage of oops:
-Reusbalitiy of source code
-Support to modular programing, large task can be written in small set
-Easy to manage source code


There are following principles of oops:
-class              : is wrapper of data member and function/method
                    example:
                        class Compute:

                                



                        
-object             : is an instance of class
                    example:
                    o = Compute()

                    
-encapsulation     : is wrapping of data member and function in a unit i.e. called encapsulation
                    -every class is by default encapsulated 
-abstraction       : expose the essential features of class, and method and hide the defininatino i.e. called encapsulation 
-constructor       : is function which will invoke or call automatically when object will create
                    __init__()  : is inbuilt name which is constructor
-deconstructor
-inheritence
-overriding

'''

class Compute:
    def add(a):  #every function of class will take at least one argument which is ref of current object
        print('hello, add ',a)

    def sub(self,a,b):
        c =a-b
        print(c)

    def get_input(s):
        s.eid = input('enter id :')  #local variable , s.
        s.name  = raw_input('enter name :')
    def show(s):
        print(s.eid)
        print(s.name)


    def __init__(s):
        print('object is created')
        
        
        
o = Compute()
print(o)

o.add() #  --solved : error 
o.sub(11,2)

o.get_input()
o.show()





    


