import math

def equation(x):
    return 4 * math.exp(-0.5 * x) - x

def derivative(x):
    return -2 * math.exp(-0.5 * x) - 1

def newton_raphson(initial_guess, iterations):
    x_n = initial_guess
    for i in range(iterations):
        f_x_n = equation(x_n)
        f_prime_x_n = derivative(x_n)
        x_n = x_n - f_x_n / f_prime_x_n
    return x_n

initial_guess = 2
iterations = 4


root = newton_raphson(initial_guess, iterations)

print("Bulunan kök:", root)