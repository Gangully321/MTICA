def hod(name,marks=99.9,age=23): #default
    print("name:",name)
    print("marks:",marks)
    print('age:',age)
    return None

#hod()          #->TypeError
hod('pant')     #->TypeError
hod('Ganguly',)
hod(99,'Ganesh')

hod(marks=99,name='sourav') #keyword argument

