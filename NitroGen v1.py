
import os
import random
import string
import requests
import time

# Enable colors on Windows
os.system("")

# Colors
G = "\033[92m"  # Green
Y = "\033[93m"  # Yellow
C = "\033[96m"  # Cyan
M = "\033[95m"  # Magenta
W = "\033[0m"   # Reset

print(f"{M}   MED NITRO GENERATOR 2026 – MOROCCO EDITION 🇲🇦⚡{W}")
print(f"{C}   Pure generator → sends every code to your webhook{W}\n")

# Get webhook
while True:
    webhook = input(f"{Y}Enter your Discord webhook URL → {W}").strip()
    if webhook.startswith("https://discord.com/api/webhooks/"):
        try:
            requests.post(webhook, json={"content": "**MED GENERATOR STARTED** ⚡\nMade in Morocco with love ❤️"})
            print(f"{G}Webhook connected! Test message sent.{W}\n")
            break
        except:
            print(f"{G}Failed to send test message. Try again.{W}")
    else:
        print(f"{G}That doesn't look like a webhook URL. Try again.{W}")

# How many codes
try:
    amount = int(input(f"{Y}How many Nitro codes to generate & send? → {W}") or "500")
except:
    amount = 500

print(f"\n{C}Starting to generate and send {amount} codes... (0.5s delay){W}\n")
time.sleep(2)

generated_links = []  # List to store all generated codes
sent = 0
for i in range(amount):
    # Generate 16-char random code
    code = "".join(random.choices(string.ascii_letters + string.digits, k=16))
    link = f"https://discord.gift/{code}"
    generated_links.append(link)  # Save to list
    
    # Send to webhook
    try:
        requests.post(webhook, json={
            "content": f"`{link}`",
            "username": "MED Nitro Generator",
            "avatar_url": "https://flagcdn.com/ma.svg"
        })
        sent += 1
        print(f"{G}{link}{W}")
    except:
        print(f"{G}Failed to send one code (internet issue?){W}")
    
    # 0.5 second delay between messages
    time.sleep(0.2)

# NEW FEATURE: Create folder and save results
folder_name = "nitro_results"
try:
    os.makedirs(folder_name, exist_ok=True)  # Create folder if not exists
    file_path = os.path.join(folder_name, "generated_nitro_codes.txt")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write("MED NITRO GENERATOR RESULTS\n")
        f.write("=" * 50 + "\n\n")
        for link in generated_links:
            f.write(f"{link}\n")
    print(f"\n{G}Results saved! Check folder: {folder_name}/generated_nitro_codes.txt{W}")
except Exception as e:
    print(f"{G}Failed to create folder or save file: {e}{W}")

print(f"\n{M}╔{'═'*50}╗{W}")
print(f"{M}║    ALL {sent}/{amount} CODES SENT SUCCESSFULLY!    ║{W}")
print(f"{M}╚{'═'*50}╝{W}")
print(f"{C}Check your Discord server now, king! ❤️{W}")
input(f"{Y}Press Enter to close...")