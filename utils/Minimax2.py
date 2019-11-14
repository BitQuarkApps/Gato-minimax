from .Arbol import Nodo
import math

class Minimax:
	def __init__(self, my_id):
		self.turno = my_id
		if my_id == 0:
			self.oponente = 1
			self.maximiza = True
		else:
			self.oponente = 0
			self.maximiza = False

	def setMaximizar(self):
		"""
		True si toca maximizar.
		False si toca minimizar
		"""
		self.maximiza = not self.maximiza

	def obtener_casillas_vacias(self, tablero):
		vacias = []
		for col in range(3):
			for row in range(3):
				if tablero[col][row] == '-':
					vacias.append((col, row))
		return vacias

	def evaluar_jugadas_posibles(self, tablero, y, x, turno):
		"""
		Esta función regresa la cantidad de posibles formas de ganar,
		considerando Horizontalmente, verticalmente y en diagonal si
		es posible.

		Regresa un número entero.
		"""
		soluciones = 0
		if y == 0 and x == 0:
			# Evaluar desde la esquina superior izquierda de manera
			# horizontal
			if self.esta_libre(tablero, y+1, x, turno) and self.esta_libre(tablero, y+2, x, turno):
				soluciones += 1

			# Evaluar desde la esquina superior izquierda de manera
			# vertical
			if self.esta_libre(tablero, y, x+1, turno) and self.esta_libre(tablero, y, x+2, turno):
				soluciones += 1

			# Evaluar desde la esquina superior izquierda de manera
			# diagonal
			if self.esta_libre(tablero, y+1, x+1, turno) and self.esta_libre(tablero, y+2, x+2, turno):
				soluciones += 1

		if y == 1 and x == 0:
			if self.esta_libre(tablero, y-1, x, turno) and self.esta_libre(tablero, y+1, x, turno):
				soluciones += 1

			if self.esta_libre(tablero, y, x+1, turno) and self.esta_libre(tablero, y, x+2, turno):
				soluciones += 1

		if y == 2 and x == 0:
			if self.esta_libre(tablero, y-2, x, turno) and self.esta_libre(tablero, y-1, x, turno):
				soluciones += 1
			if self.esta_libre(tablero, y, x+1, turno) and self.esta_libre(tablero, y, x+2, turno):
				soluciones += 1
			if self.esta_libre(tablero, y-1, x+1, turno) and self.esta_libre(tablero, y-2, x+2, turno):
				soluciones += 1

		if y == 0 and x == 1:
			if self.esta_libre(tablero, y, x-1, turno) and self.esta_libre(tablero, y, x+1, turno):
				soluciones += 1
			if self.esta_libre(tablero, y+1, x, turno) and self.esta_libre(tablero, y+2, x, turno):
				soluciones += 1

		if y == 1 and x == 1:
			if self.esta_libre(tablero, y-1, x-1, turno) and self.esta_libre(tablero, y+1, x+1, turno):
				soluciones += 1
			if self.esta_libre(tablero, y, x-1, turno) and self.esta_libre(tablero, y, x+1, turno):
				soluciones += 1
			if self.esta_libre(tablero, y+1, x-1, turno) and self.esta_libre(tablero, y-1, x+1, turno):
				soluciones += 1
			if self.esta_libre(tablero, y-1, x, turno) and self.esta_libre(tablero, y+1, x, turno):
				soluciones += 1

		if y == 2 and x == 1:
			if self.esta_libre(tablero, y, x-1, turno) and self.esta_libre(tablero, y, x+1, turno):
				soluciones += 1
			if self.esta_libre(tablero, y-1, x, turno) and self.esta_libre(tablero, y-2, x, turno):
				soluciones += 1

		if y == 0 and x == 2:
			if self.esta_libre(tablero, y+1, x-1, turno) and self.esta_libre(tablero, y+2, x-2, turno):
				soluciones += 1
			if self.esta_libre(tablero, y, x-1, turno) and self.esta_libre(tablero, y, x-2, turno):
				soluciones += 1
			if self.esta_libre(tablero, y+1, x, turno) and self.esta_libre(tablero, y+2, x, turno):
				soluciones += 1

		if y == 1 and x == 2:
			if self.esta_libre(tablero, y-1, x, turno) and self.esta_libre(tablero, y+1, x, turno):
				soluciones += 1
			if self.esta_libre(tablero, y, x-1, turno) and self.esta_libre(tablero, y, x-2, turno):
				soluciones += 1

		if y == 2 and x == 2:
			if self.esta_libre(tablero, y-1, x, turno) and self.esta_libre(tablero, y-2, x, turno):
				soluciones += 1
			if self.esta_libre(tablero, y, x-1, turno) and self.esta_libre(tablero, y, x-2, turno):
				soluciones += 1
			if self.esta_libre(tablero, y-1, x-1, turno) and self.esta_libre(tablero, y-2, x-2, turno):
				soluciones += 1

		return soluciones

	def esta_libre(self, tablero, y, x, turno):
		if tablero[y][x] == '-':
			return True
		elif tablero[y][x] == turno:
			return True
		return False
 
	def takeOnlyScore(self, elem):
		return elem[0]

	def determinar_ganador(self, tablero, turno):
		if tablero[0][0] == turno and tablero[0][1] == turno and tablero[0][2] == turno:
			return True
		if tablero[1][0] == turno and tablero[1][1] == turno and tablero[1][2] == turno:
			return True
		if tablero[2][0] == turno and tablero[2][1] == turno and tablero[2][2] == turno:
			return True
		if tablero[0][0] == turno and tablero[1][1] == turno and tablero[2][2] == turno:
			return True
		if tablero[0][1] == turno and tablero[1][1] == turno and tablero[2][1] == turno:
			return True
		if tablero[0][2] == turno and tablero[1][2] == turno and tablero[2][2] == turno:
			return True
		if tablero[0][0] == turno and tablero[1][1] == turno and tablero[2][2] == turno:
			return True
		if tablero[0][2] == turno and tablero[1][1] == turno and tablero[2][0] == turno:
			return True
		return False

	def minimax(self, tablero, copia):
		nodoPadre = Nodo()
		copia_tablero = tablero
		# Iterar cada casilla disponible
		for casilla in self.obtener_casillas_vacias(copia_tablero):
			y, x = casilla
			nodo_casilla_disponible = Nodo()  # Crearmos un nuevo nodo
			nodo_casilla_disponible.set_root(nodoPadre)  # Le asignamos su padre
			nodoPadre.agregar_hijo(nodo_casilla_disponible)  # Agregamos el nodo hijo al padre
			nodo_casilla_disponible.set_x(x)  # Casilla disponible para efectuar un tiro [X]
			nodo_casilla_disponible.set_y(y) # Casilla disponible para efectuar un tiro [Y]

			peso = self.evaluar_jugadas_posibles(copia_tablero, y, x, self.turno) # Obtener la métrica del peso
			nodo_casilla_disponible.set_peso(peso) # Establecer el peso al nodo
			copia_tablero[y][x] = self.turno # Simulo mi tiro
			# Simular tiro del oponente con base en los hijos del nodo padre creado arriba
			_restantes = self.obtener_casillas_vacias(copia_tablero)
			for _r in _restantes:
				_y, _x = _r # X, Y de la casilla libre
				hijo_nodo_casilla_disponible = Nodo() # Nuevo nodo
				hijo_nodo_casilla_disponible.set_root(nodo_casilla_disponible) # Padre del nuevo nodo
				nodo_casilla_disponible.agregar_hijo(hijo_nodo_casilla_disponible) # Agregar el nuevo nodo como hijo del nodo anterior
				hijo_nodo_casilla_disponible.set_x(_x) # Ajuste de X
				hijo_nodo_casilla_disponible.set_y(_y) # Ajuste de Y
				_peso = self.evaluar_jugadas_posibles(copia_tablero, _y, _x, self.oponente) # Obtener la métrica del peso
				hijo_nodo_casilla_disponible.set_peso(_peso) # Fijar el peso para su evaluación
		hijos = nodoPadre.obtener_hijos()


		"""
		███╗   ███╗    ██╗    ███╗   ██╗    ██╗    ███╗   ███╗    ██╗    ███████╗     █████╗     ██████╗ 
		████╗ ████║    ██║    ████╗  ██║    ██║    ████╗ ████║    ██║    ╚══███╔╝    ██╔══██╗    ██╔══██╗
		██╔████╔██║    ██║    ██╔██╗ ██║    ██║    ██╔████╔██║    ██║      ███╔╝     ███████║    ██████╔╝
		██║╚██╔╝██║    ██║    ██║╚██╗██║    ██║    ██║╚██╔╝██║    ██║     ███╔╝      ██╔══██║    ██╔══██╗
		██║ ╚═╝ ██║    ██║    ██║ ╚████║    ██║    ██║ ╚═╝ ██║    ██║    ███████╗    ██║  ██║    ██║  ██║
		╚═╝     ╚═╝    ╚═╝    ╚═╝  ╚═══╝    ╚═╝    ╚═╝     ╚═╝    ╚═╝    ╚══════╝    ╚═╝  ╚═╝    ╚═╝  ╚═╝
		"""
		minimo = math.inf # Valor muy grande para la primera iteracion
		for hijo in hijos:
			nietos = hijo.obtener_hijos()
			for n in nietos:
				if n.get_peso() < minimo:
					minimo = n.get_peso()
			# En el caso de que el nodo no tenga hijos, se le asigna Infinito, lo cual estaría siendo
			# considerado como el mayor, para evitarlo, se deja el peso asignado por la métrica
			if minimo != math.inf:
				hijo.set_peso(minimo)  # Asignar el peso mínimo
				minimo = math.inf      # Reiniciar el mínimo a Infinito
		"""
		███╗   ███╗     █████╗     ██╗  ██╗    ██╗    ███╗   ███╗    ██╗    ███████╗     █████╗     ██████╗ 
		████╗ ████║    ██╔══██╗    ╚██╗██╔╝    ██║    ████╗ ████║    ██║    ╚══███╔╝    ██╔══██╗    ██╔══██╗
		██╔████╔██║    ███████║     ╚███╔╝     ██║    ██╔████╔██║    ██║      ███╔╝     ███████║    ██████╔╝
		██║╚██╔╝██║    ██╔══██║     ██╔██╗     ██║    ██║╚██╔╝██║    ██║     ███╔╝      ██╔══██║    ██╔══██╗
		██║ ╚═╝ ██║    ██║  ██║    ██╔╝ ██╗    ██║    ██║ ╚═╝ ██║    ██║    ███████╗    ██║  ██║    ██║  ██║
		╚═╝     ╚═╝    ╚═╝  ╚═╝    ╚═╝  ╚═╝    ╚═╝    ╚═╝     ╚═╝    ╚═╝    ╚══════╝    ╚═╝  ╚═╝    ╚═╝  ╚═╝
		"""

		maximo = -math.inf
		nodo_maximo = None
		for nodo in hijos:
			if nodo.get_peso() > maximo:  # Es el de mayor peso?
				maximo = nodo.get_peso()  # Asignar un nuevo peso
				nodo_maximo = nodo        # Acceso rápido al nodo mayor
		print(f"X => {nodo_maximo.get_x()}, Y => {nodo_maximo.get_y()}, PESO => {nodo_maximo.get_peso()}")
		return nodo_maximo.get_peso(), nodo_maximo.get_y(), nodo_maximo.get_x()