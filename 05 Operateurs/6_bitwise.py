# Les opérations bitwise sont des opérations "bit a bit".

# & (and)
print(5 & 9)
# 5 est représenté en binaire comme  101
# 9 est représenté en binaire comme 1001
# Le résultat du & est donc:        0001 -> 1

# | (or)
print(5 | 9)
# 5:      101
# 9:     1001
# 5 | 9: 1101 -> 13

# ^ (xor: or exclusif)
print(5 ^ 9)
# 5:      101
# 9:     1001
# 5 ^ 9: 1100 -> 12

# ~ (not)
print(~9)
# Ici les choses sont un peu plus compliquées, car l'un des bits est réservé pour le signe.

# >>, << (bitshift)
print(13 << 2)
print(13 >> 1)
# 13:        1101
# 13 >> 1:    110 -> 6
# 13 << 2: 110100 -> 52

# On peut concaténer ces opérateurs avec l'opérateur d'assignation (=)
var = 13
var >>= 2
print(var)
