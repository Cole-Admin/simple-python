import string

def obrni_tekst(tekst):
    return tekst[::-1]

def velika_slova(tekst):
    return tekst.upper()

def mala_slova(tekst):
    return tekst.lower()

def meni():
    print("Dobrodosli u Cole Text Tool!")
    print()
    
    while True:
        tekst = input("Unesite tekst: ")
        print("\n--- MENI ---")
        
        try: 
            broj = int(input("Izaberite opciju:\n" 
            "1. Obrni tekst\n" 
            "2. Velika slova\n" 
            "3. Mala slova\n"
            "0. Izlaz\n"
            "Unesite broj: "))
        except:
            print("Morate uneti broj!")
            continue

        if broj == 1:
            print(obrni_tekst(tekst))
        elif broj == 2:
            print(velika_slova(tekst))
        elif broj == 3:
            print(mala_slova(tekst))
        elif broj == 0:
            print("Dovidjenja!")
            break
        else:
            print("Nepostojeca opcija!")