#write a python program to create a new dictonary by extracting the mentioned keys from a given
#dictionary.

bio={
    'country':'india',
    'states':'25+',
    'districts':1000
    }
keys=['states','country','districts']

new={}
for i in keys:
    new[i]=bio[i]
print(new)

new={i:bio[i] for i in keys}
print(new)


#new dict

res=dict()
for k in keys:
    res.update({k:bio[k]})
print(res)
