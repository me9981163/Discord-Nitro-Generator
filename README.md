# 🇲🇦 MED Nitro Generator v1

<p align="center">
  A Python-based terminal utility for generating random Discord Nitro-style gift links and sending them to a Discord webhook.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
  <img src="https://img.shields.io/badge/Interface-CLI-black?style=for-the-badge" alt="CLI"/>
  <img src="https://img.shields.io/badge/Version-v1-purple?style=for-the-badge" alt="Version"/>
</p>

---

## 📖 Overview

**MED Nitro Generator v1 — Morocco Edition** is a command-line Python project that generates random 16-character strings and formats them as Discord Nitro-style gift links.

The program can send generated links to a user-provided Discord webhook, display them in the terminal, and save the generated results to a local text file.

> **Important:** This project generates random strings, not genuine Discord Nitro subscriptions. Generated links are not guaranteed to be valid or redeemable.

## ✨ Features

- ⚡ **Random Code Generation** — Generates random 16-character alphanumeric strings.
- 🔗 **Link Formatting** — Formats each string as a `discord.gift` URL.
- 🌐 **Discord Webhook Integration** — Sends a startup notification and generated links to a configured webhook.
- 🎨 **Colored Terminal Output** — Uses ANSI escape sequences for colored messages.
- 💾 **Local Result Storage** — Saves generated links to a text file.
- 🔢 **Configurable Quantity** — Allows users to specify how many strings to generate, defaulting to 500.
- ⏱️ **Request Delay** — Includes a short delay between webhook requests.
- 📁 **Automatic Directory Creation** — Creates the output directory when necessary.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core application |
| `random` | Random string generation |
| `string` | Letters and digits |
| `requests` | HTTP POST requests |
| `os` | Directory and terminal setup |
| `time` | Delays between operations |

## 📋 Requirements

- Python 3
- pip
- An internet connection for webhook requests
- A Discord webhook URL for message delivery

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
cd YOUR_REPOSITORY
```

Replace the placeholders with your actual repository details.

### 2. Install dependencies

```bash
python -m pip install requests
```

### 3. Run the application

```bash
python "NitroGen v1.py"
```

On some Linux installations, use `python3` instead of `python`.

## 🖥️ How It Works

1. Requests a Discord webhook URL.
2. Checks whether the URL begins with the expected Discord webhook prefix.
3. Attempts to send a startup notification.
4. Requests the number of strings to generate, defaulting to 500.
5. Generates random 16-character alphanumeric strings.
6. Formats the strings as Discord gift links and attempts to send them to the webhook.
7. Saves the generated links to a local text file.
8. Displays a completion summary.

## 📂 Output Structure

```text
nitro_results/
└── generated_nitro_codes.txt
```

The file contains a heading followed by the generated links.

## ⚙️ Configuration

The number of strings is configured interactively. Invalid integer input defaults to 500.

The delay between requests is currently set to:

```python
time.sleep(0.2)
```

The output directory is configured as:

```python
folder_name = "nitro_results"
```

## ⚠️ Limitations

- Generated strings are not verified by Discord.
- The program cannot create genuine Nitro subscriptions.
- HTTP response status codes are not checked.
- Network error handling could be improved.
- The requested quantity is not validated against a maximum.
- Discord rate-limit handling is not implemented.
- The final sent count does not guarantee successful message delivery.

## 🔒 Security & Responsible Use

- Keep webhook URLs private.
- Never publish real webhook URLs in public repositories.
- Use webhooks only in channels where you have permission to post.
- Respect Discord's rate limits.
- Do not misrepresent random links as free Nitro subscriptions.

## 🗺️ Future Improvements

- [ ] Improve error handling and logging.
- [ ] Check HTTP response status codes.
- [ ] Implement rate-limit handling.
- [ ] Add configurable request intervals.
- [ ] Validate user input and limit generation quantities.
- [ ] Add automated tests.
- [ ] Separate code generation, webhook delivery, and file storage into modules.
- [ ] Add configuration options for non-sensitive settings.

## 🤝 Contributing

Contributions and suggestions are welcome.

1. Fork the repository.
2. Create a feature branch.
3. Commit your changes.
4. Open a pull request describing your improvements.

## 📄 License

Add a license of your choice to the repository and include its full text in a `LICENSE` file.

---

<p align="center">
  <b>MED Nitro Generator v1</b><br/>
  Made in Morocco 🇲🇦
</p>
