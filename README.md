<<<<<<< HEAD
# Médix: Asistente Virtual para el Primer Respondiente

Aplicación web interactiva basada en el patrón RAG (Retrieval-Augmented Generation) para realizar consultas inteligentes sobre atención prehospitalaria y primeros auxilios, utilizando como base de conocimiento el manual oficial de la Secretaría Distrital de Salud de Bogotá.

---

##  Información del Proyecto
* **Nombre del Estudiante:** Juliana Suarez
* **Fecha:** [21] de [06] de 2026

---

##  Documento Seleccionado y Justificación

* **Documento:** *Manual del Primer Respondiente (4ª Edición)* - Secretaría Distrital de Salud de Bogotá, D.C. / Centro Regulador de Urgencias (CRU).
* **Justificación:** En situaciones de emergencia médica, accidentes de tránsito o incidentes domésticos, el tiempo y la exactitud de los primeros auxilios son fundamentales para mitigar riesgos de invalidez o muerte. Este documento oficial fue seleccionado porque estandariza los protocolos técnicos y de seguridad ciudadana aplicados bajo el ordenamiento legal colombiano. Implementar un sistema RAG sobre este manual garantiza que el asistente virtual formule respuestas estrictamente validadas por el sistema de emergencias de salud pública, eliminando alucinaciones críticas en procedimientos de soporte vital básico.

---

## Persona Usuaria Objetivo y Caso de Uso

* **Persona Usuaria Objetivo:** Ciudadanos comunes (taxistas, amas de casa, estudiantes, profesores), brigadistas de emergencias en entornos empresariales, personal de apoyo institucional (Defensa Civil, Cruz Roja) o cualquier persona que presencie un incidente.
* **Caso de Uso:** El sistema está diseñado para ser utilizado en situaciones de urgencia, entornos laborales de alta responsabilidad o escenarios de capacitación donde se requiera acceso inmediato y confiable a protocolos de soporte vital básico. Los principales escenarios de uso incluyen:
  
  1. **Atención de Emergencias en Tiempo Real:** Situaciones críticas en el hogar, la vía pública o empresas (como paros cardiorrespiratorios, atragantamientos, quemaduras, fracturas o intoxicaciones) donde un primer respondiente bajo condiciones de estrés necesita recordar inmediatamente las maniobras correctas, qué acciones evitar para no empeorar al paciente y cómo activar el Sistema de Emergencias Médicas (SEM).
  2. **Gestión de Seguridad y Salud en el Trabajo (SST):** Brigadistas de emergencia y personal de salud ocupacional en entornos corporativos o industriales que requieren verificar de forma rápida y estandarizada si sus botiquines, procedimientos de inmovilización o planes de contingencia se alinean con la normativa oficial vigente del manual.
  3. **Capacitación y Consulta Educativa:** Estudiantes de primeros auxilios, conductores de servicio público o ciudadanos interesados en la gestión del riesgo que desean validar sus conocimientos, resolver dudas puntuales en lenguaje natural o repasar técnicas específicas de atención prehospitalaria sin necesidad de hojear manualmente la totalidad del documento técnico.

---

## Pruebas del Sistema (Preguntas y Respuestas)

A continuación se registran 5 interacciones reales del sistema procesadas por el LLM (`llama-3.1-8b-instant`) con la inyección de contexto y las citas bibliográficas estructuradas dinámicamente:

### Pregunta 1: ¿Qué es un ciclo de reanimación cardiorespiratoria (RCP) y cuántas compresiones se deben alcanzar por minuto?
* **Respuesta del Sistema:** Un ciclo de reanimación cardiorespiratoria (RCP) consiste en 30 compresiones y 2 ventilaciones. Se recomienda realizar 5 ciclos en 2 minutos, lo que equivale a una frecuencia de 100 compresiones por minuto.
  **Páginas consultadas del documento:** Pág. 4, Pág. 28

### Pregunta 2: ¿Qué se debe hacer y qué NO se debe hacer ante una quemadura por calor?
* **Respuesta del Sistema:** Ante una quemadura por calor, se debe hacer lo siguiente:

- Lave con abundante agua limpia el área quemada por un tiempo no menor a 10 minutos.
- Cubra la quemadura con una tela limpia.

Y lo siguiente NO se debe hacer:

