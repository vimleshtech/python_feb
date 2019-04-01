
class Compute:
    def get_input(s):
        
        s.roll = input('enter id :')  
        s.name  = raw_input('enter name :')
        s.addr= raw_input('enter address :')
        s.city = raw_input('enter city :')
        s.country =  raw_input('enter country:')
    def show(s):
        print('roll no ',s.roll)
        print('name ',s.name)
        print('addr ',s.addr)
        print('city ',s.city)
        print('country ',s.country)
    def Retroll(s):
        return s.roll
        
data = []

for i in range(0,3):
            
    o = Compute()
    o.get_input()
    data.append(o)
    #data.sort(0)

'''for d in data:
    d.show()'''

rn = input('enter roll no to search :')

for d in data:
    if d.Retroll() == rn:
        d.show()


        
    
        
