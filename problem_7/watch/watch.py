import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    try:
        Url = re.search(r"^.+src=\"https?://(?:www.)?youtube.com/embed/(\w+)\".+$", s)
        return f"https://youtu.be/{Url.group(1)}"
    except:
        return None


if __name__ == "__main__":
    main()
