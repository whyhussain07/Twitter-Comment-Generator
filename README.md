# 🧠 Kaito Comment Generator Bot

This is a Python-based automation script that reads tweets from a file, detects the associated project, and generates short, human-like comments using the Groq API and LLaMA 3 models.

It includes secure user authentication via Google Sheets and supports a variety of crypto projects with aliases for broader detection.

---

## 🚀 Features

- ✅ Auto-detects the crypto project from tweet content
- 🧠 Generates smart, human-style comments using `llama3-8b-8192`
- 🔐 Username & passcode authentication via Google Sheets
- 📁 Reads input from `tweets.txt` and saves output to `tweet_replies.txt`
- 🔄 Supports aliases (e.g. "blessnet", "noya.ai", "oglabs")

---

## 📦 Requirements

- Python 3.10 or above
- `.env` file with your `GROQ_API_KEY`
- Dependencies listed in `requirements.txt`

---

## 🔧 Setup Instructions

1. **Clone this repository:**

```bash
git clone https://github.com/your-username/kaito-comment-bot.git
cd kaito-comment-bot
```

2. **Install dependencies:**

```bash
pip install -r requirements.txt
```

3. **Add your `.env` file:**

Create a file named `.env` and add your Groq API key:

```env
GROQ_API_KEY=your_groq_api_key_here
```

4. **Prepare `tweets.txt`:**

Each tweet block should look like this (text + URL, separated by `---`):

```
Bless has been doing crazy things with their modular design lately.
https://x.com/theblessnetwork/status/1234567890
---
Allora's model performance update is looking sharp.
https://x.com/AlloraNetwork/status/0987654321
```

---

## 🔐 Authentication

This script requires a **username** and **passcode** to run. Credentials are validated via a Google Sheets backend hosted on Google Apps Script. IP logging is also used to track access.

To get access:
- Contact the project maintainer to get your credentials added to the sheet.

---

## ✅ How to Run

```bash
python bot.py
```

You’ll be prompted for:

- 👤 `Username`
- 🔑 `Passcode`

After successful login, the bot will process all tweets in `tweets.txt` and save the results in `tweet_replies.txt`.

---

## 📂 Output Format (`tweet_replies.txt`)

```
Tweet 1: https://x.com/theblessnetwork/status/1234567890
Comment: Exciting move from Bless. Their modular architecture could change the game.

gbless #KaitoAI

Tweet 2: ...
```

---

## 🧩 Supported Projects

Includes detection support for 20+ top crypto projects like:

- Allora
- Bless
- Hana
- GOAT
- Monad
- OG Labs
- Succinct
- Noya
- ...and more!

You can expand support easily by editing the `project_handles` and `project_aliases` dictionaries in the script.

---

## 📜 License

MIT License. Free for personal and research use.

---

## 🙋‍♂️ Questions?

Open an issue or ping @yourname on Twitter!
