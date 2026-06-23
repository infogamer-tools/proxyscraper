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
