import asyncio
import re
import time
import random
import sys
import aiohttp
from aiohttp_socks import ProxyConnector, ProxyType

# -------------------------------------------------------------------
# 100+ proxy sources (HTTPS + SOCKS5)
# -------------------------------------------------------------------
PROXY_SOURCES = [
    "https://api.proxyscrape.com/v2/?request=displayproxies&protocol=https&timeout=5000&country=all&ssl=all&anonymity=all",
    "https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks5&timeout=5000&country=all",
    "https://api.proxyscrape.com/?request=getproxies&proxytype=https&timeout=5000&country=all&ssl=all&anonymity=all",
    "https://api.proxyscrape.com/?request=getproxies&proxytype=socks5&timeout=5000&country=all",
    "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt",
    "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt",
    "https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/socks5.txt",
    "https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/https.txt",
    "https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt",
    "https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-https.txt",
    "https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt",
    "https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt",
    "https://raw.githubusercontent.com/hookzof/proxy_list/main/https.txt",
    "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/https.txt",
    "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/socks5.txt",
    "https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt",
    "https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt",
    "https://spys.me/proxy.txt",
    "https://spys.me/socks.txt",
    "https://openproxy.space/list/https",
    "https://openproxy.space/list/socks5",
    "https://proxylist.geonode.com/api/proxy-list?protocols=https&limit=500&page=1&sort_by=lastChecked&sort_type=desc",
    "https://proxylist.geonode.com/api/proxy-list?protocols=socks5&limit=500&page=1&sort_by=lastChecked&sort_type=desc",
    "https://www.proxy-list.download/api/v1/get?type=https",
    "https://www.proxy-list.download/api/v1/get?type=socks5",
    "https://www.proxy-list.download/api/v1/get?type=https&country=all",
    "https://www.proxy-list.download/api/v1/get?type=socks5&country=all",
    "http://proxydb.net/?protocol=https&anonlvl=4&anonlvl=3",
    "http://proxydb.net/?protocol=socks5&anonlvl=4&anonlvl=3",
    "https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/https.txt",
    "https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt",
    "https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/https.txt",
    "https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt",
    "https://raw.githubusercontent.com/mmpx12/proxy-list/master/https.txt",
    "https://raw.githubusercontent.com/mmpx12/proxy-list/master/socks5.txt",
    "https://raw.githubusercontent.com/Zaeem20/FREE_PROXY_LIST/master/https.txt",
    "https://raw.githubusercontent.com/Zaeem20/FREE_PROXY_LIST/master/socks5.txt",
    "https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/proxies/https.txt",
    "https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/proxies/socks5.txt",
    "https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt",
    "https://raw.githubusercontent.com/ALIILAPRO/proxy/main/https.txt",
    "https://raw.githubusercontent.com/ALIILAPRO/proxy/main/socks5.txt",
    "https://raw.githubusercontent.com/muaz-kadan/Proxy-List/main/https.txt",
    "https://raw.githubusercontent.com/muaz-kadan/Proxy-List/main/socks5.txt",
    "https://raw.githubusercontent.com/UptimerBot/proxy-list/main/proxies/https.txt",
    "https://raw.githubusercontent.com/UptimerBot/proxy-list/main/proxies/socks5.txt",
    "https://raw.githubusercontent.com/yemixzy/proxy-list/main/proxy-list/data.txt",
    "https://raw.githubusercontent.com/saschazesiger/Free-Proxies/master/proxies/https.txt",
    "https://raw.githubusercontent.com/saschazesiger/Free-Proxies/master/proxies/socks5.txt",
    "https://raw.githubusercontent.com/themiralay/Proxy-List/master/proxy-list/data.txt",
    "https://raw.githubusercontent.com/hw630/proxy-list/main/proxies/https.txt",
    "https://raw.githubusercontent.com/hw630/proxy-list/main/proxies/socks5.txt",
    "https://raw.githubusercontent.com/xtekky/proxy-list/main/proxies/https.txt",
    "https://raw.githubusercontent.com/xtekky/proxy-list/main/proxies/socks5.txt",
    "https://raw.githubusercontent.com/Zyplos/proxy-list/main/proxies/https.txt",
    "https://raw.githubusercontent.com/Zyplos/proxy-list/main/proxies/socks5.txt",
    "https://raw.githubusercontent.com/proxiware/proxy-list/main/proxies/https.txt",
    "https://raw.githubusercontent.com/proxiware/proxy-list/main/proxies/socks5.txt",
    "https://raw.githubusercontent.com/alexeysergeev/proxy-list/main/proxies/https.txt",
    "https://raw.githubusercontent.com/alexeysergeev/proxy-list/main/proxies/socks5.txt",
    "https://raw.githubusercontent.com/MShivaShankarReddy/proxy-list/main/proxies/https.txt",
    "https://raw.githubusercontent.com/MShivaShankarReddy/proxy-list/main/proxies/socks5.txt",
    "https://raw.githubusercontent.com/karthi-the-hacker/proxy-list/main/proxies/https.txt",
    "https://raw.githubusercontent.com/karthi-the-hacker/proxy-list/main/proxies/socks5.txt",
    "https://raw.githubusercontent.com/y3llowking/proxy-list/main/proxies/https.txt",
    "https://raw.githubusercontent.com/y3llowking/proxy-list/main/proxies/socks5.txt",
    "https://raw.githubusercontent.com/nikhil-ks/proxy-list/main/proxies/https.txt",
    "https://raw.githubusercontent.com/nikhil-ks/proxy-list/main/proxies/socks5.txt",
    "https://raw.githubusercontent.com/dzhang-ca/proxy-list/main/proxies/https.txt",
    "https://raw.githubusercontent.com/dzhang-ca/proxy-list/main/proxies/socks5.txt",
    "https://raw.githubusercontent.com/fyvri/free-proxy-list/main/proxy-list/data.txt",
    "https://raw.githubusercontent.com/T0XIC-D3VIL/proxy-list/main/proxies/https.txt",
    "https://raw.githubusercontent.com/T0XIC-D3VIL/proxy-list/main/proxies/socks5.txt",
    "https://www.proxy-list.download/api/v1/get?type=https&country=all",
    "https://www.proxy-list.download/api/v1/get?type=socks5&country=all",
    "https://api.getproxylist.com/proxy?protocol[]=https&allowsHttps=1",
    "https://api.getproxylist.com/proxy?protocol[]=socks5",
    "http://pubproxy.com/api/proxy?type=https&limit=100",
    "http://pubproxy.com/api/proxy?type=socks5&limit=100",
    "https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt",
    "https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt",
    "https://spys.me/socks.txt",
    "https://spys.me/proxy.txt",
    "https://api.proxyscrape.com/v2/?request=displayproxies&protocol=https&timeout=10000&country=all&ssl=all&anonymity=elite",
    "https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks5&timeout=10000&country=all",
]

