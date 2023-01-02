#get the key of minimum value from the given dictonary

sem2={
    'Data Structures':69,
    'Adbms':60,
    'DCCN':70
    }


print(min(sem2,key=sem2.get))
print(max(sem2,key=sem2.get))

