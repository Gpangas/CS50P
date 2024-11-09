import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    time = re.search(
        r"(?P<h_i>\d\d?)(?::(?P<m_i>\d\d))? (?P<t_i>(?:A|P)M) to (?P<h_f>\d\d?)(?::(?P<m_f>\d\d))? (?P<t_f>(?:A|P)M)",
        s,
    )
    if not time:
        raise ValueError

    h_i = int(time.group("h_i"))
    if time.group("m_i") == None:
        m_i = 0
    else:
        m_i = int(time.group("m_i"))
    h_f = int(time.group("h_f"))
    if time.group("m_f") == None:
        m_f = 0
    else:
        m_f = int(time.group("m_f"))

    if h_i not in range(13) or h_f not in range(13):
        raise ValueError
    elif m_i not in range(60) or m_f not in range(60):
        raise ValueError

    if time.group("t_i") == "PM" and h_i != 12:
        h_i = h_i + 12
    if time.group("t_f") == "PM" and h_f != 12:
        h_f = h_f + 12
    if time.group("t_i") == "AM" and h_i == 12:
        h_i = 0
    if time.group("t_f") == "AM" and h_f == 12:
        h_f = 0

    return f"{h_i:02}:{m_i:02} to {h_f:02}:{m_f:02}"


if __name__ == "__main__":
    main()
