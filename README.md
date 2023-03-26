# ASW_22_23_front
Frontend de la app de Taiga de ASW

Para ejecutar el proyecto hay que hacer lo siguiente:
- Entrar en directorio /frontend
- Ejecutar # npm start
- Poner la dirección que nos da en el navegador

- Entrar en el directorio /backend
- Ejecutar # python3 manage.py runserver

Ahora podremos abrir la ventana del cliente ( react ) con la URL que nos del React 'http://localhost:3000' y desde ahi ejecutaremos la aplicación.


- Podemos comprobar en POSTMAN que las peticiones funcionan correctamente.

- URLs de peticiones
    - 


COMANDOS
- Borrar tablas y su contenido
# python3 manage.py flush

- Crear la migración de los modelos
# python3 manage.py makemigrations

- Aplicar la migración a la BD
# python3 manage.py migrate

- Entrar en la shell de la BD
# python3 manage.py shell

- Importar la clase
# from django.contrib.auth.models import <clase>

- Ver contenido de las tablas
# <clase>.objects.all()

- Ver tablas de BD
# python3 manage.py inspectdb


