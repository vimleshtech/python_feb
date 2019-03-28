class salary:
    def get_input(s):
        s.ecode= input('enter ecode :') 
        s.ename  = raw_input('enter ename :')
        s.bs= float(input('enter basic salary  :'))
    def cal(s):
        s.a= s.bs*0.4
        s.b= s.bs*0.2
        s.c= s.bs*0.1
        s.d= s.bs+s.b+s.c
    def display(a):
        print('Hra 40% of basic salary',a.a)
        print('br 20% of basic salary',a.b)
        print('ta 10% of basic salary',a.c)
        print('Gross salary',a.d)



f=salary()

print(f)

f.get_input()
f.cal()
f.display()

 
       
       
