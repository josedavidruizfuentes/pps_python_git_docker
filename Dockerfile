# Fase de resolución de dependencias
FROM python:slim AS builder

# Directorio de trabajo
WORKDIR /app

# Copiar los archivos necesarios para instalar las dependencias
COPY ./requirements.txt .

# Instalar las dependencias
RUN pip install -r requirements.txt

# Fase de ejecución
FROM builder AS runner

# Directorio de trabajo
WORKDIR /app2

# Copiar los archivos necesarios para ejecutar la aplicación
COPY --from=builder /app/ /app2/

COPY . .

# Exponer el puerto en el que la aplicación Flask está escuchando
EXPOSE 5000

CMD ["python", "app.py"]
