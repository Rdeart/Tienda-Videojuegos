# PROYECTO FINAL - MÓDULO 3: SISTEMA DE GESTIÓN DE TIENDA DE VIDEOJUEGOS
# Autor: Roberto Deart Perez
# Fecha: 18/05/2026

# =============================================================================
# DATOS INICIALES
# =============================================================================
videojuegos = {
    "VG001": {
        "nombre": "Pragmata",
        "plataforma": "PlayStation 5",
        "precio": 250000,
        "cantidad": 10,
    },
    "VG002": {
        "nombre": "Crimson Desert",
        "plataforma": "Xbox Series",
        "precio": 220000,
        "cantidad": 5,
    },
    "VG003": {
        "nombre": "Resident Evil 4 Remake",
        "plataforma": "Xbox Series X",
        "precio": 210000,
        "cantidad": 8,
    },
}

# =============================================================================
# FUNCIONES DEL SISTEMA
# =============================================================================


def agregar_videojuego(videojuegos: dict) -> None:
    """
    Agrega un nuevo videojuego al inventario con validaciones.
    """
    print("\n" + "=" * 50)
    print("AGREGAR NUEVO VIDEOJUEGO")
    print("=" * 50)

    # Solicitar código
    codigo = input("Ingrese el código del videojuego: ").strip().upper()

    # Validar código único
    if codigo in videojuegos:
        print("❌ Error: El código ya existe en el inventario.")
        return

    if not codigo:
        print("❌ Error: El código no puede estar vacío.")
        return

    # Solicitar nombre
    nombre = input("Ingrese el nombre del juego: ").strip()
    if not nombre:
        print("❌ Error: El nombre no puede estar vacío.")
        return

    # Solicitar plataforma
    plataforma = input("Ingrese la plataforma: ").strip()
    if not plataforma:
        print("❌ Error: La plataforma no puede estar vacía.")
        return

    # Solicitar precio
    try:
        precio = float(input("Ingrese el precio: "))
        if precio <= 0:
            print("❌ Error: El precio debe ser mayor a 0.")
            return
    except ValueError:
        print("❌ Error: El precio debe ser un número válido.")
        return

    # Solicitar cantidad
    try:
        cantidad = int(input("Ingrese la cantidad inicial: "))
        if cantidad < 0:
            print("❌ Error: La cantidad no puede ser negativa.")
            return
    except ValueError:
        print("❌ Error: La cantidad debe ser un número entero válido.")
        return

    # Agregar el videojuego
    videojuegos[codigo] = {
        "nombre": nombre,
        "plataforma": plataforma,
        "precio": precio,
        "cantidad": cantidad,
    }

    print(f"\n✅ Videojuego '{nombre}' agregado exitosamente.")


def mostrar_inventario(videojuegos: dict) -> None:
    """
    Muestra todos los videojuegos en formato tabular.
    """
    print("\n" + "=" * 80)
    print("INVENTARIO COMPLETO")
    print("=" * 80)

    if not videojuegos:
        print("📭 El inventario está vacío.")
        return

    # Encabezados
    print(
        f"{'Código':<8} {'Nombre':<30} {'Plataforma':<20} {'Precio':<12} {'Stock':<6}"
    )
    print("-" * 80)

    # Mostrar cada videojuego
    for codigo, info in videojuegos.items():
        nombre = info["nombre"][:28]  # Limitar longitud
        plataforma = info["plataforma"][:18]  # Limitar longitud
        precio = f"${info['precio']:,.0f}"
        cantidad = info["cantidad"]

        print(f"{codigo:<8} {nombre:<30} {plataforma:<20} {precio:>12} {cantidad:>6}")

    print("=" * 80)
    print(f"Total de videojuegos: {len(videojuegos)}")


