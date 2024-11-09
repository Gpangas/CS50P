from twttr import shorten


def main():
    test_shorten()


def test_shorten():
    assert shorten("hello") == "hll"
    assert shorten("HELLO") == "HLL"
    assert shorten("Hello!") == "Hll!"
    assert shorten("Hello123") == "Hll123"


if __name__ == "__main__":
    main()
