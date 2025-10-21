REG_SIZE = 69  # 68 chars + \n

## Para compilarlo inventario.py y luego correrlo:

def pad(text, length):
    return str(text).ljust(length)[:length]  # corta o rellena con espacios

def pad_num(n, length):
    return str(n).ljust(length)[:length]  # sin ceros a la izquierda

def id_existe(id_buscar):
    """Verifica si un ID (entero) ya existe en el archivo."""
    try:
        with open("inventario.txt", "r", encoding="utf-8") as f:
            for linea in f:
                id_actual = linea[:5].strip()
                if id_actual.isdigit() and int(id_actual) == id_buscar:
                    return True
    except FileNotFoundError:
        return False
    return False

def agregar_registro():
    print("\n=== AGREGAR REGISTRO ===")
    try:
        id = int(input("ID del producto (entero): "))
    except ValueError:
        print("ERROR: El ID debe ser un número entero.\n")
        return

    if id_existe(id):
        print("ERROR: El ID ya existe en el inventario.\n")
        return

    nombre = input("Nombre del producto: ")
    fabricante = input("Fabricante: ")
    categoria = input("Categoría: ")
    try:
        cantidad = int(input("Cantidad: "))
    except ValueError:
        print("ERROR: La cantidad debe ser un número entero.\n")
        return

    with open("inventario.txt", "a", encoding="utf-8") as f:
        linea = (
            pad_num(id, 5) +
            pad(nombre, 25) +
            pad(fabricante, 20) +
            pad(categoria, 12) +
            pad_num(cantidad, 6) +
            "\n"
        )
        f.write(linea)
    print(" Registro agregado correctamente.\n")

def lectura_secuencial():
    print("\n=== LECTURA SECUENCIAL ===")
    try:
        with open("inventario.txt", "r", encoding="utf-8") as f:
            for linea in f:
                print(linea.rstrip())
    except FileNotFoundError:
        print("No existe el archivo de inventario aún.\n")

def buscar_por_id():
    print("\n=== BÚSQUEDA POR ID ===")
    try:
        id_buscar = int(input("Ingrese el ID (entero): "))
    except ValueError:
        print("ERROR: El ID debe ser un número entero.\n")
        return

    try:
        with open("inventario.txt", "r", encoding="utf-8") as f:
            encontrado = False
            for linea in f:
                id_actual = linea[:5].strip()
                if id_actual.isdigit() and int(id_actual) == id_buscar:
                    print("Encontrado:", linea.rstrip(), "\n")
                    encontrado = True
                    break
            if not encontrado:
                print("No existe ese ID.\n")
    except FileNotFoundError:
        print("No existe el archivo de inventario.\n")

def buscar_por_categoria():
    print("\n=== BÚSQUEDA POR CATEGORÍA ===")
    cat = input("Ingrese la categoría a buscar: ")
    try:
        with open("inventario.txt", "r", encoding="utf-8") as f:
            encontrado = False
            for linea in f:
                categoria = linea[5+25+20:5+25+20+12].strip()
                if categoria.lower() == cat.lower():
                    print(linea.rstrip())
                    encontrado = True
            if not encontrado:
                print("No se encontraron productos en esa categoría.\n")
    except FileNotFoundError:
        print("No existe el archivo de inventario.\n")

def menu():
    while True:
        print("""
            =========== MENÚ DE INVENTARIO ===========
            1. Agregar registro
            2. Lectura secuencial
            3. Buscar por ID
            4. Buscar por categoría
            5. Salir
            ==========================================
            """)
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_registro()
        elif opcion == "2":
            lectura_secuencial()
        elif opcion == "3":
            buscar_por_id()
        elif opcion == "4":
            buscar_por_categoria()
        elif opcion == "5":
            print("Salir del programa...")
            break
        else:
            print("Opción no válida, intente nuevamente.\n")
            print("Este programa fue desarrollado por Suárez.\n")

# --- PROGRAMA PRINCIPAL ---
if __name__ == "__main__":
    menu()
