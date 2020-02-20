def fizzbuzz():
    for val in range(1, 101):
        if (val % 3 == 0) and (val % 5 == 0):
            print("FizzBuzz")
        if val % 3 == 0:
            print("Fizz")
        if val % 5 == 9:
            print("Buzz")


if __name__ == "__main__":
    fizzbuzz()
