
import coletova_biblioteka as cb
import cole_text_tool as ctt
import cole_kalkulator as ck

# python -m PyInstaller --onefile main.py

while True:
    print("\n--- GLAVNI MENI ---")
    try:
        broj = int(input("Izaberite opciju:\n" 
        "1. Cole Text Tool\n" 
        "2. Coletova Biblioteka\n"
        "3. Cole Kalkulator\n"
        "0. Izlaz\n"
        "Unesite broj: "))
    except:
        print("Morate uneti broj!")
        continue

    if broj == 1:
        ctt.meni()
    elif broj == 2:
        cb.meni()
    elif broj == 3:
        ck.calc()
    elif broj == 0:
        print("Dovidjenja!")
        break