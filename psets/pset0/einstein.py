# https://cs50.harvard.edu/python/2022/psets/0/einstein/

M = int(input("Mass (kg): "))

# c squared
CC = 300000000 * 300000000

energy = M * CC

print(f"Energy (J): {energy}")