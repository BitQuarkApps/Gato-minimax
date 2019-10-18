from math import inf as infinito
from random import choice

class Minimax:
	def __init__(self, turno):
		print('ready to beat its ass tho')
		self.turno = turno
		if turno == 0:
			self.oponente = 1
		else:
			self.oponente = 0

	def evaluar(self, tablero):
		if self.gana(tablero, self.turno):
			puntaje = +1
		elif self.gana(tablero, self.oponente):
			puntaje = -1
		else:
			puntaje = 0
		return puntaje

	def gana(self, tablero, turno):
		if tablero[0][0] == turno and tablero[0][1] == turno and tablero[0][2] == turno:
			return True
		if tablero[1][1] == turno and tablero[1][1] == turno and tablero[1][2] == turno:
			return True
		if tablero[2][1] == turno and tablero[2][1] == turno and tablero[2][2] == turno:
			return True
		if tablero[0][0] == turno and tablero[1][1] == turno and tablero[2][1] == turno:
			return True
		if tablero[0][1] == turno and tablero[1][1] == turno and tablero[2][1] == turno:
			return True
		if tablero[0][2] == turno and tablero[1][2] == turno and tablero[2][2] == turno:
			return True
		if tablero[0][0] == turno and tablero[1][1] == turno and tablero[2][2] == turno:
			return True
		if tablero[0][2] == turno and tablero[1][1] == turno and tablero[2][1] == turno:
			return True
		return False

	def game_over(self, tablero):
		return self.gana(tablero, self.turno) or self.gana(tablero, self.oponente)

	def casillas_vacias(self, tablero):
		vacias = []
		for row in range(3):
			for col in range(3):
				if tablero[row][col] == '-':
					vacias.append((row, col))  # X, Y ( Tupla )
		return vacias

	def movimiento_valido(self, x, y, tablero):
		if (x,y) in self.casillas_vacias(tablero):
			return True
		else:
			return False

	def tirar(self, x, y, tablero):
		if self.movimiento_valido(x, y, tablero):
			return x,y, True
		else:
			return x, y, False  # No puede tirar ahí

	def minimax(self, tablero, profundidad, turno):
		if turno == self.turno:
			mejor = [-1, -1, -infinito]
		else:
			mejor = [-1, -1, +infinito]

		if profundidad == 0 or self.game_over(tablero):
			puntaje = self.evaluar(tablero)
			return [-1, -1, puntaje]

		print(self.casillas_vacias(tablero))
		for casilla in self.casillas_vacias(tablero):
			x,y = casilla  # Tupla
			tablero[x][y] = turno
			puntaje = self.minimax(tablero, profundidad-1, -turno)
			tablero[x][y] = '-'
			puntaje[0], puntaje[1] = x, y

			if turno == self.turno:
				if puntaje[2] > mejor[2]:
					mejor = puntaje
			else:
				if puntaje[2] < mejor[2]:
					mejor = puntaje
		return mejor

	def mi_turno(self, tablero):
		profundidad = len(self.casillas_vacias(tablero))
		print(profundidad)
		if profundidad == 0 or self.game_over(tablero):
			return

		if profundidad == 9:
			# Como es el primer tiro, elige una casilla de las 9 al azar, tanto para X como para Y
			x = choice([0, 1, 2])
			y = choice([0, 1, 2])
		else:
			movimiento = self.minimax(tablero, profundidad, self.turno)
			print(movimiento)
			x, y = movimiento[0], movimiento[1]
		return x, y