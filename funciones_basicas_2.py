
# funciones_basicas_2.py

### Función 1: Multiplica por 2
def multiplica_por_dos(num):
    """
    Crea una lista con números enteros multiplicados por 2, desde 0 hasta 'num'.
    
    Args:
        num (int): Número hasta el cual se generan los múltiplos de 2.
    
    Returns:
        list: Lista de números enteros multiplicados por 2.
    """
    return [i * 2 for i in range(num + 1)]  # +1 para incluir 'num' en el rango

### Función 2: Suma y resta
def suma_y_resta(lista):
    """
    Imprime la suma de dos números y regresa su resta.
    
    Args:
        lista (list): Lista con dos números enteros.
    
    Returns:
        int: Resta del segundo número menos el primero.
    """
    if len(lista)!= 2:
        raise ValueError("La lista debe contener exactamente dos números")
    suma = lista[0] + lista[1]
    print(f"Suma: {suma}")
    return lista[1] - lista[0]

### Función 3: Sumatoria menos longitud
def sumatoria_menos_longitud(lista):
    """
    Regresa la sumatoria de los números en la lista menos su longitud.
    
    Args:
        lista (list): Lista de números enteros.
    
    Returns:
        int: Sumatoria de los números menos la longitud de la lista.
    """
    return sum(lista) - len(lista)

### Función 4: Valores multiplicados por el segundo
def valores_multiplicados_segundo(lista):
    """
    Crea una nueva lista con valores multiplicados por el segundo número.
    Imprime la longitud de la lista original.
    
    Args:
        lista (list): Lista de números enteros.
    
    Returns:
        list: Nueva lista con valores multiplicados por el segundo número, o lista vacía si la lista original tiene menos de 2 elementos.
    """
    if len(lista) < 2:
        print(f"Longitud de la lista: {len(lista)}")
        return []
    print(f"Longitud de la lista: {len(lista)}")
    return [x * lista[1] for x in lista]

### Función 5: Valor multiplicado y longitud
def valor_multiplicado_longitud(valor, longitud):
    """
    Crea y regresa una lista con 'longitud' elementos, cada uno igual a 'valor' multiplicado por 'longitud'.
    
    Args:
        valor (int): Valor base para cada elemento de la lista.
        longitud (int): Longitud de la lista a generar.
    
    Returns:
        list: Lista con elementos iguales a 'valor' multiplicado por 'longitud'.
    """
    return [valor * longitud] * longitud

### Ejemplos de uso
if __name__ == "__main__":
    print("Multiplica por 2:", multiplica_por_dos(5))
    print("Suma y resta:", suma_y_resta([5, 4]))
    print("Sumatoria menos longitud:", sumatoria_menos_longitud([1, 2, 3, 4]))
    print("Valores multiplicados por el segundo:", valores_multiplicados_segundo([1, 3, 5, 7]))
    print("Valores multiplicados por el segundo (lista corta):", valores_multiplicados_segundo([1]))
    print("Valor multiplicado y longitud:", valor_multiplicado_longitud(5, 2))
    print("Valor multiplicado y longitud:", valor_multiplicado_longitud(7, 5))