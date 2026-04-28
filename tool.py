import os
import requests
import platform

def clear():
    os.system("clear")

def banner():
    print(r"""
██╗    ██╗ █████╗ ███████╗██████╗ ██╗   ██╗██████╗ ███████╗
██║    ██║██╔══██╗██╔════╝██╔══██╗██║   ██║██╔══██╗██╔════╝
██║ █╗ ██║███████║███████╗██████╔╝██║   ██║██████╔╝█████╗  
██║███╗██║██╔══██║╚════██║██╔══██╗██║   ██║██╔═══╝ ██╔══╝  
╚███╔███╔╝██║  ██║███████║██║  ██║╚██████╔╝██║     ███████╗
 ╚══╝╚══╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚═╝     ╚══════╝
    """)

def ip_lookup():
    ip = input("IP eingeben: ")
    try:
        data = requests.get(f"http://ip-api.com/json/{ip}").json()
        print("\n--- IP INFO ---")
        for k, v in data.items():
            print(f"{k}: {v}")
    except:
        print("Fehler beim Abrufen")

def system_info():
    print("\n--- SYSTEM INFO ---")
    print("System:", platform.system())
    print("Node:", platform.node())
    print("Release:", platform.release())
    print("Machine:", platform.machine())

def username_check():
    username = input("Username: ")
    sites = [
        f"https://github.com/{username}",
        f"https://instagram.com/{username}",
        f"https://twitter.com/{username}"
    ]
    print("\n--- CHECK ---")
    for site in sites:
        try:
            r = requests.get(site)
            if r.status_code == 200:
                print(f"[+] Gefunden: {site}")
            else:
                print(f"[-] Nicht gefunden: {site}")
        except:
            print(f"[!] Fehler bei {site}")

def main():
    while True:
        clear()
        banner()
        print("""
[1] IP Info
[2] Username Check
[3] System Info
[0] Exit
        """)

        c = input("> ")

        if c == "1":
            ip_lookup()
        elif c == "2":
            username_check()
        elif c == "3":
            system_info()
        elif c == "0":
            break
        else:
            print("Ungültig")

        input("\nEnter drücken...")

if __name__ == "__main__":
    main()
