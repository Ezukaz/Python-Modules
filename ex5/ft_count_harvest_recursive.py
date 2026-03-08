
def ft_count_harvest_recursive():
    def recur(n):
        if n == 0:
            return
        recur(n - 1)
        print(f"Day {n}")

    n = int(input("Days until harvest: "))
    recur(n)
    print("Harvest time!")
