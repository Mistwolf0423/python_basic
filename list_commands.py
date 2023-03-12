if __name__ == "__main__":
    N = int(input())
    ls = []
    for i in range(N):
        s = list(input().split())
        if s[0] == "insert":
            ls.insert(int(s[1]), int(s[2]))
        if s[0] == "remove":
            ls.remove(int(s[1]))
        if s[0] == "append":
            ls.append(int(s[1]))
        if s[0] == "sort":
            ls.sort()
        if s[0] == "pop":
            ls.pop()
        if s[0] == "reverse":
            ls.reverse()
        if s[0] == "print":
            print(ls)
