def hill_climbing(f, x0, generate_neighbors):
    x = x0
    while any((f(n) > f(x) for n in generate_neighbors(x))):
        x = max(generate_neighbors(x), key=f)
    return x
def f(x):
    return -x**2
generate_neighbors = lambda x: [x + delta for delta in [-0.1, 0.1]]
result = hill_climbing(f, 2.0, generate_neighbors)
print("Optimal solution:", result)
print("Optimal value:", f(result))
