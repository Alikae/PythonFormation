# is
user1 = {
    "name": "Jean",
    "age": 33
}
user2 = {
    "name": "Jean",
    "age": 33
}
print(user1 == user2)
print(user1 is user1)
print(user1 is user2)

mon_tableau = [3]
print(mon_tableau is mon_tableau)

# Un tableau étant caché derrière une réference, le comportement est un peu différent,
# il faut garder ca en tête.
print([3] is [3])

# is not
print([3] is not [3])

print(True is not False)

var = 4
def plus_three(n):
    return n + 3

var = plus_three(var)
print(var)