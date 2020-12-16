def main(n):
    p = 0
    q = 1
    for i in range(1, n + 1):
        p = 0.9 * p + 0.4 * q
        q = 1 - p
    p = round(p, 2)
    q = round(q, 2)
    return p, q

print(main(4))