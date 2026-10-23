# 🇲🇦 MED Nitro Generator 2026

<p align="center">
  A Python-based terminal utility for generating random Discord Nitro-style gift links and sending them to a Discord webhook.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
  <img src="https://img.shields.io/badge/Interface-CLI-black?style=for-the-badge" alt="CLI"/>
  <img src="https://img.shields.io/badge/Platform-Cross--platform-green?style=for-the-badge" alt="Cross-platform"/>
</p>

---

## 📖 Overview

**MED Nitro Generator 2026 — Morocco Edition** is a command-line Python project that generates random 16-character strings and formats them as Discord Nitro-style gift links.

The program can send generated links to a user-provided Discord webhook, display them in the terminal, and save the generated results to a local text file.

Built as an experimental programming project, it demonstrates random string generation, HTTP requests, webhook integration, terminal formatting, and file handling.

> **Important:** This project does not generate genuine Discord Nitro subscriptions. Its output consists of randomly generated strings, and the resulting links are not guaranteed to be valid or redeemable.

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
| `requests` | HTTP POST requests to Discord webhooks |
| `os` | Directory creation and terminal setup |
| `time` | Delays between operations |

The `random`, `string`, `os`, and `time` modules are part of Python's standard library. The project additionally requires the `requests` package.

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

Replace `YOUR_USERNAME` and `YOUR_REPOSITORY` with the actual GitHub repository details.

### 2. Install dependencies

```bash
python -m pip install requests
```

### 3. Run the application

Save the script as `NitroGen.py`, then execute:

```bash
python NitroGen.py
```

On some Linux installations, you may need to use `python3` instead of `python`.

## 🖥️ How It Works

1. The program requests a Discord webhook URL.
2. It checks whether the URL begins with the expected Discord webhook prefix.
3. It attempts to send a startup notification through the webhook.
4. It asks how many random strings to generate, using `500` as the default.
5. It generates 16-character alphanumeric strings and formats them as gift links.
6. It attempts to send each generated link to the webhook.
7. It saves the generated links in a local text file.
8. It displays a completion summary in the terminal.

## 📂 Output Structure

After execution, the program creates the following directory and file:

```text
nitro_results/
└── generated_nitro_codes.txt
```

The text file contains a heading followed by the generated links.

## ⚙️ Configuration

The generation quantity is entered interactively when the program runs. If the input cannot be converted to an integer, the program defaults to 500.

The delay between generated-link requests is currently configured as:

```python
time.sleep(0.2)
```

The output directory is configured as:

```python
folder_name = "nitro_results"
```

## ⚠️ Limitations

- Generated strings are random and are not verified against Discord.
- The application cannot create genuine Nitro subscriptions.
- The webhook URL is entered at runtime.
- HTTP response status codes are not checked, so a completed HTTP request does not necessarily mean Discord accepted the message.
- Network and HTTP error handling could be improved.
- The script does not currently validate the requested quantity or implement rate-limit handling.
- The results file stores generated strings, not verified or redeemed codes.

## 🔒 Security & Responsible Use

- Treat Discord webhook URLs as secrets because anyone possessing one may be able to post messages through it.
- Do not publish real webhook URLs in source code, screenshots, logs, or public repositories.
- Use webhooks only in servers and channels where you have permission to send messages.
- Avoid excessive requests and respect Discord's rate limits.
- Do not use this project to mislead users into believing random links provide free Nitro.

## 🗺️ Future Improvements

Potential improvements for future versions include:

- [ ] Add structured logging and clearer error messages.
- [ ] Check HTTP status codes and handle failed requests.
- [ ] Implement Discord rate-limit handling.
- [ ] Add configurable request intervals.
- [ ] Validate user input and impose sensible quantity limits.
- [ ] Add automated unit tests.
- [ ] Separate generation, webhook delivery, and file storage into modules.
- [ ] Introduce a configuration file for non-sensitive settings.

## 🤝 Contributing

Contributions and suggestions are welcome.

1. Fork the repository.
2. Create a feature branch.
3. Commit your changes.
4. Open a pull request describing your improvements.

## 📄 License

Choose a license appropriate for your project and add its full text to a `LICENSE` file before claiming that the project is distributed under that license.

---

<p align="center">
  <b>MED Nitro Generator 2026</b><br/>
  Made in Morocco 🇲🇦
</p>
