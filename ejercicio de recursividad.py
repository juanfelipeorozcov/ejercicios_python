def forma_i(n):
    if n == 0:
        return
    forma_i(n - 1)
    print('a' * n)

print("forma_i")

forma_i(7)

def forma_ii(n):
    if n == 0:
        return
    print('a' * n)
    forma_ii(n - 1)

print("forma_ii")
forma_ii(6)

def forma_iii(n, espacios=0):
    if n == 0:
        return
    forma_iii(n - 1, espacios + 1)
    print(' ' * (2 * espacios) + 'a' * (2 * n - 1))

print("forma_iii")
forma_iii(10)