from pymongo import MongoClient

# def instanciar()
# def add(frases: list())
# def inicializar() no haremos uso de lista de datos, sino de un fichero
# def consultar(n_frases: int)


def instanciacion():
    # Conexión con el motor de Mongo
    cliente_mongo = MongoClient('mongodb://mi-mongo:27017/')
    
    # Conexión con la BD (la crea si no existe)
    bd = cliente_mongo['bayeta']
    
    # Conexión con la tabla (llamada colección en Mongo)
    frases_auspiciosas = bd['frases_auspiciosas']
    
    return cliente_mongo, frases_auspiciosas
    
def inicializacion(datos):
    # Obtener instancias de motor y colección
    cliente_mongo, frases_auspiciosas = instanciacion()
    
    # Comprobamos que no se haya inicializado previamente
    if frases_auspiciosas.count_documents({}) == 0:
        # Inserción de datos desde el archivo
        with open(datos, 'r') as file:
            lines = file.readlines()
            frases_datos = [{"frase": line.strip()} for line in lines]
            frases_auspiciosas.insert_many(frases_datos)
    
    # Cerrar cliente
    cliente_mongo.close()

def consulta(n_frases):
    # Obtener instancias de motor y colección
    cliente_mongo, frases_auspiciosas = instanciacion()
    
    # Obtener frases aleatorias
    frases_aleatorias = list(frases_auspiciosas.aggregate([{'$sample': {'size': n_frases}}]))
    
    # Imprimir las frases
    for frase in frases_aleatorias:
        print(frase['frase'])

    # Cerrar cliente
    cliente_mongo.close()

    # Devolver las frases como una lista de strings
    return [frase['frase'] for frase in frases_aleatorias]

def insertar_datos(nuevas_frases):
    # Obtener instancias de motor y colección
    cliente_mongo, frases_auspiciosas = instanciacion()

    # Inserción de nuevas frases
    frases_nuevas = [{"frase": frase} for frase in nuevas_frases]
    frases_auspiciosas.insert_many(frases_nuevas)

    # Cerrar cliente
    cliente_mongo.close()

# Rutas a los archivos de datos y ejecución de funciones
ruta_archivo_datos = "frases.txt"
inicializacion(ruta_archivo_datos)

# Consulta de 3 frases aleatorias
#consulta(3)
