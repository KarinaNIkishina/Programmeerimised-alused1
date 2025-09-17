#näide 1

age= int(input("sisesta vanus:"))
if age >= 18:
    text = " sa oled täiskasvane "
else:
    text = " sa oled liiga noor "
print(text)

#näide 2

arvKontrollimiseks = int(input("sisesta arv:"))
#           TRUE
if arvKontrollimiseks % 2 == 1:
    print("paaris arv")
else:
    print("paaritu arv")
    
#näide 3
    arv = int(input("sisesta punkti:"))
tulemus = 0
if arv<60:
    tulemus = "D"
else:
    if arv > 74:
        if arv > 89:
            tulemus = "A"
        else:
            tulemus = "B"
    else:
        tulemus= "C"
print("Teie tulemus", tulemus)
a = int(input("sisesta arv A:"))
b = int(input("sisesta arv B:"))
c = int(input("sisesta arv C:"))

if(a<b):
    if a>c:
        print(a)
    else:
        print(c)
else:
    if b>c:
        print(b)
    else:
        print(c)
