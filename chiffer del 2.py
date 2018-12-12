
# Variabler och listor
word = ""
key = 12
letters = []
crypt = []
meny = 0


print("<<<| Välkommen till cryptotek |>>>")

# Loopar koden tills man väljer 3
while meny != 3:

    print("\n1. Kryptera: ") # Printar ut menyn
    print("2. Dekryptera: ")
    print("3. Avsluta: ")

    try: # Gör så att programmet inte crashar om du skriver in en bokstav istället för siffra
        meny = int(input("\n>>> Gör ett val: ")) # Sparar användarens inmatningar i variabeln meny som tillåter en att göra ett val
    except:
        print("Välj en siffra!")

    if meny == 1: #Om du trycker 1 så sker understående
        key = (int(input("\n>>> Skriv in en nyckel: "))) # Sparar användarens inmatning i variabeln key
        word = input("\n>>> Vad vill du kryptera: ") # Sparar användarens inmatning i listan word

        for letter in word: # För varje bokstav i listan så slår den ihop användarens inmatning i word och omvandlar det till siffror, den plusar också på med nyckeln
            letters.append(ord(letter) + key)

        print(letters) # Printar ut alla bokstäver
    
    elif meny == 2: # Om du trycker 2 så sker understående

        for l in letters: # För varje bokstav så...
            crypt.append(chr(l -key)) # Tar den bort nyckeln och omvandlar tillbaka det krypterade till bokstäver
        print(crypt) # Skriver ut det dekrypterade 

    else: # Helt oviktigt då det inte syns när man kör programmet i cmd
        print("<<< Det här syns inte >>>")

