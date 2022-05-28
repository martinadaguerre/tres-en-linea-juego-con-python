from re import I, X
from jugador import JugadorComputadora, JugadorHumano


class TaTeTi:
    def __init__(self):
        self.tablero = [' ' for _ in range(9)]  #uso una lista simple para representar el tablero de 3x3
        self.ganador_actual = None  #llevar registro del ganador

    def print_tablero(self):
        for row in [self.tablero[i*3:(i+1)*3]for i in range(3)]:
            print(' | '+ ' | '.join(row)+ ' | ')

    @staticmethod
    def print_tablero_nums():
        # 0|1|2 etc dice que numero corresponde a cada box
        numero_tablero = [[str(i)for i in range(j*3, (j+1)*3)]for j in range(3)]
        for row in numero_tablero : 
            print(' | '+ ' | '.join(row)+ ' | ')

    def movimientos_disponibles(self): 
        return [i for i, espacio in enumerate(self.tablero)if espacio == ' ' ]

    def cuadrados_vacios(self):
        return ' ' in self.tablero

    def cant_cuadrados_vacios(self):
        return self.tablero.count(' ')   

    def hacer_movimiento(self, cuadrado, letra):
        if self.tablero[cuadrado] == ' ':
            self.tablero[cuadrado] == letra
            if self.ganador(cuadrado, letra):
                self.ganador_actual = letra
            return False

    def ganador(self, cuadrado, letra):
        # se gana cuando hace 3 en linea. puede ser vertical, horizontal o diagonal
        #Chequeamos la fila (row)
        row_ind = cuadrado //3
        row = self.tablero[row_ind*3 : (row_ind+1)*3]
        if all([espacio == letra for espacio in row]):
            return True
        # Chequeamos la columna
        col_ind = cuadrado % 3
        # ojo aca arriba puede haber un error y que sea // en vez de 
        column = [self.tablero[col_ind+i*3]for i in range(3)]
        if all([espacio == letra for espacio in column]):
            return True
        # chequear las DIAGONALES
        if cuadrado % 2 == 0:
            diagonal1 = [self.tablero[i]for i in [0, 4, 8]] # diagonal de izquierda a derecha
            if all([espacio == letra for espacio in diagonal1]):
                return True
            diagonal2 = [self.tablero[i]for i in [2, 4, 6]] # diagonal de derecha a izquierda
            if all([espacio == letra for espacio in diagonal2]):
                return True

def jugar(juego, jugador_x, jugador_o, print_juego= True):
        if print_juego:
            juego.print_tablero_nums()
        letra = 'x'
        while juego.cuadrados_vacios():
            if letra == 'O':
                cuadrado = jugador_o.movimiento(juego) 
            else: 
                 cuadrado = jugador_x.movimiento(juego) 
        #defino una funcion para hacer un movimiento:
        if juego.hacer_movimiento(cuadrado, letra):
            if print_juego:
                print (letra + f'hace un movimiento hacia el cuadrado{cuadrado}')
                juego.print_tablero()
                print('') # linea vacia
        # devuelve el ganador del juego si es que lo hay
            if juego.ganador_actual:
               if print_juego:
                   print(letra + 'es el ganador del juego!')
                   return letra
        # ahora hay que alternar las letras para que le toque un turno a cada player
               letra= 'O' if  letra == 'x' else 'x' 
               if print_juego:
                   print('It\'s a tie')

if __name__ == '__main__':
    jugador_x = JugadorHumano('X')
    jugador_o = JugadorComputadora('O')
    t = TaTeTi()
    jugar(t, jugador_x, jugador_o, print_juego= True)














