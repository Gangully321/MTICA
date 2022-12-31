def hod(name,marks):
    print("name:",name)
    print("marks:",marks)
    return None

#hod()          ->TypeError
#hod('pant')     ->TypeError
hod('Ganguly',99)
hod(99,'Gangully')

hod(marks=99,name='sourav') #keyword argument