LOGIN_LIVE_URL = "https://login.live.com"
OUTPUT_HTTPS = "working_https.txt"
OUTPUT_SOCKS5 = "working_socks5.txt"

# Fast test settings (safe for Windows ProactorEventLoop)
TEST_TIMEOUT = aiohttp.ClientTimeout(total=1.5)
MAX_TEST_CONCURRENT = 800

# Download anti‑rate‑limit
DOWNLOAD_CONCURRENT = 50
MIN_DELAY = 0.05
MAX_DELAY = 0.2

# -------------------------------------------------------------------
# Helpers
# -------------------------------------------------------------------
USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.4 Safari/605.1.15",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
]

def random_ua():
    return random.choice(USER_AGENTS)

def convert_to_cdn_url(raw_url):
    if "raw.githubusercontent.com" in raw_url:
        parts = raw_url.replace("https://raw.githubusercontent.com/", "").split("/", 3)
        if len(parts) == 4:
            user, repo, branch, path = parts
            return f"https://cdn.jsdelivr.net/gh/{user}/{repo}@{branch}/{path}"
    return raw_url

# Custom exception handler to suppress ConnectionResetError noise
def quiet_exception_handler(loop, context):
    exc = context.get("exception")
    if isinstance(exc, (ConnectionResetError, ConnectionAbortedError)):
        return
    loop.default_exception_handler(context)

async def fetch_proxies(session, url, semaphore):
    target = convert_to_cdn_url(url)
    async with semaphore:
        await asyncio.sleep(random.uniform(MIN_DELAY, MAX_DELAY))
        try:
            headers = {"User-Agent": random_ua()}
            async with session.get(target, headers=headers, timeout=8) as resp:
                if resp.status == 200:
                    text = await resp.text()
                    return re.findall(r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}:[0-9]{2,5}\b', text)
        except Exception:
            pass
        return []

async def test_https(session, proxy):
    proxy_url = f"http://{proxy}"
    start = time.time()
    headers = {"User-Agent": random_ua()}
    try:
        async with session.get(LOGIN_LIVE_URL, proxy=proxy_url,
                               timeout=TEST_TIMEOUT, headers=headers) as resp:
            if resp.status == 200:
                return round((time.time() - start) * 1000)
    except Exception:
        pass
    return None

