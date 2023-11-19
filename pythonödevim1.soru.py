def f(x):
    return x*3 - 2 * x*2 - 5

def bisection_method(a, b, tol, max_iter):
    iter_count = 0

    while (b - a) / 2 > tol and iter_count < max_iter:
        c = (a + b) / 2
        if f(c) == 0:
            break
        elif f(c) * f(a) < 0:
            b = c
        else:
            a = c

        iter_count += 1

    return (a + b) / 2
 
# Başlangıç aralığı [2, 4]
a, b = 2, 4
tolerance = 1e-5
max_iterations = 4

root = bisection_method(a, b, tolerance, max_iterations)
print(f"Bulunan kök: {root}")
