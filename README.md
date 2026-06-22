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
* **Justificación:** En situaciones de emergencia médica, accidentes de tránsito o incidentes domésticos, el tiempo y la exactitud de los primeros auxilios son fundamentales para mitigar riesgos de invalidez o muerte. Este documento oficial fue seleccionado porque estandariza los protocolos técnicos y de seguridad ciudadana aplicados bajo el ordenamiento legal colombiano. Implementar un sistema RAG sobre este manual garantiza que el asistente virtual formule respuestas estrictamente validadas por el sistema de emergencias de salud pública, eliminando posibles alucinaciones.
---

## Persona Usuaria Objetivo y Caso de Uso

* **Persona Usuaria Objetivo:** Ciudadanos comunes (taxistas, amas de casa, estudiantes, profesores), brigadistas de emergencias en entornos empresariales, personal de apoyo institucional (Defensa Civil, Cruz Roja) o cualquier persona que presencie un incidente como primer respondiente.
* **Caso de Uso:** El sistema está diseñado para ser utilizado en situaciones de urgencia, entornos laborales de alta responsabilidad o escenarios de capacitación donde se requiera acceso inmediato y confiable a protocolos. 
Los principales escenarios de uso incluyen:
  
  1. **Atención de Emergencias en Tiempo Real:** Situaciones críticas en el hogar, la vía pública o empresas (como paros cardiorrespiratorios, atragantamientos, quemaduras, fracturas o intoxicaciones) donde un primer respondiente bajo condiciones de estrés necesita recordar inmediatamente la primera respuesta a incidentes o emergencias, qué acciones evitar para no empeorar la situacion o afectados y cómo activar el Sistema de Emergencias Médicas (SEM).
  2. **Gestión de Seguridad y Salud en el Trabajo (SST):** Brigadistas de emergencia y personal de salud ocupacional en entornos corporativos o industriales que requieren verificar de forma rápida y estandarizada si sus botiquines, procedimientos de inmovilización o planes de contingencia se alinean con la normativa oficial vigente del manual.
  3. **Capacitación y Consulta Educativa:** Estudiantes de primeros auxilios, conductores de servicio público o ciudadanos interesados en la gestión del riesgo que desean validar sus conocimientos, resolver dudas puntuales en lenguaje natural o repasar técnicas específicas de atención prehospitalaria sin necesidad de hojear manualmente la totalidad del documento técnico.

---

## Pruebas del Sistema (Preguntas y Respuestas)

A continuación se registran 5 interacciones reales del sistema procesadas por el LLM (`llama-3.1-8b-instant`) con la inyección de contexto y las citas bibliográficas estructuradas dinámicamente:

### Pregunta 1: ¿Qué es un ciclo de reanimación cardiorespiratoria (RCP) y cuántas compresiones se deben alcanzar por minuto?
* **Respuesta del Sistema:** Un ciclo de reanimación cardiorrespiratoria (RCP) consiste en 30 compresiones y 2 ventilaciones. Se debe intentar alcanzar una frecuencia de 100 compresiones por minuto.
  **Páginas consultadas del documento:** Pág. 4, Pág. 28

### Pregunta 2: ¿Qué se debe hacer y qué NO se debe hacer ante una quemadura por calor?
* **Respuesta del Sistema:**Ante una quemadura por calor, se deben hacer los siguientes pasos:

- Acérquese a la persona con precaución.
- Identifíquese ofreciendo ayuda.
- Asegúrese que usted o la persona no corren peligro adicional.
- Active el sistema de emergencias médicas. Llame al 125/123.
- Protéjase usted.
- Retire a la persona de la fuente de calor lo más rápido posible.
- Si las prendas de vestir están en llama, apague el fuego de la víctima. Esto se logra envolviéndola en una cobija o toalla.
- Aplique agua fría (no helada) por 10 minutos, especialmente si las quemaduras son grandes.
- Retire todas las prendas de vestir y las alhajas que no estén adheridas a la piel.
- Cubra la lesión con una tela limpia.

Y lo siguiente NO se debe hacer:

- No le dé nada de tomar o de comer a la persona quemada (agua, gaseosa, aromática).
- No le dé ningún medicamento.
- No aplique nada en la quemadura (cremas, pomadas, aceites, etcétera).

  **Páginas consultadas del documento:** Pág. 12, Pág. 22, Pág. 23  
  
