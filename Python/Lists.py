if __name__ == '__main__':
    N = int(input())

    L = []


    for _ in range(N):
        selection = input().split()

        if selection[0] == "insert":
            L.insert(int(selection[1]), int(selection[2]))

        if selection[0] == "print":
            print(L)

        if selection[0] == "remove":
            L.remove(int(selection[1]))

        if selection[0] == "append":
            L.append(int(selection[1]))

        if selection[0] == "sort":
            L.sort()

        if selection[0] == "pop":
            L.pop()

        if selection[0] == "reverse":
            L.reverse()

