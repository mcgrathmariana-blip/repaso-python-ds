# TAREA 1: Definición de variables
# Definimos los datos del producto utilizando distintos tipos de datos.

producto = "Auriculares"
precio_producto = 85.50
stock_producto = 20
tiene_descuento = True

print("TAREA 1: Información del producto")
print(
    f"Producto: {producto} | "
    f"Precio: ${precio_producto:.2f} | "
    f"Stock: {stock_producto} unidades | "
    f"Descuento disponible: {tiene_descuento}"
)


# TAREA 2: Bucle y condicional
# Recorremos los precios y los clasificamos según si superan 100.

precios = [45, 120, 89.90, 150, 100]

print("\nTAREA 2: Clasificación de precios")

for precio in precios:
    if precio > 100:
        print(f"${precio:.2f}: Caro")
    else:
        print(f"${precio:.2f}: Económico")


# TAREA 3: Diccionario de almacén

almacen = {
    "Auriculares": 20,
    "Teclado": 15,
    "Mouse": 30
}

# Agregamos un producto nuevo
almacen["Monitor"] = 10

# Consultamos el stock de un producto
print("\nTAREA 3: Stock del almacén")
print(f"Stock de Teclado: {almacen['Teclado']} unidades")


# TAREA 4: Función de resumen estadístico

def resumen_estadistico(numeros):
    return {
        "suma_total": sum(numeros),
        "promedio": sum(numeros) / len(numeros),
        "cantidad_elementos": len(numeros)
    }


# Probamos la función con una lista de ejemplo
print("\nTAREA 4: Resumen estadístico")
resultado = resumen_estadistico([10, 20, 30])
print(resultado)
