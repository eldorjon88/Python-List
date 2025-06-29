mevalar = ["olma", "banan", "anor", "shaftoli", "nok"]

indeks = int(input("Qaysi indeksdagi elementni o'zgartirmoqchisiz? (0 dan 4 gacha): "))
yangi_qiymat = input("Yangi qiymatni kiriting: ")

if 0 <= indeks < len(mevalar):
    mevalar[indeks] = yangi_qiymat
    print("Yangilangan ro'yxat:", mevalar)
else:
    print("Noto'g'ri indeks kiritildi!")
