import sys
import requests


def main():
    try:
        n = getValue()
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        response_conv = response.json()
        bpi = response_conv["bpi"]
        Usd = bpi["USD"]
        rate = float(Usd["rate"].replace(",", ""))
        print(f"${rate*n:,}")
    except requests.RequestException:
        pass


def getValue():
    try:
        n = float(sys.argv[1])
        return n
    except ValueError:
        sys.exit("Command-line argument is not a number")
    except IndexError:
        sys.exit("Missing command-line argument")


if __name__ == "__main__":
    main()
