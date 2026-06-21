<<<<<<< HEAD
# 🚑 Médix: Asistente Virtual para el Primer Respondiente (RAG)

Aplicación web interactiva basada en el patrón RAG (Retrieval-Augmented Generation) para realizar consultas inteligentes sobre atención prehospitalaria y primeros auxilios, utilizando como base de conocimiento el manual oficial de la Secretaría Distrital de Salud de Bogotá.

---

## 👤 Información del Proyecto
* **Nombre del Estudiante:** [Tu Nombre Completo Aquí]
* **Fecha:** [Día] de [Mes] de 2026

---

## 📖 Documento Seleccionado y Justificación

* **Documento:** *Manual del Primer Respondiente (4ª Edición)* - Secretaría Distrital de Salud de Bogotá, D.C. / Centro Regulador de Urgencias (CRU).
* **Justificación:** En situaciones de emergencia médica, accidentes de tránsito o incidentes domésticos, el tiempo y la exactitud de los primeros auxilios son fundamentales para mitigar riesgos de invalidez o muerte. Este documento oficial fue seleccionado porque estandariza los protocolos técnicos y de seguridad ciudadana aplicados bajo el ordenamiento legal colombiano. Implementar un sistema RAG sobre este manual garantiza que el asistente virtual formule respuestas estrictamente validadas por el sistema de emergencias de salud pública, eliminando alucinaciones críticas en procedimientos de soporte vital básico (como RCP o desatoramiento).

---

## 🎯 Persona Usuaria Objetivo y Caso de Uso

* **Persona Usuaria Objetivo:** Ciudadanos comunes (taxistas, amas de casa, estudiantes, profesores), brigadistas de emergencias en entornos empresariales, personal de apoyo institucional (Defensa Civil, Cruz Roja) o cualquier persona que presencie un incidente de salud en la vía pública o el hogar y desee auxiliar de forma responsable.
* **Caso de Uso:** Un brigadista escolar se enfrenta a un caso sospechoso de intoxicación o una quemadura en el laboratorio. En lugar de buscar manualmente entre las más de 40 páginas del documento digital bajo condiciones de estrés, ingresa a la interfaz web de "Médix", realiza una consulta directa en lenguaje natural y obtiene en segundos los pasos exactos de qué hacer, qué acciones evitar por completo y la referencia exacta del manual para dar continuidad inmediata a la cadena de auxilio mientras arriba una ambulancia.

---

## 🧪 Pruebas del Sistema (Preguntas y Respuestas)

A continuación se registran 5 interacciones reales del sistema procesadas por el LLM (`llama-3.1-8b-instant`) con la inyección de contexto y las citas bibliográficas estructuradas dinámicamente:

### Pregunta 1: ¿Qué es un ciclo de reanimación cardiorespiratoria (RCP) y cuántas compresiones se deben alcanzar por minuto?
* **Respuesta del Sistema:** Un ciclo de reanimación cardiorrespiratoria en adultos y niños consiste en realizar 30 compresiones combinadas con 2 ventilaciones (ciclos de 30x2). Se deben realizar 5 ciclos completos en un lapso de 2 minutos, intentando alcanzar una frecuencia constante de 100 compresiones por minuto.  
  **📌 Páginas consultadas del documento:** Pág. 28

### Pregunta 2: ¿Qué se debe hacer y qué NO se debe hacer ante una quemadura por calor?
* **Respuesta del Sistema:** Ante una quemadura por calor, lo que se debe hacer es enfriar la zona afectada utilizando agua corriente limpia durante un tiempo prolongado, de al menos 10 o 15 minutos, además de cubrir la lesión de forma ligera con un paño limpio o gasa estéril humedecida. Por el contrario, lo que NO se debe hacer bajo ninguna circunstancia es reventar las ampollas (flictenas) que se formen en la piel, ni intentar retirar la ropa que se encuentre adherida al tejido quemado.  
  **📌 Páginas consultadas del documento:** Pág. 22