async def test_socks5(proxy):
    start = time.time()
    headers = {"User-Agent": random_ua()}
    try:
        host, port = proxy.split(":")
        connector = ProxyConnector(proxy_type=ProxyType.SOCKS5, host=host, port=int(port), rdns=True)
        async with aiohttp.ClientSession(connector=connector, timeout=TEST_TIMEOUT) as session:
            async with session.get(LOGIN_LIVE_URL, headers=headers) as resp:
                if resp.status == 200:
                    return round((time.time() - start) * 1000)
    except Exception:
        pass
    return None

async def check_proxy(session, proxy, semaphore):
    async with semaphore:
        https_lat, socks5_lat = await asyncio.gather(
            test_https(session, proxy),
            test_socks5(proxy)
        )
        return proxy, https_lat, socks5_lat

# -------------------------------------------------------------------
# Main
# -------------------------------------------------------------------
async def main():
    # Install quiet exception handler on the running loop
    loop = asyncio.get_running_loop()
    loop.set_exception_handler(quiet_exception_handler)

    download_conn = aiohttp.TCPConnector(limit=DOWNLOAD_CONCURRENT, ttl_dns_cache=300)
    test_conn = aiohttp.TCPConnector(limit=MAX_TEST_CONCURRENT, ttl_dns_cache=300)
    download_sema = asyncio.Semaphore(DOWNLOAD_CONCURRENT)
    test_sema = asyncio.Semaphore(MAX_TEST_CONCURRENT)

    # ----- Download phase -----
    print(f"⚡ Downloading from {len(PROXY_SOURCES)} sources (rate‑limited)...")
    t0 = time.time()
    async with aiohttp.ClientSession(connector=download_conn) as session:
        tasks = [fetch_proxies(session, url, download_sema) for url in PROXY_SOURCES]
        results = await asyncio.gather(*tasks)

    all_proxies = set()
    for lst in results:
        if lst:
            all_proxies.update(lst)
    total = len(all_proxies)
    print(f"📊 Collected {total:,} unique proxies in {time.time()-t0:.1f}s.")

    if total == 0:
        print("❌ No proxies found. Exiting.")
        return

    # ----- Testing phase -----
    print(f"🔥 Testing against {LOGIN_LIVE_URL} (timeout={TEST_TIMEOUT.total}s, concurrency={MAX_TEST_CONCURRENT})...")
    t1 = time.time()
    https_working = []
    socks5_working = []
    completed = 0

    async with aiohttp.ClientSession(connector=test_conn) as test_session:
        # Create explicit tasks – no dangling coroutines
        check_tasks = {
            asyncio.create_task(check_proxy(test_session, p, test_sema)): p
            for p in all_proxies
        }

        for coro in asyncio.as_completed(check_tasks):
            try:
                proxy, https_lat, socks5_lat = await coro
                if https_lat is not None:
                    https_working.append((proxy, https_lat))
                if socks5_lat is not None:
                    socks5_working.append((proxy, socks5_lat))
            except Exception:
                pass
            completed += 1
            if completed % 1000 == 0:
                elapsed = time.time() - t1
                speed = completed / elapsed if elapsed > 0 else 0
                print(f"   ... {completed}/{total} tested ({elapsed:.1f}s, {speed:.0f} tests/s)")

    t2 = time.time()
    print(f"⏱️  Testing done in {t2-t1:.1f}s.")

    # ----- Save results -----
    https_working.sort(key=lambda x: x[1])
    socks5_working.sort(key=lambda x: x[1])

    with open(OUTPUT_HTTPS, "w") as f:
        for ip, lat in https_working:
            f.write(f"{ip} | Latency: {lat}ms\n")
    with open(OUTPUT_SOCKS5, "w") as f:
        for ip, lat in socks5_working:
            f.write(f"{ip} | Latency: {lat}ms\n")

    print(f"📁 {OUTPUT_HTTPS} → {len(https_working)} working HTTPS proxies")
    print(f"📁 {OUTPUT_SOCKS5} → {len(socks5_working)} working SOCKS5 proxies")
    print(f"🎉 Total working: {len(https_working)+len(socks5_working)} | Total time: {t2-t0:.1f}s")

if __name__ == "__main__":
    # Force ProactorEventLoop on Windows (avoids select() FD limit)
    if sys.platform == "win32":
        asyncio.set_event_loop_policy(asyncio.WindowsProactorEventLoopPolicy())
    asyncio.run(main())