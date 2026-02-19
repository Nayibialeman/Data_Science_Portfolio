Sistema de Tokenizacion de Obras de Arte (NFT)
Este proyecto es una aplicacion de escritorio basada en web que permite la creacion, registro y transferencia de Tokens No Fungibles (NFT) representativos de obras de arte. El sistema asigna un identificador unico universal (UUID) a cada pieza, garantizando la trazabilidad de la propiedad y el historial de transacciones.

Caracteristicas Principales
Minteo de NFTs: Registro de nuevas obras incluyendo titulo, artista, fecha de creacion y propietario inicial.

Soporte Multimedia: Capacidad para adjuntar y visualizar archivos de imagen (JPG, PNG) y archivos de audio (MP3) vinculados al token.

Historial de Transacciones: Registro inmutable de los cambios de propietario (de/hacia) con marcas de tiempo precisas.

Persistencia de Datos: Implementacion de almacenamiento local mediante archivos binarios (.pkl), lo que permite conservar los registros aun despues de cerrar la aplicacion.

Requisitos del Sistema
Para la ejecucion local, se requiere:

Librerias de Python: Instalacion de Streamlit.

Bash
pip install streamlit
Base de Datos Local: El sistema utiliza un archivo llamado nft_data.pkl generado automaticamente para actuar como base de datos persistente.

Instrucciones de Ejecucion
Para poner en marcha el dashboard interactivo:

Abra una terminal o CMD.

Navegue hasta la carpeta donde se encuentra el archivo Arte Tokerizado2.py.

Ejecute el siguiente comando:

Bash
streamlit run "Arte Tokerizado2.py"
Estructura del Token (Clase ArtworkNFT)
Cada objeto de arte tokenizado contiene la siguiente estructura de datos:

Token ID: Generado automaticamente mediante uuid4.

Metadata: Informacion tecnica fija (resolucion, formato, fecha de minteo).

Multimedia: Almacenamiento en bytes de la imagen y el audio cargado.

Transaction History: Una lista de diccionarios que rastrea el flujo de propiedad.

Tecnologias Utilizadas
Frontend: Streamlit.

Logica de Identidad: Libreria uuid de Python.

Persistencia: Libreria pickle para serializacion de objetos.

Entornos recomendados: Visual Studio Code o Spyder.
