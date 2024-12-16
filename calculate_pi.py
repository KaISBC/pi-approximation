import random

def calculate_pi(num_points):
    """Calcola un'approssimazione di π usando il metodo di Monte Carlo."""
    inside_circle = 0

    for _ in range(num_points):
        x, y = random.uniform(0, 1), random.uniform(0, 1)
        distance = x**2 + y**2
        if distance <= 1:
            inside_circle += 1

    return (inside_circle / num_points) * 4

if __name__ == "__main__":
    points = int(input("Inserisci il numero di punti da utilizzare: "))
    approx_pi = calculate_pi(points)
    print(f"Approssimazione di π con {points} punti: {approx_pi}")
