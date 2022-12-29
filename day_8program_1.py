def kelvin_to_fahrenhite(temperature):
    assert(temperature>=0),"colder then the obsolute zero at mtica!"
    res=((temperature-273)*1.8)+32
    return res
try:
    print(kelvin_to_fahrenhite(-50))
except Exception as ob:
    print(ob)
try:
    print(kelvin_to_fahrenhite(273))
except Exception as ob:
    print(ob)
try:
    print(kelvin_to_fahrenhite(505.78))
except Exception as ob:
    print(ob)
try:
    print(kelvin_to_fahrenhite(-5))
except Exception as ob:
    print(ob)

print("THANK YOU")
