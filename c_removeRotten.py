import re

def remove_rotten(bag_of_fruits):
    out = []
    for fruit in bag_of_fruits:
        fruit = fruit.lower()
        fruit = fruit.replace('rotten','')
        out.append(fruit)
    return out

print remove_rotten([])