three_rings = open("three_rings", "r+")
rings = three_rings.read()
print(rings)
rings = rings.replace(".", "")
rings = rings.replace(",", "")
rings = rings.split()
print(rings)
three_rings.close()
