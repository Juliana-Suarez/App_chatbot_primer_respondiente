import os
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv

# Librerías del Vector Store y Embeddings
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEndpointEmbeddings

# Librerías para el Prompt y el LLM (Groq)
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq

# 0. CONFIGURACIÓN DE ENTORNO Y LLAVES
load_dotenv()
HF_TOKEN = os.getenv('HUGGINGFACEHUB_API_TOKEN')
GROQ_API_KEY = os.getenv('GROQ_API_KEY')
PERSIST_DIR = './chromadb'

# Inicializamos la aplicación Flask
app = Flask(__name__)

# INICIALIZACIÓN DE COMPONENTES DEL RAG (Se cargan al encender el servidor)
embeddings = HuggingFaceEndpointEmbeddings(
    model="sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2",
    huggingfacehub_api_token=HF_TOKEN
)

vector_store = Chroma(
    persist_directory=PERSIST_DIR,
    embedding_function=embeddings
)

retriever = vector_store.as_retriever(search_type="similarity", search_kwargs={"k": 5})

llm = ChatGroq(
    model='llama-3.1-8b-instant',
    temperature=0.2,
    groq_api_key=GROQ_API_KEY
)

PROMPT_TEMPLATE = """
Eres Médix, un asistente virtual experto en guiar a los ciudadanos como primer respondiente con todos los pasos del contexto, especializado estrictamente en el contexto proporcionado.
Responde la pregunta del usuario de forma completa, clara y precisa, usando única y exclusivamente la información del contexto proporcionado.
Si la respuesta no está en el contexto, responde textualmente: "Lo siento, no puedo responder a preguntas fuera del contexto del manual del primer respondiente".

Contexto:
{contexto}

Pregunta del usuario:
{question}

Respuesta:
"""
prompt_template = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)


# ==========================================
# RUTAS DE FLASK
# ==========================================

# Ruta principal: Muestra la interfaz gráfica de chat
@app.route('/')
def home():
    return render_template('index.html')


# Ruta de la API: Recibe la pregunta en JSON, procesa el RAG y devuelve la respuesta
@app.route('/ask', methods=['POST'])
def ask():
    # Obtener los datos JSON enviados desde el frontend
    data = request.get_json()
    user_query = data.get('message', '')
    
    if not user_query:
        return jsonify({'response': 'Por favor, escribe una pregunta válida.'}), 400

    # 1. Recuperar fragmentos relevantes mediante similitud matemática
    documents = retriever.invoke(user_query)
    
    paginas_consultadas = set()
    fragmentos_contexto = []
    
    for i, doc in enumerate(documents):
        num_pag = doc.metadata.get("page", 0) + 1
        paginas_consultadas.add(num_pag)
        fragmentos_contexto.append(f"[Fragmento {i+1}]\n{doc.page_content}")
        
    contexto = '\n\n--\n\n'.join(fragmentos_contexto)
    
    # 2. Formatear el Prompt Aumentado
    prompt_aumentado = prompt_template.invoke({
        'contexto': contexto,
        'question': user_query
    })
    
    # 3. Obtener respuesta del LLM con Groq
    respuesta = llm.invoke(prompt_aumentado)
    texto_respuesta = respuesta.content
    
    frase_control = "Lo siento, no puedo responder a preguntas fuera del contexto del manual del primer respondiente"
    
    # 4. Añadir citas si la respuesta está fundamentada en el documento
    if frase_control.lower() not in texto_respuesta.lower():
        paginas_ordenadas = sorted(list(paginas_consultadas))
        citas = ", ".join(f"Pág. {p}" for p in paginas_ordenadas)
        texto_respuesta += f"\n\n** Páginas consultadas del documento:** {citas}"
    
    # Devolver el resultado final en formato JSON al frontend
    return jsonify({'response': texto_respuesta})


if __name__ == '__main__':
    # Desactivamos el reloader para evitar reinicios infinitos en entornos virtuales
    app.run(debug=True, port=5000, use_reloader=False)