import os
import time
import shutil
import subprocess

RED = "\033[31m"
RESET = "\033[0m"

MENU = f"""
███████╗ ███████╗ ██████╗  ██████╗ ██╗███████╗████████╗██╗   ██╗
██╔════╝ ██╔════╝██╔═══██╗██╔════╝ ██║██╔════╝╚══██╔══╝╚██╗ ██╔╝
█████╗   ███████╗██║   ██║██║  ███╗██║█████╗     ██║    ╚████╔╝ 
██╔══╝   ╚════██║██║   ██║██║   ██║██║██╔══╝     ██║     ╚██╔╝  
██║      ███████║╚██████╔╝╚██████╔╝██║███████╗   ██║      ██║   
╚═╝      ╚══════╝ ╚═════╝  ╚═════╝ ╚═╝╚══════╝   ╚═╝      ╚═╝   

╔══════════════════════════════════════════════════════════════════════════════╗
║ Fsociety Tool | v1.0.4                                     [ - ] [ □ ] [ X ] ║
╠══════════════════════════════════════════════════════════════════════════════╣
║                                                                              ║
║ [01] Tool Info              [11] Discord Token Info                         ║
║ [02] IP Info                [12] Discord Token Nuker                        ║
║ [03] DDOS (#soon)           [13] Discord Token Joiner                       ║
║ [04] Mass Report (#soon)    [14] Discord Token BruteForce                   ║
║ [05] Phone Number Lookup    [15] N/A                                       ║
║ [06] Mail Info              [16] Discord Token Generator                    ║
║ [07] Username Tracker       [17] Discord Nitro Generator                    ║
║ [08] SQL Vulnerability      [18] Discord Server Info                        ║
║ [09] Discord Raid           [19] Web Cloner (#soon)                         ║
║ [10] Dmall                  [20] Next Page (1/2) (#soon)                    ║
║                                                                              ║
╚══════════════════════════════════════════════════════════════════════════════╝
"""

ACTIONS = {
    0: "./tools/discord.py",
    1: "./tools/tool_info.py",
    2: "./tools/geoip.py",
    3: "./fsociety.py",
    4: "./fsociety.py",
    5: "./tools/phone_number.py",
    6: "./tools/mail_info.py",
    7: "./tools/username_tracker.py",
    8: "./tools/sql_vulnerability.py",
    9: "./tools/discord_raid.py",
    10: "./tools/dmall.py",
    11: "./tools/discord_token_info.py",
    12: "./tools/discord_token_nuker.py",
    13: "./tools/discord_token_joiner.py",
    14: "./tools/discord_token_bruteforce.py",
    15: "./fsociety.py",
    16: "./fsociety.py",
    17: "./tools/discord_nitro_generator.py",
    18: "./fsociety.py",
    19: "./tools/web_cloner.py",
    20: "./nextpage.py",
}

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def loading():
    clear()
    print(f"{RED}{MENU}{RESET}")

def run_choice(choice):
    path = ACTIONS.get(choice)
    if path:
        subprocess.run(["python", path])
    else:
        raise ValueError

def main():
    while True:
        clear()
        print(f"{RED}{MENU}{RESET}")

        try:
            choice = int(input("Choice >> ").strip())
            run_choice(choice)
            break
        except ValueError:
            print(f"{RED}[!] Invalid choice < [!]{RESET}")
            time.sleep(2)

if __name__ == "__main__":
    main()
