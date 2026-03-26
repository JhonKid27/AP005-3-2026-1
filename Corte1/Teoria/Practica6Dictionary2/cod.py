## Este codigo es una practica un poco mas avanzada de la requerida, pero con los mismos objetivos de aprendizaje sobre esta misma 

# #### Get A Key
# puedes acceder a valores usando la clave
goles = {"Messi": 800, "Ronaldo": 850, "Neymar": 400, "Mbappe": 300, "Haaland": 250}
print(goles["Messi"])
print(goles["Haaland"])

posiciones = {"defensas": ["Ramos", "Pique", "Alaba"], "mediocampistas": ["Modric", "Xavi", "Busquets"], "delanteros": ["Messi", "Ronaldo", "Mbappe"]}
print(posiciones["delanteros"])
print(posiciones["defensas"])

## Get an Invalid Key
goles = {"Messi": 800, "Ronaldo": 850, "Neymar": 400, "Mbappe": 300, "Haaland": 250}
# print(goles["Pele"])  # ERROR si se descomenta

jugador_a_buscar = "Pele"
if jugador_a_buscar in goles:
    print(goles["Pele"])

posiciones = {"defensas": ["Ramos", "Pique", "Alaba"], "mediocampistas": ["Modric", "Xavi", "Busquets"], "delanteros": ["Messi", "Ronaldo", "Mbappe"]}
posiciones["porteros"] = "No hay porteros registrados"
if "porteros" in posiciones:
    print(posiciones["porteros"])

## Safely Get a Key
goles = {"Messi": 800, "Ronaldo": 850, "Neymar": 400, "Mbappe": 300, "Haaland": 250}
goles.get("Ronaldo")
goles.get("Pele")

dorsales = {"Messi": 10, "Ronaldo": 7, "Neymar": 10, "Modric": 10, "Ramos": 4}
if dorsales.get("Messi") == None:
    dorsal_messi = 99
else:
    dorsal_messi = dorsales.get("Messi")
print(dorsal_messi)

if dorsales.get("Haaland") == None:
    dorsal_haaland = 9
print(dorsal_haaland)

### Delete a Key
jugadores = {100: "Messi", 200: "Ronaldo", 300: "Neymar", 400: "Mbappe", 500: "Haaland"}
print(jugadores.pop(300, "Jugador no encontrado"))
print(jugadores)
print(jugadores.pop(999, "Jugador no encontrado"))
print(jugadores)
print(jugadores.pop(200, "Jugador no encontrado"))
print(jugadores)

estadisticas = {"pases": 50, "tiros": 8, "faltas": 3, "asistencias": 5, "goles": 2, "tarjetas": 1}
rendimiento = 0
rendimiento += estadisticas.pop("goles", 0)
rendimiento += estadisticas.pop("asistencias", 0)
rendimiento += estadisticas.pop("hat trick", 0)
print(estadisticas)
print(rendimiento)

## Get All Keys
plantel = {"Colombia": [85, 78, 90], "Brasil": [92, 88, 95], "Argentina": [95, 90, 97], "Francia": [93, 89, 94]}
print(list(plantel))
for seleccion in plantel.keys():
    print(seleccion)

equipos_ids = {"Real Madrid": 1001, "Barcelona": 1002}
torneos = {"Liga": 10, "Champions": 13, "Copa": 8}
equipos = equipos_ids.keys()
competencias = torneos.keys()
print(equipos)
print(competencias)

## Get All Values
plantel = {"Colombia": [85, 78, 90], "Brasil": [92, 88, 95], "Argentina": [95, 90, 97], "Francia": [93, 89, 94]}
for puntajes in plantel.values():
    print(puntajes)

torneos = {"Liga": 10, "Champions": 13, "Copa": 8}
total_partidos = 0
for partidos in torneos.values():
    total_partidos += partidos
print(total_partidos)

## Get All Items
goles = {"Messi": 800, "Ronaldo": 850, "Neymar": 400}
for jugador, cantidad in goles.items():
    print(jugador + " ha marcado " + str(cantidad) + " goles en su carrera")

ligas = {"Premier League": 20, "La Liga": 18, "Serie A": 15}
for liga, equipos in ligas.items():
    print("La " + liga + " tiene " + str(equipos) + " equipos participantes")
