hrs = input("Enter Hours:")
h = float(hrs)
rt = input("Enter rate:")
r = float(rt)

if h <= 40 :
    pay = h * r
else :
    pay = (40 * r) + ((h - 40) * r * 1.5)

print(pay)
