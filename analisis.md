1- 
Es el método por el cual se proporciona caracteristicas generales y unicas a cada juego en el catalogo, con el obejtivo de crear una forma de poder separar en menores grupos al extenso catalogo y así realizar busquedas más eficientes, ademas de poder ofrecer titulos que compartan caracteristicas que sean del interes del usuario.

Para la clase "Catalogo" como sus invariantes a "version" (aunque no se muestre explicitamente al usuario, si la version que emplea no es la misma a la actualmente manejada, se debe mostrar un mensaje pidiendo la actualización ademas de evitar usar algún juego hasta que realize la actualización) , "año_publicacion" (que no puede tener fechas imposibles o del futuro) y "empresa_desarrolladora" (no puede estar vacias, aunque la opcion "indie" terminaria aglomerando a la mayoria de empresas menores o que realizaron solo un juegos para que sean derivados a una sublista y así darle cierta prioridad a las empresas de mayor rendimiento economico a la plataforma).

En la clase "Juego" puede tener como invariables "id_juego" (calculado como S*3 + hora_exacta_milisegundo_publicado ), "nombre" (no se pueden repetir nombres), y "categorias" (debe pertenecer al menos a una con la opcion "otros" en caso de no ser apropiadamente definida en una categoria preexistente)
Por el lado de la clase "Usuario" puede tener a "id_identificacion" (definido como "id_juego", ya que ambos numeros terminarian definiendo diferentes elementos), "email" (cuenta unica por mail), "historial" (puede estar vacia e incluso borrar parte del historial, pero nunca ser negativa) y "saldo" (no puede tener un saldo negativo).
Mientras que en "Reseña" las invariables pueden ser "tipo" (debe decir si es positiva o negativa), "tiempo_jugado" (no puede dar una reseña alguien con tiempo menor a S/1200 horas), y "fecha_realizada" (no puede haber reseñas previas al lanzamiento del juego)

Este encapsulamiento de caracteristicas permiten que se filtre de forma logica las distintas clases y proporcionar una depuración de los resultados al navegar sobre ellas y evita duplicados o caracteristicas que no sean realistas.

2-






