def get_negatives_loop(lst):
    result = []
    for x in lst:
        if x < 0:
            result.append(x)
    return result


def get_negatives_comprehension(lst):
    return [x for x in lst if x < 0]


def main():
    n = int(input("Введіть кількість елементів списку: "))
    a = []
    for i in range(n):
        val = float(input(f"  a[{i}] = "))
        a.append(val)

    print(f"\nВхідний список: {a}")

    result1 = get_negatives_loop(a)
    print(f"Від'ємні числа (без генератора): {result1}")

    result2 = get_negatives_comprehension(a)
    print(f"Від'ємні числа (з генератором):  {result2}")


if __name__ == "__main__":
    main()
