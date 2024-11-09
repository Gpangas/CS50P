import inflect
p = inflect.engine()

Name = []
while True:
    try:
        Name.append(input("Name: ").strip())
    except EOFError:
        print()
        break

for i in range(len(Name)):
    list = p.join(Name[:(i+1)])
    print("Adieu, adieu, to " + list)