def buscar_videojuego(videojuegos: dict) -> None:
    """
    Busca y muestra la información completa de un videojuego.
    """
    print("\n" + "=" * 50)
    print("BUSCAR VIDEOJUEGO")
    print("=" * 50)

    codigo = input("Ingrese el código del videojuego: ").strip().upper()

    if codigo in videojuegos:
        info = videojuegos[codigo]
        print("\n✅ Videojuego encontrado:")
        print("-" * 40)
        print(f"Código:      {codigo}")
        print(f"Nombre:      {info['nombre']}")
        print(f"Plataforma:  {info['plataforma']}")
        print(f"Precio:      ${info['precio']:,.0f}")
        print(f"Stock:       {info['cantidad']} unidades")
        print("-" * 40)
    else:
        print(f"❌ No se encontró videojuego con código '{codigo}'.")


def actualizar_precio(videojuegos: dict) -> None:
    """
    Actualiza el precio de un videojuego existente.
    """
    print("\n" + "=" * 50)
    print("ACTUALIZAR PRECIO")
    print("=" * 50)

    codigo = input("Ingrese el código del videojuego: ").strip().upper()

    if codigo not in videojuegos:
        print(f"❌ Error: No existe videojuego con código '{codigo}'.")
        return

    print(f"\nJuego actual: {videojuegos[codigo]['nombre']}")
    print(f"Precio actual: ${videojuegos[codigo]['precio']:,.0f}")

    try:
        nuevo_precio = float(input("Ingrese el nuevo precio: "))
        if nuevo_precio <= 0:
            print("❌ Error: El precio debe ser mayor a 0.")
            return
    except ValueError:
        print("❌ Error: El precio debe ser un número válido.")
        return

    precio_anterior = videojuegos[codigo]["precio"]
    videojuegos[codigo]["precio"] = nuevo_precio

    print(f"\n✅ Precio actualizado:")
    print(f"   Anterior: ${precio_anterior:,.0f}")
    print(f"   Nuevo:    ${nuevo_precio:,.0f}")


def registrar_venta(videojuegos: dict) -> None:
    """
    Registra una venta y actualiza el inventario.
    """
    print("\n" + "=" * 50)
    print("REGISTRAR VENTA")
    print("=" * 50)

    codigo = input("Ingrese el código del videojuego: ").strip().upper()

    if codigo not in videojuegos:
        print(f"❌ Error: No existe videojuego con código '{codigo}'.")
        return

    try:
        cantidad_venta = int(input("Ingrese la cantidad a vender: "))
        if cantidad_venta <= 0:
            print("❌ Error: La cantidad debe ser mayor a 0.")
            return
    except ValueError:
        print("❌ Error: La cantidad debe ser un número entero válido.")
        return

    # Validar stock disponible
    cantidad_disponible = videojuegos[codigo]["cantidad"]
    if cantidad_venta > cantidad_disponible:
        print(f"❌ Error: Stock insuficiente.")
        print(f"   Disponible: {cantidad_disponible} unidades")
        print(f"   Solicitado: {cantidad_venta} unidades")
        return

    # Procesar venta
    info = videojuegos[codigo]
    total_venta = info["precio"] * cantidad_venta

    # Actualizar inventario
    videojuegos[codigo]["cantidad"] -= cantidad_venta

    # Mostrar factura
    print("\n" + "=" * 50)
    print("FACTURA DE VENTA")
    print("=" * 50)
    print(f"Juego:            {info['nombre']}")
    print(f"Plataforma:       {info['plataforma']}")
    print(f"Precio unitario:  ${info['precio']:,.0f}")
    print(f"Cantidad:         {cantidad_venta} unidades")
    print("-" * 50)
    print(f"Total a pagar:    ${total_venta:,.0f}")
    print("=" * 50)
    print("✅ ¡Venta registrada exitosamente!")


