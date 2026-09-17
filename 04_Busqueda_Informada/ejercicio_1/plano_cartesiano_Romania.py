import matplotlib.pyplot as plt

LOCATIONS: dict[str, tuple[float, float]] = {
    "Arad": (91, 492),
    "Bucharest": (400, 327),
    "Craiova": (253, 288),
    "Drobeta": (165, 299),
    "Eforie": (562, 293),
    "Fagaras": (305, 449),
    "Giurgiu": (375, 270),
    "Hirsova": (534, 350),
    "Iasi": (473, 506),
    "Lugoj": (165, 379),
    "Mehadia": (168, 339),
    "Neamt": (406, 537),
    "Oradea": (131, 571),
    "Pitesti": (320, 368),
    "Rimnicu Vilcea": (233, 410),
    "Sibiu": (207, 457),
    "Timisoara": (94, 410),
    "Urziceni": (456, 350),
    "Vaslui": (509, 444),
    "Zerind": (108, 531),
}

# Configuración del tamaño del gráfico
plt.figure(figsize=(10, 7))

# Extraer coordenadas e iterar para graficar
for city, (x, y) in LOCATIONS.items():
    plt.scatter(x, y, color="red", zorder=5)  # Dibuja el punto
    plt.annotate(
        city, (x, y), textcoords="offset points", xytext=(5, 5), ha="left"
    )  # Etiqueta el nombre

# Personalización del plano cartesiano
plt.title("Mapa de Ciudades (Coordenadas Cartesianas)")
plt.xlabel("Eje X")
plt.ylabel("Eje Y")
plt.grid(True, linestyle="--", alpha=0.6)

# Mostrar el gráfico
plt.show()