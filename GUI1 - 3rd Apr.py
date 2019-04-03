'''
GUI Programming: Graphical user interface
	-> We can create or develop own application with user interface which can more 	interactive
	-> There is inbuilt module/package
	 import tkinter 

	-> There are following widgets: (user control )
		- frame
		- textbox / entry 
		- button 
		- label 

'''

from  tkinter import * #* : import all classes, 
o  = Tk() #toolkit

fl  = Label(text='First Name :')
fl.pack()
#fl.grid(1,1)

ft = Entry()
ft.pack()


ll  = Label(text='Last Name :')
ll.pack()

lt = Entry()
lt.pack()


f  = Label(text='FullName :')
f.pack()


def submit():
     print('you have clicked on submit button !!!')
     fn = ft.get()
     ln = lt.get()

     name = fn +' '+ln
     f.configure(text='Full name is '+name)
     
     
     

b = Button(text="Click Me",command=submit)
b.pack()




o.mainloop()





