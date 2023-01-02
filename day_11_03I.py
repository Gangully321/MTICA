#change value of a key in a nested dictonary


mtica={'Betch':{'ECE','CSE','EEE','MECH','CIVIL','Duration':4},
'Intermediate':{'MPC','MEC','BIPC','Duration':2},
'Degree':{'MPCS','MSCS','b.COM','Duration':3}
       }


mtica['Degree']['Duration']=6
print(mtica)
