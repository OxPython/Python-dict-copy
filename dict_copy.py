'''
Created on Jul 2, 2014

@author: viejoemer

How to copy or clone a dict in Python?

¿Cómo copiar o clonar un diccionario en Python?

The method copy() returns a shallow copy of the dictionary.
d2 = d.copy() is not equal than d2 = d
'''

#dict with three values and keys
d = {"one":1, "two":2, "three":3}
print(d)

#copy a dict into another variable
d2 = d.copy()
print(d2)

#Change dict d, insert a new value
d["Four"] = 4
print(d)

#Change dict d2, insert a new value
d2["Five"] = 5
print(d2)