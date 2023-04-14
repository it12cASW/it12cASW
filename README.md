# Tabla de miembros

| Nombre miembro | Usuario de Taiga | Usuario GitHub |
| ------------------------- | ------------------------- | ------------------------- |
| Dimas Noguera | @dimas.noguera | DimasNP01 |
| Miguel Núñez | @miguelnunez | miguelnunez15 |
| Juan Clusellas | @jclusi | clusellas |
| Joan Martínez | @joanmartinezsoria | JoanMartinezSoria |

Aplicacion deployada en: it12casw.fly.dev
# Más información

### Para ejecutar la parte de frontend
- Entrar en directorio /frontend
- Ejecutar # npm start
- Poner la dirección que nos da en el navegador

### Para ejecturar el proyecto de backend
- Entrar en el directorio /backend
- Ejecutar # python3 manage.py runserver

Ahora podremos abrir la ventana del cliente ( react ) con la URL que nos del React 'http://localhost:3000' y desde ahi ejecutaremos la aplicación.

# COMANDOS

###### Borrar tablas y su contenido
- python3 manage.py flush

###### Crear la migración de los modelos
- python3 manage.py makemigrations

###### Aplicar la migración a la BD
- python3 manage.py migrate

###### Entrar en la shell de la BD
- python3 manage.py shell

###### Importar la clase
- from django.contrib.auth.models import <clase>

###### Ver contenido de las tablas
- <clase>.objects.all()

###### Ver tablas de BD
- python3 manage.py inspectdb
