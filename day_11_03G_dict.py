#check  if a value exist in a dictionary
#write a python program to check if value 200 exists in the following dict

india={
    'tamilNadu':'Chennai',
    'bihar':'patna',
    'karnataka':'banglore',
    'mumbai':'delhi',
    'andhra pradesh':'amaravathi'
    }
keys=['tamilNadu','andhra pradesh']



 
for k,v in india.items():
    if v=='amaravathi':
        print('for',v,'key is',k)
