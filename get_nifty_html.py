import sys

URL = "https://en.wikipedia.org/wiki/NIFTY_50"


def fetch_html(url=URL, out_file="nifty50.html"):
    try:
        import requests
    except ImportError:
        requests = None

    headers = {"User-Agent": "Mozilla/5.0 (compatible; fetcher/1.0)"}

    if requests:
        try:
            resp = requests.get(url, headers=headers, timeout=10)
            resp.raise_for_status()
            html = resp.text
            method = "requests"
        except Exception:
            requests = None

    if not requests:
        # fallback to urllib
        from urllib.request import Request, urlopen
        req = Request(url, headers=headers)
        with urlopen(req, timeout=15) as r:
            html = r.read().decode("utf-8")
        method = "urllib"

    with open(out_file, "w", encoding="utf-8") as f:
        f.write(html)

    print(f"Saved HTML to {out_file} using {method}")


if __name__ == "__main__":
    out = "nifty50.html"
    if len(sys.argv) > 1:
        out = sys.argv[1]
    fetch_html(out_file=out)
