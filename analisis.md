1- 
Es el método por el cual se proporciona caracteristicas generales y unicas a cada juego en el catalogo, con el obejtivo de crear una forma de poder separar en menores grupos al extenso catalogo y así realizar busquedas más eficientes, ademas de poder ofrecer titulos que compartan caracteristicas que sean del interes del usuario.
Se puede emplear para la clase "Catalogo" como sus invariantes "categoria", "año_publicacion" y "empresa_desarrolladora" (aunque la opcion "indie" terminaria aglomerando a la mayoria de empresas menores o que realizaron solo un juegos para que sean derivados a una sublista y así darle cierta prioridad a las empresas de mayor rendimiento economico a la plataforma).
En la clase "Juego" puede tener como invariables "id_juego", "nombre", y "popularidad" (expresada de cero a cinco que varian según el promedio de votos por cada usuario le haya asignado).
Por el lado de la clase "Usuario" puede tener a "id_identificacion", "email" y "historial" como invariables
Mientras que en "Reseña" las invariables pueden ser "tipo" (generalmente para decir si es positiva o negativa), "tiempo_jugado" (para que aquellos con mayor tiempo a S sean de mayor visibilidad respecto a otras reseñas), "fecha_realizada" (afecta mucho ya que son habituales las actualizaciones que corrigen errores post reseña) y "valoracion" (similar a la popularidad, donde los otros usuarios determinan que tan de acuerdo están con la reseña).