### Pregunta 3: ¿Cuáles son las medidas para desobstruir la vía aérea en bebés (menores de 1 año) conscientes que muestran signos de atoramiento?
* **Respuesta del Sistema:** Si el bebé muestra signos de atoramiento, abra la boca y verifique si observa el cuerpo extraño y puede retirarlo con el dedo meñique. No haga barridos a ciegas. Si no ve el cuerpo extraño o el elemento que está produciendo la obstrucción de la vía aérea, vuelva al niño boca abajo sosteniéndolo firmemente, y dé 5 golpes con el talón de la mano en la espalda, entre los omóplatos o paletas. Inmediatamente vuelva al niño boca arriba, realice 5 compresiones torácicas en el punto de cruce de la línea imaginaria entre tetillas y el esternón.
  **Páginas consultadas del documento:** Pág. 30

### Pregunta 4: ¿Qué elementos esenciales debe contener un botiquín de primeros auxilios y cómo se debe usar el esparadrapo y las vendas?
* **Respuesta del Sistema:** Según el Manual del Primer Respondiente de Bogotá, un botiquín de primeros auxilios debe contener los siguientes elementos esenciales:

* Antisépticos
* Esparadrapo: se utiliza para fijar vendas y afrontar el borde de las heridas.
* Gasas: se usan para limpiar y cubrir heridas o para detener hemorragias pequeñas.
* Vendas: sirven para inmovilizar extremidades y realizar compresión en caso de hemorragias. Pueden ser elásticas, de tela o de gasa.
* Vendas adhesivas: tales como banditas, curitas; son útiles para cubrir heridas superficiales.
* Agua limpia: se utiliza para lavar heridas y quemaduras.
* Otros elementos: guantes desechables, tapabocas, linterna, tijeras, termómetro, jabón de manos, lista de teléfonos de emergencia, incluidos los de las EPS y las ARP, Manual del Primer Respondiente, bolsas plásticas.

En cuanto a la utilización del esparadrapo y las vendas, se debe tener en cuenta lo siguiente:

* El esparadrapo se utiliza para fijar vendas y afrontar el borde de las heridas.
* Las vendas se utilizan para inmovilizar extremidades y realizar compresión en caso de hemorragias. Pueden ser elásticas, de tela o de gasa.
* Es importante recordar que el uso de medicamentos debe ser bajo receta del médico y no se debe autoformular ni utilizar fórmulas antiguas ni formular a otros.

  **Páginas consultadas del documento:** Pág. 3, Pág. 8, Pág. 13, Pág. 14, Pág. 40

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
```

2. Configurar el Entorno Virtual (Python 3)  
En entornos Windows (PowerShell/CMD):
```bash
python -m venv venv
venv\Scripts\activate
```


3. Instalar dependencias requeridas  
Ejecuta el gestor de paquetes para instalar todas las librerías necesarias definidas en las configuraciones del código fuente:
```bash
pip install -r requirements.txt
```

4. Configurar Variables de Entorno y Llaves API  
Crea un archivo de texto plano en la raíz del proyecto llamado .env e introduce tus respectivos tokens privados de conexión remota:
```bash
HUGGINGFACEHUB_API_TOKEN=tu_token_de_huggingface_aqui
GROQ_API_KEY=gsk_tu_api_key_de_groq_aqui
```

5. Orden Obligatorio de Ejecución del Sistema  

a. Construcción de la Base de Datos Vectorial (Poblamiento inicial)  
Para leer el documento PDF, segmentarlo en fragmentos reducidos, generar los embeddings y guardarlos localmente, ejecuta el script principal:
```bash
python main.py
```

Espera a ver el mensaje de confirmación: 🎉 ¡Base de datos vectorial construida con éxito!. Verás que se habrá generado automáticamente la carpeta persistente local llamada chromadb/.

b. Inicialización de la Aplicación Web (Flask)  
Una vez que la base vectorial contenga los datos indexados, arranca el servidor web que expone la API de interacción para el modelo de lenguaje Groq:
```bash
python app.py
```

6. El servidor iniciará en modo local. Abre tu navegador web e ingresa a la siguiente URL para interactuar con la interfaz gráfica de Médix:
http://127.0.0.1:5000

=======
# App_chatbot_primer_respondiente
>>>>>>> 89a77fbd82f72c045ae04657528b9db5b1dfb883
