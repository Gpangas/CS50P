class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.cookies = 0

    def __str__(self):
        return f'{"🍪"*self.cookies}'

    def deposit(self, n):
        if (self.cookies + n) > self.capacity:
            raise ValueError("More deposit than capacity")
        self.cookies += n

    def withdraw(self, n):
        if (self.cookies - n) < 0:
            raise ValueError("Not enought cookies")
        self.cookies -= n

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if capacity < 0:
            raise ValueError("Invalid capacity")
        self._capacity = capacity

    @property
    def size(self):
        return self.cookies


def main():
    jar = Jar(10)
    jar.deposit(5)
    jar.withdraw(2)
    print(jar)


if __name__ == "__main__":
    main()
