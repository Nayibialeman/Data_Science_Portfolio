🛡️ Chatbot de Incidencia Delictiva en México
Este es un asistente virtual desarrollado con el framework Rasa diseñado para consultar y visualizar información pública sobre delitos en México. El bot procesa datos estadísticos desde un archivo Excel y responde de forma conversacional a las dudas del usuario.

🚀 Características.
Procesamiento de Excel: Uso de pandas en las Custom Actions para filtrar datos por estado, municipio o tipo de delito.
Interfaz conversacional: Capacidad para entender intenciones como saludar, consultar estadísticas y agradecer.

📂 Estructura del Proyecto
/actions: Contiene actions.py, donde reside la lógica para leer el Excel.

/data: Archivos nlu.yml, rules.yml y stories.yml para el entrenamiento del modelo.

requirements.txt: Dependencias necesarias (Rasa, Pandas, Openpyxl).

data_delitos.xlsx: El archivo fuente con las cifras de incidencia.

🛠️ Instalación y Configuración
1. Clonar el repositorio y crear entorno virtual
Bash
git clone <tu-repositorio-url>
cd <nombre-del-directorio>
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
2. Instalar dependencias
Bash
pip install -r requirements.txt
3. Entrenar el modelo
Bash
rasa train
🏃 Ejecución
Para probar el chatbot, necesitas ejecutar dos servicios en terminales separadas:

Terminal 1: Servidor de Acciones (Custom Actions)
Este servidor es el que permite al bot leer tu archivo Excel.

Bash
rasa run actions
Terminal 2: Interfaz del Chat

Bash
rasa shell
