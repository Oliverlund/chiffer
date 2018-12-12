word = ""
key = 12
letters = []
crypt = []
meny = 0

print("<<<| Välkommen till cryptotek |>>>")

while meny != 3:

    print("\n1. Kryptera: ")
    print("2. Dekryptera: ")
    print("3. Avsluta: ")

    try:
        meny = int(input("\n>>> Gör ett val: "))
    except:
        print("Välj en siffra!")

    if meny == 1: 
        key = (int(input("\n>>> Skriv in en nyckel: ")))
        word = input("\n>>> Vad vill du kryptera: ")

        for letter in word:
            letters.append(ord(letter) + key)

        print(letters)
    
    elif meny == 2:

        for l in letters:
            crypt.append(chr(l -key))
        print(crypt)

    else:
        print("<<< Det här syns inte >>>")

