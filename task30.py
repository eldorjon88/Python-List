words = []

print("5 ta so'z kiriting:")

for _ in range(5):
    word = input()
    words.append(word)

palindromes = []

for w in words:
    if w == w[::-1]:
        palindromes.append(w)

print("Palindrom so'zlar:", palindromes)
