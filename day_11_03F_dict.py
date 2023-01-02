#DELETE A LIST OF KEYS FROM DICTONARY

india={
    'tamilNadu':'Chennai',
    'bihar':'patna',
    'karnataka':'banglore',
    'mumbai':'delhi',
    'andhra pradesh':'amaravathi'
    }

#keys to remove
keys=['tamilNadu','andhra pradesh']

for k in keys:
    india.pop(k)
print(india)


g=dict()
for i in india.keys()-keys:
    g[i]=india[i]

print(g)