def mostrar_estadisticas(videojuegos: dict) -> None:
    """
    Genera reportes estadísticos del inventario.
    """
    print("\n" + "=" * 50)
    print("ESTADÍSTICAS DEL INVENTARIO")
    print("=" * 50)

    if not videojuegos:
        print("📭 No hay datos para mostrar estadísticas.")
        return

    # Calcular total de videojuegos
    total_videojuegos = len(videojuegos)

    # Calcular valor total del inventario
    valor_total = sum(
        info["precio"] * info["cantidad"] for info in videojuegos.values()
    )

    # Encontrar videojuego más costoso
    juego_mas_costoso = max(videojuegos.items(), key=lambda x: x[1]["precio"])

    # Encontrar videojuego con mayor cantidad
    juego_mayor_cantidad = max(videojuegos.items(), key=lambda x: x[1]["cantidad"])

    # Calcular promedio de precios
    promedio_precios = (
        sum(info["precio"] for info in videojuegos.values()) / total_videojuegos
    )

    # Mostrar estadísticas
    print(f"\nTotal de videojuegos registrados:  {total_videojuegos}")
    print(f"Valor total del inventario:        ${valor_total:,.0f}")
    print(f"\nVideojuego más costoso:")
    print(
        f"  → {juego_mas_costoso[1]['nombre']} (${juego_mas_costoso[1]['precio']:,.0f})"
    )
    print(f"\nMayor cantidad disponible:")
    print(
        f"  → {juego_mayor_cantidad[1]['nombre']} ({juego_mayor_cantidad[1]['cantidad']} unidades)"
    )
    print(f"\nPromedio de precios:               ${promedio_precios:,.0f}")
    print("=" * 50)


def eliminar_videojuego(videojuegos: dict) -> None:
    """
    Elimina un videojuego del inventario.
    """
    print("\n" + "=" * 50)
    print("ELIMINAR VIDEOJUEGO")
    print("=" * 50)

    codigo = input("Ingrese el código del videojuego a eliminar: ").strip().upper()

    if codigo not in videojuegos:
        print(f"❌ Error: No existe videojuego con código '{codigo}'.")
        return

    nombre = videojuegos[codigo]["nombre"]

    # Confirmar eliminación
    confirmacion = input(f"¿Desea eliminar '{nombre}'? (s/n): ").strip().lower()

    if confirmacion == "s":
        del videojuegos[codigo]
        print(f"✅ Videojuego '{nombre}' eliminado exitosamente.")
    else:
        print("❌ Eliminación cancelada.")


def menu() -> None:
    """
    Muestra el menú principal y controla el flujo del programa.
    """
    while True:
        print("\n" + "=" * 50)
        print("    TIENDA DE VIDEOJUEGOS - MENÚ PRINCIPAL")
        print("=" * 50)
        print("1. Agregar videojuego")
        print("2. Mostrar inventario")
        print("3. Buscar videojuego por código")
        print("4. Actualizar precio")
        print("5. Registrar venta")
        print("6. Mostrar estadísticas")
        print("7. Eliminar videojuego")
        print("8. Salir")
        print("=" * 50)

        opcion = input("Seleccione una opción (1-8): ").strip()

        if opcion == "1":
            agregar_videojuego(videojuegos)
        elif opcion == "2":
            mostrar_inventario(videojuegos)
        elif opcion == "3":
            buscar_videojuego(videojuegos)
        elif opcion == "4":
            actualizar_precio(videojuegos)
        elif opcion == "5":
            registrar_venta(videojuegos)
        elif opcion == "6":
            mostrar_estadisticas(videojuegos)
        elif opcion == "7":
            eliminar_videojuego(videojuegos)
        elif opcion == "8":
            print("\n👋 ¡Gracias por usar el Sistema de Tienda de Videojuegos!")
            print("   ¡Hasta luego!")
            break
        else:
            print("❌ Opción no válida. Por favor, seleccione una opción entre 1 y 8.")


# =============================================================================
# PUNTO DE ENTRADA DEL PROGRAMA
# =============================================================================

if __name__ == "__main__":
    print("\n" + "=" * 50)
    print("  BIENVENIDO AL SISTEMA DE TIENDA DE VIDEOJUEGOS")
    print("=" * 50)
    print("\nCargando inventario inicial...")
    print(f"✅ {len(videojuegos)} videojuegos cargados.")

    menu()
