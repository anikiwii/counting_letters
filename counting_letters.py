import matplotlib.pyplot as plt

letters = {}

try:
    for line in open("znachor.txt", encoding="UTF-8"):
        if len(line) > 1:
            for char in line:
                char = char.lower()
                if "a" <= char <= "z":
                    if char in letters:
                        letters[char] = letters[char]+1
                    else:
                        letters[char] = 1


except IOError as e:
    print(f"Nie mozna otworzyc pliku: {e}")

letters=dict(sorted(letters.items()))
print(letters)

plt.bar(letters.keys(), letters.values())
plt.show()