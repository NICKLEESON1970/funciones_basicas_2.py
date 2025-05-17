
# funciones_intermedias_1.py

### Actualizar valores en diccionarios y listas
matriz = [ [10, 15, 20], [3, 7, 14] ]
cantantes = [
    {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
    {"nombre": "Chayanne", "pais": "Puerto Rico"}
]
ciudades = {
    "México": ["Ciudad de México", "Guadalajara", "Cancún"],
    "Chile": ["Santiago", "Concepción", "Viña del Mar"]
}
coordenadas = [
    {"latitud": 8.2588997, "longitud": -84.9399704}
]

# Actualizar valores
matriz[1][0] = 6
cantantes[0]["nombre"] = "Enrique Martin Morales"
ciudades["México"][2] = "Monterrey"
coordenadas[0]["latitud"] = 9.9355431

print("Matriz actualizada:", matriz)
print("Cantantes actualizados:", cantantes)
print("Ciudades actualizadas:", ciudades)
print("Coordenadas actualizadas:", coordenadas)

### Función 1: Iterar a través de una lista de diccionarios
def iterarDiccionario(lista):
    """
    Recorre cada diccionario en la lista e imprime cada llave y su valor correspondiente.
    
    Args:
        lista (list): Lista de diccionarios.
    """
    for diccionario in lista:
        for llave, valor in diccionario.items():
            print(f"{llave} - {valor}")

# Ejemplo de uso
cantantes = [
    {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
    {"nombre": "Chayanne", "pais": "Puerto Rico"},
    {"nombre": "José José", "pais": "México"},
    {"nombre": "Juan Luis Guerra", "pais": "República Dominicana"}
]
print("\nIterar a través de una lista de diccionarios:")
iterarDiccionario(cantantes)

### Función 2: Obtener valores de una lista de diccionarios
def iterarDiccionario2(llave, lista):
    """
    Imprime el valor almacenado para la llave dada en cada diccionario de la lista.
    
    Args:
        llave (str): Nombre de la llave a buscar.
        lista (list): Lista de diccionarios.
    """
    for diccionario in lista:
        if llave in diccionario:
            print(diccionario[llave])

# Ejemplos de uso
print("\nObtener valores de una lista de diccionarios (nombre):")
iterarDiccionario2("nombre", cantantes)
print("\nObtener valores de una lista de diccionarios (pais):")
iterarDiccionario2("pais", cantantes)

### Función 3: Iterar a través de un diccionario con valores de lista
def imprimirInformacion(diccionario):
    """
    Imprime el nombre de cada clave junto con el tamaño de su lista y los valores de la lista.
    
    Args:
        diccionario (dict): Diccionario con valores de lista.
    """
    for llave, valor in diccionario.items():
        print(f"{len(valor)} {llave.upper()}")
        for item in valor:
            print(item)

# Ejemplo de uso
costa_rica = {
    "ciudades": ["San José", "Limón", "Cartago", "Puntarenas"],
    "comidas": ["gallo pinto", "casado", "tamales", "chifrijo", "olla de carne"]
}
print("\nIterar a través de un diccionario con valores de lista:")
imprimirInformacion(costa_rica)