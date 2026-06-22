import os
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEndpointEmbeddings

# 0. Configuración de llaves y entorno
load_dotenv()
HF_TOKEN = os.getenv('HUGGINGFACEHUB_API_TOKEN')

# Rutas de los archivos
RUTA_PDF = "./pdf/Manual_Primer_Respondiente_4edicion.pdf"
PERSIST_DIR = './chromadb'

# 1. CARGA DE DOCUMENTO
print("1. Cargando el manual en formato PDF...")
loader = PyPDFLoader(RUTA_PDF)
paginas = loader.load()
print(f"Documento cargado. Páginas totales: {len(paginas)}")

# 2. CREAR CHUNKS
print("2. Dividiendo el texto en chunks...")
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=400,
    length_function=len,
    separators=["\n\n", "\n", " ", ""]
)
chunks = text_splitter.split_documents(paginas)
print(f"Fragmentación lista. Chunks creados: {len(chunks)}")

# 3 . GENERAR EMBEDDINGS 
print("3. Inicializando embeddings remotos de Hugging Face...")
embeddings = HuggingFaceEndpointEmbeddings(
    model="sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2",
    huggingfacehub_api_token=HF_TOKEN
)
#4. ALMACENAR EN BD VECTORIAL
print(f"4. Indexando los fragmentos en la BD Vectorial ({PERSIST_DIR})...")
vector_store = Chroma.from_documents(
    documents=chunks,
    embedding=embeddings,
    persist_directory=PERSIST_DIR
)

print("\n🎉 ¡Base de datos vectorial construida con éxito! Ya puedes cerrar este script.")