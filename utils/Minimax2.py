from .Arbol import Nodo

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

	def minimax(self, tablero):
		nodoPadre = Nodo()
		backup = tablero
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
			print(_restantes)
			for _r in _restantes:
				_y, _x = _r
				hijo_nodo_casilla_disponible = Nodo()
				hijo_nodo_casilla_disponible.set_root(nodo_casilla_disponible)
				nodo_casilla_disponible.agregar_hijo(hijo_nodo_casilla_disponible)
				hijo_nodo_casilla_disponible.set_x(_x)
				hijo_nodo_casilla_disponible.set_y(_y)
				_peso = self.evaluar_jugadas_posibles(copia_tablero, _y, _x, self.oponente) # Obtener la métrica del peso
				hijo_nodo_casilla_disponible.set_peso(_peso)
				# _copia_restantes[_y][_x] = self.oponente # Simula el tiro del oponente
		print('Tablero:\n')
		print(backup)
		print('\n')
		hijos = nodoPadre.obtener_hijos()
		print('Hijos raiz:\n')
		for hijo in hijos:
			hijo.show()
			nietos = hijo.obtener_hijos()
			print('Nietos =>')
			for n in nietos:
				n.show()
		print('\n')
		# vacias = self.obtener_casillas_vacias(tablero)
		# pesos = []  # tendrá una tupla (peso, y, x)
		# for casilla in vacias:
		# 	y, x = casilla
		# 	if self.maximiza:
		# 		peso = self.evaluar_jugadas_posibles(tablero, y, x, self.turno)
		# 	else:
		# 		peso = self.evaluar_jugadas_posibles(tablero, y, x, self.oponente)
		# 	pesos.append((peso, y, x))

		# # Si maximizar, entonces ordenar del mayor al menor
		# if self.maximiza:
		# 	print("Maximizando:\n\n")
		# 	pesos.sort(reverse=True, key=self.takeOnlyScore)
		# 	_peso, _y, _x = pesos[0]
		# 	print(f'Y => {_y}')
		# 	print(f'X => {_x}')
		# 	print(f'Peso => {_peso}')
		# 	return pesos[0]
		# else:
		# 	print("Minimizando:\n\n")
		# 	pesos.sort(key=self.takeOnlyScore)
		# 	_peso, _y, _x = pesos[0]
		# 	print(f'Y => {_y}')
		# 	print(f'X => {_x}')
		# 	print(f'Peso => {_peso}')
		# 	return pesos[0]
