
print("Content-Type: text/html\n\n")
n = 5
for i in range(1, n + 1):
    print(' ' * (n - i) + ''.join(map(str, range(1, i + 1))) + ''.join(map(str, range(i - 1, 0, -1))) + "<br>")
