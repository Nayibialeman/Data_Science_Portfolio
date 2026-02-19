Sistema de Gestion de Tokens en MongoDB
Este script de Python realiza la inicializacion y gestion de saldos de criptoactivos en una base de datos local. El sistema permite registrar usuarios, asociar tarjetas de identificacion y asignar cantidades de tokens con marcas de tiempo precisas.

Requisitos del Entorno
Para ejecutar este script, debe asegurarse de cumplir con las siguientes configuraciones:

Base de Datos Local: Se requiere una instancia activa de MongoDB corriendo en localhost:27017. El script creara automaticamente la base de datos Token y la coleccion cripto.

Librerias de Python: Es necesario tener instalada la libreria pymongo para la conexion con el cluster.

Entorno de Ejecucion: Puede ejecutarse desde Visual Studio Code, Spyder, Google Colab o cualquier IDE compatible con Python 3.x.

Funcionalidades del Codigo
El script realiza las siguientes operaciones:

Conexion: Establece el enlace con el servidor local de MongoDB.

Simulacion de Datos: Inserta un conjunto inicial de registros para usuarios (ej. Carlos, Ana, Luis).

Estructura de Documento: Cada registro incluye:

Nombre del usuario.

Numero de tarjeta asociada.

Cantidad de tokens asignados (float).

Timestamp generado mediante datetime.utcnow().

Instrucciones de Uso
Asegurese de que el servicio de MongoDB este iniciado en su maquina local.

Instale las dependencias si es necesario:

Bash
pip install pymongo
Ejecute el archivo desde su terminal o IDE.

Verifique la carga de datos mediante un cliente como MongoDB Compass o la shell de Mongo.
