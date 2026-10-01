
# juego: AVENTURA LEGENDARIA
# Diego Fernando Jiménez Murcia


import os
import random


# UTILIDADES

def limpiar():
    os.system("cls" if os.name == "nt" else "clear")


def pausar():
    input("\nPresiona ENTER para continuar...")


def titulo(texto):
    limpiar()
    print("=" * 60)
    print(texto.center(60))
    print("=" * 60)


# CLASE JUGADOR

class Jugador:
    def __init__(self, nombre, habilidad):
        self.nombre = nombre
        self.habilidad = habilidad
        self.vidas = 3
        self.monedas = 0
        self.puntos = 0
        self.nivel = 1
        self.checkpoint = 1
        self.objetos = []

    def mostrar_estado(self):
        print("\n========== ESTADO DEL JUGADOR ==========")
        print("Personaje:", self.nombre)
        print("Habilidad:", self.habilidad)
        print("Vidas:", self.vidas)
        print("Monedas:", self.monedas)
        print("Puntos:", self.puntos)
        print("Nivel:", self.nivel)
        print("Objetos:", self.objetos if self.objetos else "Ninguno")
        print("========================================")


#NIVELES

niveles = [
    {
        "nombre": "Bosque Encantado",
        "enemigo": "Lobos mágicos",
        "dificultad": 1,
        "recompensa": 100
    },
    {
        "nombre": "Cueva Misteriosa",
        "enemigo": "Murciélagos oscuros",
        "dificultad": 2,
        "recompensa": 150
    },
    {
        "nombre": "Desierto del Fuego",
        "enemigo": "Guerreros de arena",
        "dificultad": 3,
        "recompensa": 200
    },
    {
        "nombre": "Castillo Oscuro",
        "enemigo": "Caballeros oscuros",
        "dificultad": 4,
        "recompensa": 300
    },
    {
        "nombre": "Reino Final",
        "enemigo": "Rey Oscuro",
        "dificultad": 5,
        "recompensa": 500
    }
]


#PERSONAJES

def seleccionar_personaje():
    titulo("SELECCIONAR PERSONAJE")

    print("1. Alex - Ataque básico")
    print("2. Luna - Disparo preciso")
    print("3. Drako - Hechizo mágico")
    print("4. Rex - Golpe poderoso")

    while True:
        opcion = input("\nSelecciona tu personaje: ")

        if opcion == "1":
            return Jugador("Alex", "Ataque básico")

        elif opcion == "2":
            return Jugador("Luna", "Disparo preciso")

        elif opcion == "3":
            jugador = Jugador("Drako", "Hechizo mágico")
            jugador.puntos = 25
            return jugador

        elif opcion == "4":
            jugador = Jugador("Rex", "Golpe poderoso")
            jugador.vidas = 4
            return jugador

        else:
            print("Opción inválida. Intenta de nuevo.")


#EVENTOS

def recoger_monedas(jugador):
    cantidad = random.randint(5, 20)

    jugador.monedas += cantidad
    jugador.puntos += cantidad

    print("\n¡Encontraste monedas!")
    print("Monedas obtenidas:", cantidad)


def encontrar_premio(jugador):
    premios = [
        "Poción de vida",
        "Amuleto protector",
        "Tesoro antiguo"
    ]

    premio = random.choice(premios)

    jugador.objetos.append(premio)
    jugador.puntos += 30

    print("\n¡Encontraste un premio:", premio, "!")
    print("Ganaste 30 puntos.")


def enfrentar_enemigo(jugador, nivel):
    enemigos = [
        "Lobo mágico",
        "Goblin",
        "Guerrero de arena",
        "Caballero oscuro"
    ]

    enemigo = random.choice(enemigos)

    print("\n¡Apareció un enemigo:", enemigo, "!")

    print("1. Atacar")
    print("2. Defenderse")
    print("3. Huir")

    opcion = input("Selecciona una acción: ")

    if opcion == "1":
        probabilidad = 65

        if jugador.habilidad == "Disparo preciso":
            probabilidad += 10

        elif jugador.habilidad == "Hechizo mágico":
            probabilidad += 5

        elif jugador.habilidad == "Golpe poderoso":
            probabilidad += 8

        if random.randint(1, 100) <= probabilidad:
            puntos = random.randint(20, 45)
            jugador.puntos += puntos

            print("\n¡Derrotaste al enemigo!")
            print("Ganaste", puntos, "puntos.")

        else:
            print("\nTu ataque falló.")
            jugador.vidas -= 1
            print("Perdiste una vida.")

    elif opcion == "2":
        print("\nTe defendiste.")

        if random.randint(1, 100) <= 70:
            print("Bloqueaste el ataque.")
        else:
            jugador.vidas -= 1
            print("La defensa falló. Perdiste una vida.")

    elif opcion == "3":
        if random.randint(1, 100) <= 60:
            print("\nLograste escapar.")
        else:
            jugador.vidas -= 1
            print("No pudiste escapar. Perdiste una vida.")

    else:
        print("Acción inválida.")