- No le dé nada de tomar o de comer a la persona quemada: agua, gaseosa, aromática.
- No le dé ningún medicamento.
- No aplique nada en la quemadura (cremas, pomadas, aceites, etcétera).
- Si la quemadura presenta ampollas, no las rompa.

  **Páginas consultadas del documento:** Pág. 23

### Pregunta 3: ¿Cuáles son las medidas para desobstruir la vía aérea en bebés (menores de 1 año) conscientes que muestran signos de atoramiento?
* **Respuesta del Sistema:** Si el bebé muestra signos de atoramiento, debe abrir la boca y verificar si observa el cuerpo extraño y puede retirarlo con el dedo meñique. Si no ve el cuerpo extraño o el elemento que está produciendo la obstrucción de la vía aérea, debe voltear al niño boca abajo sosteniéndolo firmemente, y dar 5 golpes con el talón de la mano en la espalda, entre los omóplatos o paletas. Luego, debe voltearlo boca arriba y realizar 5 compresiones torácicas en el punto de cruce de la línea imaginaria entre tetillas y el esternón.
  **Páginas consultadas del documento:** Pág. 30

### Pregunta 4: ¿Qué elementos esenciales debe contener un botiquín de primeros auxilios y cómo se debe usar el esparadrapo y las vendas?
* **Respuesta del Sistema:** Según el Manual del Primer Respondiente, un botiquín de primeros auxilios debe contener elementos esenciales como:

* Antisépticos: para prevenir la infección en heridas superficiales.
* Otros elementos no mencionados específicamente en el texto, pero que generalmente se incluyen en un botiquín de primeros auxilios son:
+ Vendajes y esparadrapo: para cubrir y proteger heridas.
+ Guantes: para protegerse las manos al atender a alguien.
+ Kit de primeros auxilios para heridas: que incluye elementos como algodón, gasas, etc.
+ Medicamentos básicos: como analgésicos, antihistamínicos, etc.

En cuanto al uso del esparadrapo y las vendas, se debe utilizar de la siguiente manera:

* El esparadrapo se debe utilizar para cubrir heridas pequeñas y superficiales, asegurándose de que no se aplique demasiado fuerte para evitar dañar la piel.
* Las vendas se deben utilizar para cubrir heridas más grandes o para aplicar presión en áreas específicas del cuerpo. Se deben aplicar de manera suave y segura, asegurándose de que no se apliquen demasiado apretadas.

Recuerda que es importante seguir las instrucciones del Manual del Primer Respondiente y consultar con un profesional de la salud si no estás seguro de cómo utilizar estos elementos.

  **Páginas consultadas del documento:** Pág. 13, Pág. 40

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
```bash
python -m venv venv
venv\Scripts\activate

3. Instalar dependencias requeridas
Ejecuta el gestor de paquetes para instalar todas las librerías necesarias definidas en las configuraciones del código fuente:
```bash
pip install -r requirements.txt

4. Configurar Variables de Entorno y Llaves API
Crea un archivo de texto plano en la raíz del proyecto llamado .env e introduce tus respectivos tokens privados de conexión remota:
```bash
HUGGINGFACEHUB_API_TOKEN=tu_token_de_huggingface_aqui
GROQ_API_KEY=gsk_tu_api_key_de_groq_aqui

5. Orden Obligatorio de Ejecución del Sistema
a. Construcción de la Base de Datos Vectorial (Poblamiento inicial)
Para leer el documento PDF, segmentarlo en fragmentos reducidos, generar los embeddings y guardarlos localmente, ejecuta el script principal:
```bash
python main.py

Espera a ver el mensaje de confirmación: 🎉 ¡Base de datos vectorial construida con éxito!. Verás que se habrá generado automáticamente la carpeta persistente local llamada chromadb/.

b. Inicialización de la Aplicación Web (Flask)
Una vez que la base vectorial contenga los datos indexados, arranca el servidor web que expone la API de interacción para el modelo de lenguaje Groq:
```bash
python app.py

El servidor iniciará en modo local. Abre tu navegador web e ingresa a la siguiente URL para interactuar con la interfaz gráfica de Médix:
http://127.0.0.1:5000
=======
# App_chatbot_primer_respondiente
>>>>>>> 89a77fbd82f72c045ae04657528b9db5b1dfb883
