from tkinter import ttk, font
from tkinter import messagebox
from utils.Minimax import Minimax
from anytree import Node
from tkinter import *
import websocket
import random
import time
import json

my_id = None  # Puede tomar 0 o 1
server = 'ws://localhost:9000'
agente = None

def do_minimax(tableroActual):
	x, y = agente.mi_turno(tableroActual)
	return x, y

# Funciones del websocket
def on_message(ws, message):
	global my_id
	global agente
	message = json.loads(message)
	print(message)

	# Si el message tiene un id significa que todavia no ha iniciado el juego
	if "id" in message:
		if message["id"] == -1:
			print("ya no hay cupo")
			messagebox.showinfo("Error al ingresar a la sala", "Ya no hay cupo.")
			ws.close()
		else:
			print("mi id es: " + str(message["id"]))
			my_id = message["id"]
			tablero = [['-' for _ in range(3)] for _ in range(3)]
			agente = Minimax(my_id)

	# Si no tiene id siginifica que el juego ya inicio
	else:
		if "empate" in message:
			print("Fue un empate")
			ws.close()
		elif "ganador" in message:
			print("El ganador es : " + str(message["ganador"]))
			messagebox.showinfo("¡Ganador!", "El ganador es : " + message["ganador"])
			ws.close()
		else:
			turno = message["turno"]
			matriz = message["matriz"]
			print("mi turno id: " + str(my_id) + " " + str(turno))
			x, y = do_minimax(matriz)
			ganador = agente.gana(matriz, my_id)
			# ganador = agente.puede_ganar(matriz, my_id)
			# agente.update_tablero(matriz)
			print("\n")
			for row in matriz:
				print(f"{row}")
			print("\n")

			# envio mi posicion de tiro
			my_message = json.dumps({"x": x, "y": y, "ganador": ganador, "id": my_id})
			ws.send(my_message)
			# proceso de acuerdo a mis reglas
			# minimax, x, y = agente.minimax()
			# if minimax != None and x != None and y != None:
			# 	print(f'Minimax => {minimax}, x => {y}, y => {x}')
			# 	# envio mi posicion de tiro
			# 	my_message = json.dumps({"x": y, "y": x, "ganador": ganador, "id": my_id})
			# 	ws.send(my_message)

def on_error(ws, error):
	print(error)

def on_close(ws):
	print("### Se ha cerrado el servidor ###")

def on_open(ws):
	def run(*args):
		print("Conectado...")

if __name__ == "__main__":
	websocket.enableTrace(True)
	print(server)
	ws = websocket.WebSocketApp(server, on_message=on_message, on_error=on_error, on_close=on_close)
	ws.on_open = on_open
	ws.run_forever()
	# tablero = [['-' for _ in range(3)] for _ in range(3)]
	# root = Node(tablero)  # Tablero inicial
	# print(root.casillasVacias())