def superar_obstaculo(jugador):
    obstaculos = [
        "Roca gigante",
        "Puente dañado",
        "Río peligroso",
        "Muro alto"
    ]

    obstaculo = random.choice(obstaculos)

    print("\nEncontraste un obstáculo:", obstaculo)

    print("1. Saltar")
    print("2. Agacharse")
    print("3. Buscar otro camino")

    opcion = input("Selecciona una acción: ")

    if opcion == "1":
        if random.randint(1, 100) <= 75:
            print("¡Superaste el obstáculo!")
            jugador.puntos += 10
        else:
            jugador.vidas -= 1
            print("Fallaste el salto.")

    elif opcion == "2":
        if random.randint(1, 100) <= 60:
            print("Evitaste el peligro.")
            jugador.puntos += 5
        else:
            jugador.vidas -= 1
            print("No lograste evitar el obstáculo.")

    elif opcion == "3":
        print("Encontraste un camino alternativo.")
        jugador.puntos += 3

    else:
        jugador.vidas -= 1
        print("No reaccionaste a tiempo.")


def activar_trampa(jugador):
    trampas = ["Espinas", "Fuego", "Roca que cae", "Trampa oculta"]

    trampa = random.choice(trampas)

    print("\n¡Cuidado! Se activó:", trampa)

    print("1. Esquivar")
    print("2. Defenderse")

    opcion = input("Selecciona una acción: ")

    if opcion == "1":
        if random.randint(1, 100) <= 55:
            print("¡Esquivaste la trampa!")
        else:
            jugador.vidas -= 1
            print("La trampa te alcanzó.")

    elif opcion == "2":
        if random.randint(1, 100) <= 70:
            print("Te defendiste correctamente.")
        else:
            jugador.vidas -= 1
            print("La defensa falló.")

    else:
        jugador.vidas -= 1
        print("Perdiste una vida.")


def evento_aleatorio(jugador, nivel):
    evento = random.choice([
        "monedas",
        "premio",
        "enemigo",
        "obstaculo",
        "trampa",
        "nada"
    ])

    if evento == "monedas":
        recoger_monedas(jugador)

    elif evento == "premio":
        encontrar_premio(jugador)

    elif evento == "enemigo":
        enfrentar_enemigo(jugador, nivel)

    elif evento == "obstaculo":
        superar_obstaculo(jugador)

    elif evento == "trampa":
        activar_trampa(jugador)

    else:
        print("\nEl camino está tranquilo.")
        jugador.puntos += 2

    pausar()


# USAR OBJETOS 

def usar_pocion(jugador):
    if "Poción de vida" in jugador.objetos:

        if jugador.vidas < 3:
            jugador.objetos.remove("Poción de vida")
            jugador.vidas += 1
            print("Recuperaste una vida.")
        else:
            print("Ya tienes todas tus vidas.")

    else:
        print("No tienes pociones.")

    pausar()


#BATALLA FINAL

def batalla_final(jugador):
    titulo("BATALLA FINAL: REY OSCURO")

    energia = 100

    print("¡El Rey Oscuro apareció!")
    print("Debes derrotarlo para salvar el reino.")

    while energia > 0 and jugador.vidas > 0:

        print("\nEnergía del Rey Oscuro:", energia)
        jugador.mostrar_estado()

        print("\n1. Atacar")
        print("2. Usar habilidad especial")
        print("3. Defenderse")

        opcion = input("Selecciona una acción: ")

        if opcion == "1":
            dano = random.randint(15, 30)
            energia -= dano
            print("Causaste", dano, "de daño.")

        elif opcion == "2":
            dano = random.randint(25, 40)
            energia -= dano
            print("Usaste tu habilidad especial.")
            print("Causaste", dano, "de daño.")

        elif opcion == "3":
            if random.randint(1, 100) <= 70:
                print("Bloqueaste el ataque del jefe.")
                pausar()
                continue
            else:
                print("Tu defensa falló.")

        else:
            print("Opción inválida.")
            continue

        if energia > 0:
            if random.randint(1, 100) <= 65:
                jugador.vidas -= 1
                print("El Rey Oscuro te atacó.")
                print("Perdiste una vida.")
            else:
                print("El Rey Oscuro falló.")

        pausar()

    if energia <= 0:
        titulo("¡HAS SALVADO EL REINO!")

        jugador.puntos += 1000

        print("Derrotaste al Rey Oscuro.")
        print("Puntos finales:", jugador.puntos)
        print("Monedas recolectadas:", jugador.monedas)

        return True

    titulo("GAME OVER")
    print("El Rey Oscuro te derrotó.")

    return False


# JUGAR NIVEL

