def f(x):
    return x*3 + 4*x*2 - 10

def bisection_method(a, b, epsilon, max_iterations):
    iteration = 0
    while (b - a) / 2 > epsilon:
        c = (a + b) / 2
        if f(c) == 0:
            break
        elif f(c) * f(a) < 0:
            b = c
        else:
            a = c
        iteration += 1
        if iteration >= max_iterations:
            break
    return (a + b) / 2


a = 1
b = 2
epsilon = 1e-6
max_iterations = 4


solution = bisection_method(a, b, epsilon, max_iterations)


print("Bulunan kök:", solution)