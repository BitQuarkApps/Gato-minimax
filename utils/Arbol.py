class Nodo:
	def __init__(self):
		"""
		Clase que contendrá nodos con:
		Una casilla de tiro para el tablero del gato.
		Un peso
		"""
		self.children = []
		self.root = None
		self.x = None
		self.y = None
		self.peso = 0

	def set_root(self, nodo):
		"""
		Fijar el nodo raiz del arbol
		"""
		self.root = nodo
	
	def set_x(self, x):
		"""
		Fijar el valor de x
		"""
		self.x = x

	def set_y(self, y):
		"""
		Fijar el valor de y
		"""
		self.y = y
	
	def agregar_hijo(self, nodo):
		"""
		Agregar un nodo como hijo
		"""
		self.children.append(nodo)

	def obtener_hijos(self):
		"""
		Obtener todos los nodos hijos
		"""
		return self.children

	def set_peso(self, peso):
		self.peso = peso

	def show(self):
		print(f'X => {self.x}, Y => {self.y}, peso => {self.peso}')