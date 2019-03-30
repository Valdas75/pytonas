print("Svaru konvertavimas ji kilogramus.")

pounds = eval(input("Svorio konvertavimas SVARAI= "))

print()

kilograms = pounds * 0.454

print()

print("svorys kilogramais=", kilograms, "kg")

string = 'QWERTYUIOPLKJHGFDSAZXCVBNM'
print(string.lower())

for fizzbuzz in range(61):
    if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
        print("fizzbuzz")
        continue
    elif fizzbuzz % 3 == 0:
        print("fizz")
        continue
    elif fizzbuzz % 5 == 0:
        print("buzz")
        continue
    print(fizzbuzz)

pounds = 10

kg = pounds / 2.200462262

print(f"pounds({pounds}) => kg({kg})")

kg =10

pounds = kg * 2.20462262

print(f"kg({kg}) => pounds({round(pounds, 3)}")