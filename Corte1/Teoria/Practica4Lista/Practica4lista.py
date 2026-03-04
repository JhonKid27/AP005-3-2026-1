 sensores =  {"living room": 21, "kitchen": 23, "bedroom": 20, "pantry": 22}
 cantidad_camaras = {"backyard": 6,  "garage": 2, "driveway": 1}
 print(sensores)
 print(cantidad_camaras)
 lista_palabras = {"mountain": "orod", "bread": "bass", "friend": "mellon", "horse": "roch" }
 print(lista_palabras)
Verificando un error:
 potencias = {[1, 2, 4, 8, 16]: 2, [1, 3, 9, 27, 81]: 3}
  print(potencias)
 hijos = {"von Trapp": ["Johannes", "Rosmarie", "Eleonore"] , "Corleone": ["Sonny", "Fredo", "Michael"]}
 print(hijos)
 diccionario_vacio = {}
 print(diccionario_vacio)
 carta_menu = {"oatmeal": 3, "avocado toast": 6, "carrot juice": 5, "blueberry muffin": 2}
 print("Antes: ", carta_menu)
 carta_menu["cheesecake"] = 8
 print("Despues", carta_menu)
 animales_zoo = {"dinosaurs": 0}
 animales_zoo = {"dinosaurs": 0}
 animales_zoo = {"horses": 2}
 print(animales_zoo)
Agregar multiples claves
 sensores = {"living room": 21, "kitchen": 23, "bedroom": 20}
 print("Antes", sensores)
 Si quisieramos agregar 3 habitaciones nuevas, podriamos usar:
 sensores.update({"pantry": 22, "guest room": 25, "patio": 34})
 print("Despues", sensores)

 cuentas = {"teraCoder": 9018293, "proProgrammer": 119238}
 print(cuentas)
 cuentas.update({"theLooper": 138475, "stringQueen": 85739})
 print(cuentas)
 Sobreescribir Valores 
 Sabemos que podemos agregar una clave usando la siguiente sintaxis:
 carta_menu["banana"] = 3
 carta_menu = {"oatmeal": 3, "avocado toast": 6, "carrot juice": 5, "blueberry muffin": 2}
 print("Antes: ", carta_menu)
 carta_menu["oatmeal"] = 5
 print("Despues", carta_menu)
 Noten que el valor de "oatmeal" ahora cambio a 5.
 ganadores_oscar = {"Best Picture": "La La Land", "Best Actor": "Casey Affleck", "Best Actress": "Emma Stone", "Animated Feature": "Zootopia"}
 print("Antes", ganadores_oscar)
 print()
 ganadores_oscar.update({"Supporting Actress": "Viola Davis"})
 print("Despues1", ganadores_oscar)
 print()
 ganadores_oscar["Best Picture"] = "Moonlight"
 print("Despues2", ganadores_oscar)
Comprension de Diccionarios
 Digamos que tenemos dos listas que queremos combinar en un
 diccionario, como una lista de estudiantes y sus alturas
 en pulgadas:
nombres_estudiantes = ['Jenny', 'Alexus', 'Sam', 'Grace']
alturas_estudiantes = [61, 70, 67, 64]
 Python permite crear un diccionario usando
 una comprension de diccionario, con esta sintaxis:
 combinados = zip(nombres_estudiantes, alturas_estudiantes)
 print("combinados: ", combinados)
 datos_estudiantes = {clave:valor for clave, valor in zip(nombres_estudiantes, alturas_estudiantes)}
  datos_estudiantes es ahora {'Jenny': 61, 'Alexus': 70, 'Sam': 67, 'Grace': 64}
 print(datos_estudiantes)
  zip() combina dos listas en un iterador de tuplas con los elementos emparejados. Esta comprension:
 bebidas = ["espresso", "chai", "decaf", "drip"]
 niveles_cafeina = [64, 40, 0, 120]
 bebidas_combinadas = zip(bebidas, niveles_cafeina)
 print(bebidas_combinadas)
 cafeina_por_bebida = {clave:valor for clave, valor in bebidas_combinadas}
 print(cafeina_por_bebida)
nombres_canciones = ["Like a Rolling Stone", "Satisfaction", "Imagine", "What's Going On", "Respect", "Good Vibrations"]
conteo_reproducciones = [78, 29, 44, 21, 89, 5]
reproducciones = {clave:valor for clave, valor in zip(nombres_canciones, conteo_reproducciones)}
print(reproducciones)
reproducciones.update({"Purple Haze": 1})
reproducciones.update({"Respect": 94})
print("Despues: ", reproducciones)
coleccion = {"The Best Songs": reproducciones, "Sunday Feelings": {}}
print(coleccion)
