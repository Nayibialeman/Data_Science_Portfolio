Sistema de Gestion de Activos: Blockbuster NFT
Este proyecto implementa un sistema de control de inventario y rentas para una tienda de peliculas (tipo Blockbuster) utilizando el concepto de identificadores unicos (NFT). Cada pelicula es tratada como un activo digital unico dentro de una cadena de registros inmutable, permitiendo un seguimiento preciso de su estado, cliente y fechas de vencimiento.

Caracteristicas del Sistema
El sistema ofrece una interfaz interactiva dividida en cinco modulos principales:

Registro de pelicula: Alta de nuevos activos mediante un ID unico de Token (NFT).

Gestion de Rentas: Asignacion de peliculas a clientes con calculo automatico de fechas de vencimiento.

Devolucion: Actualizacion del estado del activo para reingreso al inventario.

Historial General: Visualizacion de todos los registros y estados de la base de datos.

Alertas de Vencimiento: Panel de control para identificar rentas proximas a vencer en un margen de 3 dias.

Requisitos de Instalacion
Para ejecutar este proyecto de forma local, es necesario instalar las siguientes dependencias de Python:

Bash
pip install streamlit pymongo pandas
Ademas, se requiere:

MongoDB Local: El script se conecta a mongodb://localhost:27017/.

Base de Datos: Se utiliza la base de datos denominada Token y la coleccion nofung.

Instrucciones de Ejecucion
Este proyecto utiliza Streamlit para el despliegue del dashboard. Siga estos pasos para correr el archivo:

Abra su terminal o consola desde Visual Studio Code o Spyder.

Navegue hasta la carpeta donde se encuentra el archivo blockbuster_nft.py.

Ejecute el siguiente comando:

Bash
streamlit run blockbuster_nft.py
Nota: Al ejecutar el comando, se abrira automaticamente una pestaña en su navegador con la interfaz grafica del sistema.

Tecnologias Utilizadas
Frontend: Streamlit (Dashboard interactivo).

Base de Datos: MongoDB (NoSQL para almacenamiento de documentos NFT).

Procesamiento de Datos: Pandas (Para la gestion de tablas y fechas).

Lenguaje: Python 3.x.
