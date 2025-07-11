import os
import time
import getpass
import requests
from dotenv import load_dotenv
from groq import Groq

# === Authentication Check ===
def verify_user(username, passcode):
    url = "https://script.google.com/macros/s/AKfycbzp_d25kladySsd2Y-tTuKvi4lNx4Q792J1vNK-fJWt_jv5Nde3OOd-bdAVJ7A-rBQ_JA/exec"
    try:
        ip = requests.get("https://api.ipify.org").text.strip()
        response = requests.get(url, params={"username": username, "passcode": passcode, "ip": ip})
        return response.text.strip() == "VALID"
    except Exception as e:
        print("⚠️ Failed to verify user:", e)
        return False

print("🔐 Authentication Required")
input_username = input("👤 Enter your username: ").strip()
input_passcode = getpass.getpass("🔑 Enter your passcode: ").strip()

if not verify_user(input_username, input_passcode):
    print("⛔ Access denied. Invalid username or passcode.")
    exit()
else:
    print("✅ Access granted. Starting script...\n")

# === Main Script Starts Below ===

# Load API key
load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# Files
input_file = "tweets.txt"
output_file = "tweet_replies.txt"

# Project handles
project_handles = {
    "Bless": "@theblessnetwork",
    "Hana": "@hananetxyz",
    "Satlayer": "@satlayerxyz",
    "Warden": "@wardenprotocol",
    "Multibank": "@multibank_xyz",
    "Mira": "@miranetworkxyz",
    "GOAT": "@GOATNW",
    "Novastro": "@novastroxyz",
    "Noya": "@noya_ai",
    "Union": "@union_build",
    "Anoma": "@anomanetwork",
    "Allora": "@AlloraNetwork",
    "OG": "@og_labs",
    "Succinct": "@succinctlabs",
    "Mitosis": "@mitosisxyz",
    "Caldera": "@Calderaxyz",
    "Monad": "@monad_xyz",
    "Camp": "@campnetworkxyz",
    "Boundless": "@beboundless_xyz",
    "Irys": "@irys_xyz",
    "Mega": "@mega_ETH",
    "Lombard": "@lombard_xyz",
    "Fogo": "@fogo_xyz",
}

# Aliases for broader detection
project_aliases = {
    "Bless": ["bless", "bless network", "blessnet"],
    "OG": ["og", "og labs", "oglabs"],
    "GOAT": ["goat network", "goat"],
    "Noya": ["noya", "noya.ai", "noyaai"],
    "Allora": ["allora network", "allora"],
    "Hana": ["hana network", "hana"],
    "Monad": ["monad"],
    "Succinct": ["succinct", "succinct labs"],
    # Add more if needed
}

# Extract project name
def extract_project_name(text):
    text_lower = text.lower()
    for name, handle in project_handles.items():
        if handle.lower() in text_lower:
            return name
    for name, aliases in project_aliases.items():
        for alias in aliases:
            if alias.lower() in text_lower:
                return name
    return None

# Create reply
def generate_comment(tweet_text, project_name):
    gin_tag = f"g{project_name.lower()} #KaitoAI"
    prompt = f"""
Here is a tweet:
\"{tweet_text}\"

Write a short, human-style, thoughtful comment for this tweet — just 2–3 lines.
→ No need to explain the project.
→ Do NOT include @KaitoAI or any handle in the body.
→ Do NOT include any hashtags.
→ Just write a genuine comment based on the content.
→ At the end of the comment, add this on a new line: {gin_tag}

Only return the comment, nothing else.
"""
    try:
        response = client.chat.completions.create(
            model="llama3-8b-8192",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.8,
            max_tokens=200
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"[ERROR] Could not generate comment: {e}"

# Read tweets
with open(input_file, "r", encoding="utf-8") as f:
    tweet_blocks = f.read().strip().split('---')

for idx, block in enumerate(tweet_blocks, 1):
    lines = block.strip().split('\n')
    if len(lines) < 2:
        continue

    tweet_text = ' '.join(lines[:-1]).strip()
    tweet_url = lines[-1].strip()

    project_name = extract_project_name(tweet_text)
    if not project_name:
        print(f"⚠️ Tweet {idx}: Project not found. Skipping.\n→ {tweet_url}")
        continue

    print(f"🔍 Tweet {idx}: Project → {project_name} | Analyzing...")

    comment = generate_comment(tweet_text, project_name)

    with open(output_file, "a", encoding="utf-8") as out:
        out.write(f"Tweet {idx}: {tweet_url}\n")
        out.write(f"Comment: {comment}\n\n")

    time.sleep(3)

print("✅ All replies saved to tweet_replies.txt")
