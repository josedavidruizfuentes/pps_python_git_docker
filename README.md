Para ejecutar esta aplicación, hemos usado un entorno virtual de Python:

python3 -m venv pps_venv_01

Para instalar las dependencias correspondientes exportadas al fichero "requirements.txt", ejecutar:

pip install -r requirements.txt

Para ejecutar la aplicación, ejecutar:

python3 app.py

La aplicación web ahora tiene una "base de datos" con frases auspiciosas. Podemos acceder a estas ejecutando el script de app.py como se ha mostrado antes. 

Ahora, en nuestro navegador, accederemos a 'http://localhost:5000/frotar/<n_frases>', donde '<n_frases>' es el número de frases auspiciosas que queremos ver.

Si queremos desplegar la aplicación en un contenedor de Docker, debemos hacer uso del Dockerfile. Para ello, lo primero es crear la imagen. Dentro de este directorio, ejecutar:

docker build -t bayeta-app .

Levantamos el contenedor con esa imagen y mapeamos el puerto 5000 del contenedor al 5000 de nuestra máquina:

docker run -p 5000:5000 bayeta-app

Ya solo queda acceder al navegador web del mismo modo que antes: 'http://localhost:5000/frotar/<n_frases>', donde '<n_frases>' es el número de frases auspiciosas que queremos ver.

Ahora, hemos añadido a nuestra aplicación una base de datos MongoDB, la cual se aloja en un contenedor de Docker. Nuestra aplicación se va a conectar a esta base de datos para obtener las frases auspiciosas. Para ello, primero debemos crear una red de Docker para que los contenedores puedan comunicarse entre sí y luego levantar el contenedor de MongoDB:

docker network create mongo_network
docker run -d --network mongo_network -p 27017:27017 --name mi-mongo mongo

En el caso de que ya tengamos una imagen anterior de nuestra aplicación, debemos eliminarla y volver a crearla con la nueva configuración de la base de datos. Para ello, ejecutamos:

docker rmi bayeta-app
docker build -t bayeta-app .

Para levantar nuestra aplicación, debemos hacerlo en la misma red de Docker que la base de datos. Para ello, ejecutamos:

docker run -d --network mongo_network -p 5000:5000 bayeta-app

De nuevo, accedemos a: 'http://localhost:5000/frotar/<n_frases>', donde '<n_frases>' es el número de frases auspiciosas que queremos ver.

