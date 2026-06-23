# 🚀 ProxyScraper – Ultra‑Fast Proxy Scraper & Tester

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey)

An asynchronous, high‑speed proxy scraper and validator that collects thousands of free proxies from **100+ public sources** and tests them against `login.live.com` in seconds.  
Built for security researchers, developers, and anyone who needs a fresh, verified proxy list.

---

## ✨ Features

- 🕸️ **100+ Proxy Sources** – HTTPS & SOCKS5 lists gathered from the best free repositories.
- ⚡ **Blazing Fast** – Concurrent downloading & testing with hundreds of parallel connections.
- 📊 **Smart Verification** – Each proxy is checked **simultaneously** for both HTTPS and SOCKS5 support.
- 🌐 **Auto CDN Fallback** – GitHub raw links are automatically converted to jsDelivr CDN to avoid rate limits.
- 💾 **Results Sorted by Latency** – Working proxies saved with response time (ms) for easy selection.
- 🛡️ **Windows‑Friendly** – Uses `ProactorEventLoop` automatically on Windows to avoid FD limits.
- 🧪 **Respectful Scraping** – Random delays and user‑agent rotation keep you under the radar.

---

## 📦 Requirements

- Python **3.8+**
- Dependencies listed in [`requirements.txt`](requirements.txt)

```bash
pip install -r requirements.txt
```

> **Note for Windows users:** The script automatically activates the `ProactorEventLoop` policy. No extra steps required.

---

## 🚀 Quick Start

```bash
# 1. Clone the repository
git clone https://github.com/yourusername/proxyharvester.git
cd proxyharvester

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the scraper
python proxyharvester.py
```

After a short while you’ll find two files in the current directory:

- `working_https.txt` – HTTPS proxies with latency
- `working_socks5.txt` – SOCKS5 proxies with latency

---

## ⚙️ Customisation

All configuration is at the top of the script – no command‑line arguments needed.

| Variable               | Default                  | Description |
|------------------------|--------------------------|-------------|
| `PROXY_SOURCES`        | 100+ URLs                | List of sources to scrape. Add/remove any line. |
| `LOGIN_LIVE_URL`       | `https://login.live.com` | Target URL used for proxy validation. Change to any HTTP endpoint. |
| `TEST_TIMEOUT`         | `1.5` seconds            | Timeout for each test request. |
| `MAX_TEST_CONCURRENT`  | `800`                    | Maximum simultaneous tests. |
| `DOWNLOAD_CONCURRENT`  | `50`                     | Maximum simultaneous downloads. |

Edit these values directly in the script to fit your network and needs.

---

## 📁 Output Format

Each working proxy is saved as:

```
ip:port | Latency: Xms
```

Example:

```
192.168.1.100:8080 | Latency: 234ms
```

Latency is measured from the start of the request until the first byte of a `200 OK` response.

---

## 🧠 How It Works

1. **Download Phase**  
   Fetches proxy lists from all sources concurrently, parses `ip:port` pairs, and deduplicates them.

2. **Validation Phase**  
   Every unique proxy is tested **twice in parallel**:
   - As an **HTTPS proxy** using `aiohttp` with `http://` schema.
   - As a **SOCKS5 proxy** using `aiohttp_socks`.

3. **Output**  
   Results are sorted by latency and written to the respective output files.

---

## 📚 Use Cases

- Web scraping & crawling
- Security testing (pentesting, bug bounty)
- Accessing geo‑restricted content
- Load testing & network analysis
- Avoiding rate limits

---

## ⚠️ Disclaimer

This tool is intended for **educational and ethical purposes only**.  
You are responsible for complying with the terms of service of any website you access using these proxies.  
The proxies collected are **publicly available**; their quality and anonymity are not guaranteed.

---

## 🤝 Contributing

Pull requests are welcome!  
You can help by:

- Adding new proxy sources (make sure they’re reliable and public)
- Improving speed or accuracy
- Adding new protocols (HTTP, SOCKS4)
- Writing tests or documentation

---

## 📜 License

MIT – do what you want, just keep the credit.  
© 2026 [Your Name / Handle]

---

## ⭐ Support

If you find this tool useful, drop a ⭐ on the repo and share it with your Discord community!