def jugar_nivel(jugador, numero):
    nivel = niveles[numero - 1]

    titulo("NIVEL " + str(numero) + ": " + nivel["nombre"])

    print("Enemigo:", nivel["enemigo"])
    print("Dificultad:", nivel["dificultad"])
    print("Recompensa:", nivel["recompensa"], "puntos")

    pausar()

    acciones = 0
    limite = 6 + nivel["dificultad"]

    while acciones < limite and jugador.vidas > 0:

        titulo("NIVEL " + str(numero) + ": " + nivel["nombre"])

        print("Acción", acciones + 1, "de", limite)

        jugador.mostrar_estado()

        print("\n1. Caminar")
        print("2. Correr")
        print("3. Saltar")
        print("4. Agacharse")
        print("5. Atacar")
        print("6. Defenderse")
        print("7. Recoger objetos y monedas")
        print("8. Usar poción")
        print("9. Ver estado")
        print("0. Salir al menú")

        opcion = input("\nSelecciona una acción: ")

        if opcion in ["1", "2", "3", "4", "5", "6", "7"]:

            acciones += 1

            if opcion == "1":
                print("\nCaminas por el escenario.")

            elif opcion == "2":
                print("\nCorres por el escenario.")

            elif opcion == "3":
                print("\nSaltas para superar obstáculos.")

            elif opcion == "4":
                print("\nTe agachas para evitar peligros.")

            elif opcion == "5":
                print("\nTe preparas para atacar.")

            elif opcion == "6":
                print("\nAdoptas una posición defensiva.")

            elif opcion == "7":
                print("\nBuscas monedas y premios.")

            evento_aleatorio(jugador, nivel)

        elif opcion == "8":
            usar_pocion(jugador)

        elif opcion == "9":
            jugador.mostrar_estado()
            pausar()

        elif opcion == "0":
            return "menu"

        else:
            print("Opción inválida.")
            pausar()

        if jugador.vidas <= 0:
            titulo("GAME OVER")

            print("Te quedaste sin vidas.")
            print("Regresarás al último punto de control.")

            jugador.vidas = 3
            jugador.nivel = jugador.checkpoint

            pausar()

            return "game_over"

    if jugador.vidas <= 0:
        return "game_over"

    jugador.puntos += nivel["recompensa"]

    if numero < 5:
        jugador.nivel = numero + 1
        jugador.checkpoint = jugador.nivel

        titulo("NIVEL COMPLETADO")

        print("Completaste:", nivel["nombre"])
        print("Ganaste", nivel["recompensa"], "puntos.")
        print("Avanzaste al nivel", jugador.nivel)

        pausar()

        return "completado"

    return "final"


# INICIAR JUEGO

def iniciar_juego():
    jugador = seleccionar_personaje()

    while jugador.nivel <= 5:

        resultado = jugar_nivel(jugador, jugador.nivel)

        if resultado == "menu":
            return

        elif resultado == "game_over":
            return

        elif resultado == "final":
            batalla_final(jugador)
            pausar()
            return


#OPCIONES

def opciones():
    titulo("OPCIONES")

    print("1. Ver controles")
    print("2. Ver instrucciones")
    print("3. Regresar")

    opcion = input("\nSelecciona una opción: ")

    if opcion == "1":
        titulo("CONTROLES")

        print("Caminar: explorar el escenario.")
        print("Correr: avanzar rápidamente.")
        print("Saltar: superar obstáculos.")
        print("Agacharse: evitar peligros.")
        print("Atacar: enfrentar enemigos.")
        print("Defenderse: bloquear ataques.")
        print("Recoger: obtener monedas y premios.")

        pausar()

    elif opcion == "2":
        titulo("INSTRUCCIONES")

        print("1. Comienzas con 3 vidas.")
        print("2. Recolecta monedas y premios.")
        print("3. Supera obstáculos.")
        print("4. Derrota a los enemigos.")
        print("5. Completa los cinco niveles.")
        print("6. Derrota al Rey Oscuro.")

        pausar()


#CRÉDITOS

def creditos():
    titulo("CRÉDITOS")

    print("AVENTURA LEGENDARIA")
    print("Proyecto de minijuego en Python")
    print("Autor: Diego Fernando Jiménez Murcia")

    print("\nPersonajes:")
    print("Alex - Personaje principal.")
    print("Luna - Arquera.")
    print("Drako - Mago.")
    print("Rex - Guerrero.")
    print("Rey Oscuro - Enemigo final.")

    pausar()


#MENÚ PRINCIPAL

def menu_principal():

    while True:

        titulo("AVENTURA LEGENDARIA")

        print("1. Jugar")
        print("2. Opciones")
        print("3. Créditos")
        print("4. Salir")

        opcion = input("\nSelecciona una opción: ")

        if opcion == "1":
            iniciar_juego()

        elif opcion == "2":
            opciones()

        elif opcion == "3":
            creditos()

        elif opcion == "4":
            titulo("SALIR")

            print("Gracias por jugar Aventura Legendaria.")
            print("¡Hasta la próxima!")

            break

        else:
            print("Opción inválida.")
            pausar()


#EJECUTAR PROGRAMA

if __name__ == "__main__":
    menu_principal()
