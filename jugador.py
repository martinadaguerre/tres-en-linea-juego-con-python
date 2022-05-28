from lib2to3.pytree import LeafPattern
import math 
import random

class jugador: 
    # creo una clase 'jugador' que luego se lo aplico a las diferentes sub clases
    def __init__(self, letra):
         #letras son X y O en este juego
         self.letra = letra
    #establezco la funcion movimiento para que todos los jugadores jueguen su siguiente movimiento
    def movimiento(self,juego):
        pass
class JugadorComputadora(jugador):
    def __init__(self, letra):
        super().__init__(letra)
    def movimiento(self, juego): 
    #establezco que el jugador automatico elija un cuadrado aleatorio dentro de los disponibles
       cuadrado = random.Random.choice(juego.movimientos_disponibles())
       return cuadrado
class JugadorHumano(jugador):
    def __init__(self, letra):
        super().__init__(letra)
    def movimiento(self, juego):
    # establezco que el jugador humano pueda ingresar mediante un input el cuadrado que desea 
        cuadrado_valido = False
        val = None
        while not cuadrado_valido:
            cuadrado = input(self.letra + '\`s turn. ingresar movimiento 9-0: ' )
            try:
                val = int(cuadrado)
                if val not in juego.movimientos_disponibles():
                    raise ValueError
                cuadrado_valido = True 
            except ValueError : print('Cuadrado Invalido. Intente de nuevo.')   
        return val




