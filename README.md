# RETO FINAL - API LFG

Es el proyecto final del curso de Backend Pyhton Online de [GeeksHubs Academy](https://github.com/GeeksHubsAcademy)

Consiste en crear una aplicacion web LFG que permite crear grupos de videojuegos, un lugar donde los jugadores puedan comunicarse


## TECNOLOGIAS 🔧 

* **PostgreSQL**
* **Python (3.6 o superior)**
* **VirtualEnv propio**
* **Django para la estructura de proyecto**
* **Django Rest Framework encargado de la serialización de objetos JSON**
* **JWT**



## OBJETIVOS 📋

* **Requisitos funcionales para la aplicación(explicados mas abajo)**
* **Registro de usuarios**
* **Login de usuarios, auth + token**
* **CRUD de los diferentes modelos**



## VAMOS A ELLO ⚙️ 🚀

### Para empezar hemos creado los juegos disponibles desde el panel de admin entrando con el superuser
📌![imagen](https://github.com/movidasgori/LFG/blob/a4b6fbfdfe9909a58c44a8222a84acc449a80136/IMAGENES/lista%20juegos.JPG)
```
http://127.0.0.1:8000/JUEGOS/
```

### Aqui podemos ver la pagina del inicio
![imagen](https://github.com/movidasgori/LFG/blob/4eb79d063fa8534b0537c8e0eb0fadf874ad6e66/IMAGENES/inicio.JPG)
📌
```
http://127.0.0.1:8000
```


### 1.  Los usuarios se tienen que poder registrar a la aplicación, estableciendo un usuario/contraseña.

📌![imagen](https://github.com/movidasgori/LFG/blob/a3f6cf2974a7c0ab9786cadfa32acaad6c1389d6/IMAGENES/registro.JPG)
```
http://127.0.0.1:8000/registration/
```

### Se obtiene la KEY
![imagen](https://github.com/movidasgori/LFG/blob/a3f6cf2974a7c0ab9786cadfa32acaad6c1389d6/IMAGENES/key.JPG)


### 2.  Los usuarios tienen que autenticarse a la aplicación haciendo login.
📌![imagen](https://github.com/movidasgori/LFG/blob/a4b6fbfdfe9909a58c44a8222a84acc449a80136/IMAGENES/login.JPG)
```
http://127.0.0.1:8000/registration/
```

### 3.  Los usuarios tienen que poder crear Partys (grupos) por un determinado videojuego.
📌![imagen](https://github.com/movidasgori/LFG/blob/a4b6fbfdfe9909a58c44a8222a84acc449a80136/IMAGENES/creacion%20partida%202.JPG)
```
http://127.0.0.1:8000/PARTYS/
```


### 4.  Los usuarios tienen que poder buscar Partías seleccionando un videojuego.
📌![imagen](https://github.com/movidasgori/LFG/blob/a4b6fbfdfe9909a58c44a8222a84acc449a80136/IMAGENES/partys%20list.JPG)
```
http://127.0.0.1:8000/PARTYS/
```


### 5.  Los usuarios pueden entrar y salir de una Party.
📌![imagen](https://github.com/movidasgori/LFG/blob/4eb79d063fa8534b0537c8e0eb0fadf874ad6e66/IMAGENES/entrar%20party.JPG)
```
http://127.0.0.1:8000/PARTY%20PLAYERS/
```

### (Se saca al jugador de la PARTY por medio de panel de superuser)
📌![imagen](https://github.com/movidasgori/LFG/blob/4eb79d063fa8534b0537c8e0eb0fadf874ad6e66/IMAGENES/salir%20party.JPG)
```
http://127.0.0.1:8000/admin/myapi/partyplayers/
```

### 6.  Los usuarios tienen que poder enviar mensajes a la Party.
📌![imagen](https://github.com/movidasgori/LFG/blob/4eb79d063fa8534b0537c8e0eb0fadf874ad6e66/IMAGENES/mensaje%20party.JPG)
```
http://127.0.0.1:8000/PARTYS%20CHAT/
```

### (Se puede editar el mensaje buscando el id del mensaje)
📌![imagen](https://github.com/movidasgori/LFG/blob/f6b0fe643b0bdf524505391b9099b13aed5f3e87/IMAGENES/editar%20mensaje.JPG)
```
http://127.0.0.1:8000/PARTYS%20CHAT/5
```

### 7.  Los mensajes que existan a una Party se tienen que visualizar como un chat común.
📌![imagen](https://github.com/movidasgori/LFG/blob/f6b0fe643b0bdf524505391b9099b13aed5f3e87/IMAGENES/chat.JPG)
```
http://127.0.0.1:8000/PARTYS%20CHAT/
```

### 8.  Los usuarios pueden introducir y modificar sus datos de perfil, por ejemplo, su usuario de Steam.
📌![imagen](https://github.com/movidasgori/LFG/blob/f6b0fe643b0bdf524505391b9099b13aed5f3e87/IMAGENES/modificar%20datos%20user.JPG)
```
http://127.0.0.1:8000/user/
```

### 9.  Los usuarios tienen que poder hacer logout de la aplicación web.
📌![imagen](https://github.com/movidasgori/LFG/blob/f6b0fe643b0bdf524505391b9099b13aed5f3e87/IMAGENES/logout.JPG)
```
http://127.0.0.1:8000/logout/
```





## Autor ✒️

* **Grigory Kazarin**
