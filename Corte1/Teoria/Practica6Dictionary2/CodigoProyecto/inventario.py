# Sistema de inventario simple - Programacion Aplicada
# John Niño

CATEGORIAS = ("electronicos", "ropa", "alimentos", "hogar", "otros")

# lista donde se guardan todos los productos
productos = []


def mostrar_bienvenida():
    print("   SISTEMA DE INVENTARIO - TIENDA SIMPLE")
    print("="*45)
    print("Categorias disponibles:", ", ".join(CATEGORIAS))
    print()


def mostrar_menu():
    print("\n--- MENU PRINCIPAL ---")
    print("1. Agregar producto")
    print("2. Mostrar todos los productos")
    print("3. Buscar producto")
    print("4. Eliminar producto")
    print("5. Salir")
    print("----------------------")


def agregar_producto():
    print("\n>> Agregar nuevo producto")

    codigo = input("Codigo del producto: ").strip()

    codigo_repetido = False
    for p in productos:
        if p["codigo"] == codigo:
            codigo_repetido = True

    if codigo_repetido:
        print("! Ya existe un producto con ese codigo.")
        return

    nombre = input("Nombre del producto: ").strip()

    if nombre == "":
        print("! El nombre no puede estar vacio.")
        return

    # validar precio: quitamos el punto y verificamos que sea numero
    precio_texto = input("Precio: ").strip()

    if not precio_texto.replace(".", "", 1).isnumeric():
        print("! El precio debe ser un numero.")
        return

    precio = float(precio_texto)

    # validar cantidad: solo numeros enteros
    cantidad_texto = input("Cantidad en stock: ").strip()

    if not cantidad_texto.isnumeric():
        print("! La cantidad debe ser un numero entero.")
        return

    cantidad = int(cantidad_texto)

    categoria = input("Categoria " + str(CATEGORIAS) + ": ").strip().lower()

    if categoria not in CATEGORIAS:
        print("! Categoria no valida. Se asignara 'otros'.")
        categoria = "otros"

    # armar el diccionario con los datos del producto
    nuevo_producto = {
        "codigo": codigo,
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad,
        "categoria": categoria
    }

    productos.append(nuevo_producto)
    print(">> Producto '" + nombre + "' agregado correctamente.")


def mostrar_productos():
    print("\n>> Lista de productos")

    if len(productos) == 0:
        print("  No hay productos registrados.")
        return

    print(f"{'COD':<8} {'NOMBRE':<20} {'PRECIO':>8} {'CANT':>6} {'CATEGORIA':<12}")
    print("-"*58)

    for p in productos:
        print(f"{p['codigo']:<8} {p['nombre']:<20} ${p['precio']:>7.2f} {p['cantidad']:>6} {p['categoria']:<12}")

    print("\nTotal de productos:", len(productos))


def buscar_producto():
    print("\n>> Buscar producto")
    termino = input("Codigo o nombre a buscar: ").strip().lower()

    encontrados = 0

    for p in productos:
        if termino in p["codigo"].lower() or termino in p["nombre"].lower():
            print("  -", p["codigo"], "|", p["nombre"], "| $" + str(p["precio"]), "| Cant:", p["cantidad"], "| Cat:", p["categoria"])
            encontrados = encontrados + 1

    if encontrados == 0:
        print("  No se encontro ningun producto.")
    else:
        print("  Total encontrados:", encontrados)


def eliminar_producto():
    print("\n>> Eliminar producto")
    codigo = input("Codigo del producto a eliminar: ").strip()

    indice = -1
    for i in range(len(productos)):
        if productos[i]["codigo"] == codigo:
            indice = i

    if indice == -1:
        print("  No se encontro un producto con ese codigo.")
        return

    nombre = productos[indice]["nombre"]
    confirmar = input("  Seguro que deseas eliminar '" + nombre + "'? (s/n): ").strip().lower()

    if confirmar == "s":
        productos.pop(indice)
        print("  Producto '" + nombre + "' eliminado.")
    else:
        print("  Operacion cancelada.")


# --- programa principal ---

mostrar_bienvenida()

opcion = ""

while opcion != "5":
    mostrar_menu()
    opcion = input("Elige una opcion: ").strip()

    if opcion == "1":
        agregar_producto()
    elif opcion == "2":
        mostrar_productos()
    elif opcion == "3":
        buscar_producto()
    elif opcion == "4":
        eliminar_producto()
    elif opcion == "5":
        print("\nHasta luego! Cerrando el sistema...")
    else:
        print("! Opcion no valida, intenta de nuevo.")
