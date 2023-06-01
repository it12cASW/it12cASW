# Tabla de miembros

| Nombre miembro | Usuario de Taiga | Usuario GitHub |
| ------------------------- | ------------------------- | ------------------------- |
| Dimas Noguera | @dimas.noguera | DimasNP01 |
| Miguel Núñez | @miguelnunez | miguelnunez15 |
| Juan Clusellas | @jclusi | clusellas |
| Joan Martínez | @joanmartinezsoria | JoanMartinezSoria |

Aplicacion backend deployada en: https://it12casw-backend.fly.dev para el backend
Aplicacion frontend deployada en: https://it12casw.github.io/it12cASW para el frontend
# Más información

# COMANDOS

Borrar tablas y su contenido
###### python3 manage.py flush

Crear la migración de los modelos
###### python3 manage.py makemigrations

Importar la clase
###### from django.contrib.auth.models import <clase>

Entrar en la shell de la BD
###### python3 manage.py shell

Ver tablas de BD
###### python3 manage.py inspectdb

# COMO HACER DEPLOY

###### PASO 1: Installar el CLI de fly.io
- mirar esta pagina https://fly.io/docs/hands-on/install-flyctl/ 
###### PASO 2: Hacer login en fly desde la consola(solo necesario la primera vez)
- fly auth login
###### PASO 3: Hacer el deploy de la app (se debe estar en la carpeta backend para que funcione)
- fly deploy
###### PASO 4: Aplicar las migraciones en la app (se tiene que hacer cada vez que se hace un deploy)
- fly ssh console
- cd code
- python manage.py migrate
- exit


