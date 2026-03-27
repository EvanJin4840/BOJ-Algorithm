# Multiplication

a = int(input())
b = int(input())

m3 = a * (b % 10)
m4 = a * ((b // 10) % 10)
m5 = a * (b // 100)

print(m3)
print(m4)
print(m5)
print(m3 + m4 * 10 + m5 * 100)