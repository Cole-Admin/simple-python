def calc():
    prvi_broj = float(input("Unesite prvi broj: "))
    

    znak = input("Unesite znak operacije (+, -, *, /): ")

    drugi_broj = float(input("Unesite drugi broj: "))

    if znak == "+":
        rezultat = prvi_broj + drugi_broj
        print("\nRezultat: ", rezultat)
    elif znak == "-":
        rezultat = prvi_broj - drugi_broj
        print("\nRezultat: ", rezultat)
    elif znak == "*":
        rezultat = prvi_broj * drugi_broj
        print("\nRezultat: ", rezultat)
    elif znak == "/":
        if drugi_broj != 0:
            rezultat = prvi_broj / drugi_broj
            print("\nRezultat: ", rezultat)
        else:
            print("Greška: Dijeljenje s nulom nije dozvoljeno.")
    else:
        print("Nevažeći znak operacije.")