### Pregunta 3: ¿Cuáles son las medidas para desobstruir la vía aérea en bebés (menores de 1 año) conscientes que muestran signos de atoramiento?
* **Respuesta del Sistema:** Si el bebé está consciente y se atora, primero abra la boca para verificar si se observa el cuerpo extraño y retirarlo con el dedo meñique (sin hacer barridos a ciegas). Si no lo ve, voltee al niño boca abajo sosteniéndolo firmemente y dé 5 golpes con el talón de la mano en la espalda (entre los omóplatos), manteniendo la cabeza más abajo que el cuerpo. Inmediatamente después, voltéelo boca arriba y realice 5 compresiones torácicas en el punto de cruce de la línea imaginaria entre las tetillas y el esternón. Continúe alternando estas maniobras hasta que expulse el objeto, el bebé respire/llore o quede inconsciente.  
  **📌 Páginas consultadas del documento:** Pág. 30

### Pregunta 4: ¿Qué elementos esenciales debe contener un botiquín de primeros auxilios y cómo se debe usar el esparadrapo y las vendas?
* **Respuesta del Sistema:** El botiquín de primeros auxilios debe contener antisépticos, esparadrapo (utilizado para fijar vendas y afrontar el borde de heridas), gasas (para limpiar y cubrir heridas o detener hemorragias pequeñas), vendas (que sirven para inmovilizar extremidades y realizar compresión en caso de hemorragias), vendas adhesivas (banditas/curitas) y agua limpia. Además, debe incluir elementos de protección y apoyo como guantes desechables, tapabocas, linterna, tijeras, termómetro, una lista de teléfonos de emergencia y el Manual del Primer Respondiente.  
  **📌 Páginas consultadas del documento:** Pág. 13, Pág. 14

### Pregunta 5: ¿Cuál es el tratamiento con medicamentos o antibióticos para curar la diabetes o regular la tensión arterial?
* **Respuesta del Sistema:** Lo siento, no puedo responder a preguntas fuera del contexto del manual del primer respondiente.  
*(Nota: El sistema mitiga la alucinación de forma correcta dado que el botiquín e instrucciones del manual prohíben explícitamente la autoformulación y especifican que el uso de medicamentos debe ser bajo estricta receta médica).*

---

## 🚀 Instrucciones para Ejecutar el Sistema

Sigue secuencialmente estos pasos para implementar el entorno virtual local y levantar el servidor web:

1. Clonar e ingresar al repositorio
```bash
git clone [https://github.com/tu-usuario/tu-repositorio-rag.git](https://github.com/tu-usuario/tu-repositorio-rag.git)
cd tu-repositorio-rag

2. Configurar el Entorno Virtual (Python 3)
En entornos Windows (PowerShell/CMD):

python -m venv venv
venv\Scripts\activate

3. Instalar dependencias requeridas
Ejecuta el gestor de paquetes para instalar todas las librerías necesarias definidas en las configuraciones del código fuente:

pip install -r requirements.txt

4. Configurar Variables de Entorno y Llaves API
Crea un archivo de texto plano en la raíz del proyecto llamado .env e introduce tus respectivos tokens privados de conexión remota:

HUGGINGFACEHUB_API_TOKEN=tu_token_de_huggingface_aqui
GROQ_API_KEY=gsk_tu_api_key_de_groq_aqui

5. Orden Obligatorio de Ejecución del Sistema
a. Construcción de la Base de Datos Vectorial (Poblamiento inicial)
Para leer el documento PDF, segmentarlo en fragmentos reducidos, generar los embeddings y guardarlos localmente, ejecuta el script principal:

python main.py

Espera a ver el mensaje de confirmación: 🎉 ¡Base de datos vectorial construida con éxito!. Verás que se habrá generado automáticamente la carpeta persistente local llamada chromadb/.

b. Inicialización de la Aplicación Web (Flask)
Una vez que la base vectorial contenga los datos indexados, arranca el servidor web que expone la API de interacción para el modelo de lenguaje Groq:

python app.py

El servidor iniciará en modo local. Abre tu navegador web e ingresa a la siguiente URL para interactuar con la interfaz gráfica de Médix:
👉 http://127.0.0.1:5000
=======
# App_chatbot_primer_respondiente
>>>>>>> 89a77fbd82f72c045ae04657528b9db5b1dfb883
