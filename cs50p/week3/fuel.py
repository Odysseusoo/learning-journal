def main():
    while True:
        try:
            fuel = input("Fraction: ")

            x, y = fuel.split("/")

            x = int(x)
            y = int(y)

            if x < 0 or y <= 0 or x > y:
                continue

            percent = round((x / y) * 100)

            if percent <= 1:
                print("E")
            elif percent >= 99:
                print("F")
            else:
                print(f"{percent}%")

            break

        except (ValueError, ZeroDivisionError):
            pass


main()
