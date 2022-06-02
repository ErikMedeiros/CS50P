# https://cs50.harvard.edu/python/2022/psets/7/watch/

from re import fullmatch, search, IGNORECASE


def main():
    print(parse(input("HTML: ")))


def parse(html):
    if fullmatch(r"<iframe (?:[a-z]+=\"[a-z0-9/.:;, \-]+\"(?: (?!>)|))*></iframe>", html, IGNORECASE):
        youtube_re = r"(?:https?://(?:www\.)?)?youtube\.com/embed/([A-Za-z0-9_\-]{11})"

        if match := search(f"src=\"{youtube_re}\"", html):
            return f"https://youtu.be/{match.group(1)}"

    return None

if __name__ == "__main__":
    main()