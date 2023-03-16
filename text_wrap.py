import textwrap


def wrap(string, max_width):
    results = []
    for i in range(0, len(string) + 1, max_width):
        slic = string[i : max_width + i]
        results.append(slic)
    return "\n".join(results)


if __name__ == "__main__":
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
