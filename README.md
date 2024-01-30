Para ejecutar esta aplicación, hemos usado un entorno virtual de Python:

python3 -m venv pps_venv_01

Para instalar las dependencias correspondientes exportadas al fichero "requirements.txt", ejecutar:

pip install -r requirements.txt

Para ejecutar la aplicación, ejecutar:

python3 app.py

La aplicación web ahora tiene una "base de datos" con frases auspiciosas. Podemos acceder a estas ejecutando el script de app.py como se ha mostrado antes.

Ahora, en nuestro navegador, accederemos a 'http://localhost:5000/frotar/<n_frases>', donde '<n_frases>' es el número de frases auspiciosas que queremos ver.
