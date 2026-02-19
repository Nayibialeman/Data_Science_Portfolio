Analisis de Palabras Clave: Celulares Reacondicionados (ETL y NoSQL)
Este proyecto documenta el proceso de extraccion, transformacion, carga y visualizacion de datos provenientes de multiples fuentes SEO, centrados en el mercado de dispositivos moviles reacondicionados. Se utiliza MongoDB como motor de base de datos debido a su flexibilidad de esquema.

A. Justificacion de la Seleccion de la Coleccion
Conjunto de datos seleccionado
Nombre: Keywords de Celulares Reacondicionados.

Fuentes: Semrush, SimilarWeb, Ryte y Ahrefs.

Formato original: CSV.

Volumen: Aproximadamente 50,000 registros combinados.

Motivo de seleccion y Objetivos
El dataset permite analizar el comportamiento de busqueda en un mercado de alto crecimiento. El objetivo es identificar oportunidades de mercado, entender la competencia entre marcas y priorizar esfuerzos de posicionamiento SEO.

Relevancia de MongoDB
Se selecciono MongoDB por su estructura flexible (cada keyword puede tener multiples fuentes), su modelo basado en documentos que permite almacenar arrays de origen y su capacidad para manejar altos volumenes mediante pipelines de agregacion eficientes.

B. Descripcion del Tratamiento de Datos (Proceso ETL)
Extraccion: Carga de archivos CSV (semrush, similarweb, ryte, ahrefs) con normalizacion de columnas equivalentes.

Limpieza: * Normalizacion de keywords (minusculas y eliminacion de simbolos).

Correccion de errores de formato en valores numericos.

Filtrado tematico exclusivo para registros relacionados con "reacondicionado".

Transformacion: * Deteccion automatica de marca mediante reglas de negocio.

Generacion de ID unico mediante Hash SHA-256 (16 caracteres).

Consolidacion de metricas (promedio, maximo y total) por keyword.

Esquema Final del Documento
JSON
{
  "_id": "abc123def456",
  "kw": "iphone 13 reacondicionado",
  "m": "apple",
  "s": [
    {"n": "Semrush", "v": 15000},
    {"n": "Ahrefs", "v": 14500}
  ],
  "st": {
    "n": 2,
    "avg": 14750,
    "max": 15000,
    "tot": 29500
  }
}
C. Metodo de Carga al Cluster
Configuracion
Cluster: MongoDB Atlas (Nivel M0).

Metodo: Script Python utilizando la libreria PyMongo.

Justificacion del metodo
El uso de un script de Python permite realizar la limpieza y transformacion de forma atomica durante la carga, garantizando la idempotencia mediante operaciones de upsert y facilitando el manejo de excepciones en grandes volumenes de datos.

D. Diseño del Dashboard
El dashboard fue desarrollado en Power BI para responder preguntas estrategicas mediante las siguientes visualizaciones:

Tendencia del precio promedio por marca: Grafica de lineas para observar variaciones temporales.

Volumen de busqueda por vendedor y producto: Grafica de barras horizontales para identificar lideres de segmento.

Distribucion por categoria: Grafica de pastel para visualizar la proporcion de intenciones de busqueda.

Top 5 Keywords: Grafica de barras verticales centrada en los terminos de mayor demanda.

Conteo total de productos: Indicador KPI para dimensionar el universo de la coleccion.
