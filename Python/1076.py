# Resistance

'''there will be three numbers given as input, the first two numbers are the first two digits of the resistance value, 
and the third number is the multiplier. The output should be the resistance value in ohms.'''

color = {'black': 0, 'brown': 1, 'red': 2, 'orange': 3, 'yellow': 4, 'green': 5, 'blue': 6, 'violet': 7, 'grey': 8, 'white': 9}

a = color[input()]
b = color[input()]
c = color[input()]

resistance = (a * 10 + b) * (10 ** c)
print(resistance)
