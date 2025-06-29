names = []

while True:
    name = input("Ism kiriting.")
    if name == "":
        break
    names.append(name)

print("Jami ismlar soni:", len(names))
