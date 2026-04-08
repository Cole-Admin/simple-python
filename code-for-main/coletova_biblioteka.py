import os
import socket
import sys


IME_FAJLA_V1 = r"C:\Users\Home PC\Desktop\programiranje\program\dist\hosts.txt"

def pinger(host):
    response = os.system("ping -n 2 " + host)
    if response == 0:
        print(host, 'Host je dostupan!✅')
    else:
        print(host, 'Host nije dostupan!')

def pretraga_ip_po_domenu(domen):
    ip = socket.gethostbyname(domen)
    print(f"IP adresa od {domen} je {ip}")
    
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def proveri_internet_konekciju():
    response = os.system("ping -n 2 8.8.8.8")
    if response == 0:
        print("Internet konekcija je dostupna!✅")
    else:
        print("Internet konekcija nije dostupna!")

def port_info(port):
    f = open(IME_FAJLA_V1, "r")
    for line in f:
        p, name = line.strip().split(":")
        if int(p) == port:
            print(f"Port {port} → {name}")
            f.close()
            return
        else:
            print(f"Ne poznajem port {port}")
    f.close()

def meni():
    print("Dobrodosli u program!")
    print()
    
    while True:
        print("\n--- MENI ---")
        try:
            broj = int(input("Izaberite opciju:\n" 
            "1. Pingovanje hosta\n" 
            "2. Pretraga IP adrese po domenu\n" 
            "3. Provera internet konekcije\n"
            "4. Informacije o portu\n"
            "0. Izlaz\n"
            "Unesite broj: "))
        except:
            print("Morate uneti broj!")
            continue

        if broj == 1:
            host = input("Unesite IP adresu ili domen: ")
            pinger(host)
        elif broj == 2:
            domen = input("Unesite domen: ")
            pretraga_ip_po_domenu(domen)
        elif broj == 3:
            proveri_internet_konekciju()
        elif broj == 4:
            try:
                port = int(input("Unesite broj porta: "))
                port_info(port)
            except:
                print("Morate uneti broj!")
        elif broj == 0:
            print("--- KRAJ PROGRAMA ---")
            sys.exit()
        else:
            print("Nevalidan izbor")