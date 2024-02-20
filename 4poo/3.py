class Jugador:
    juego=30
    def __init__(self):
        self.nombre=input("introduce nombre")
        self.puntaje=int(input("introduce puntos"))

    def __str__(self):
        cadena=self.nombre+"tiene un puntaje de",+str(self.puntaje)
        if self.puntaje>1000:
            cadena=cadena+" y es Experto"
        else:
            cadena=cadena+"y es principiante"
        return cadena

jugador1=Jugador()
jugador2=Jugador()
print(jugador1)
print(jugador2)
