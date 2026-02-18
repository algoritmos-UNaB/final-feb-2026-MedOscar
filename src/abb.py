def insertar_juego(self,juego):
  if juego not in self.juegos:
    self.juegos.append(juego)
    return True
  return False
S = (019 + 18) % 17 + 3

