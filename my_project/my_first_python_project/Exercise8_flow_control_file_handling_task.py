with open("three_rings", "r+") as three_rings:
    rings = three_rings.read()
    rings = rings.replace("Ring", "Wing")
    print(rings)
    with open("three_wings.txt", "w+") as wings:
        wings.write(rings)

with open("three_wings.txt", "r") as w:
    print(w.read())




