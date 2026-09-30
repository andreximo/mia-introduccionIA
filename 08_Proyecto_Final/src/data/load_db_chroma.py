from pypdf import PdfReader
from sentence_transformers import SentenceTransformer
from langchain_text_splitters import RecursiveCharacterTextSplitter
from chromadb.utils import embedding_functions
from transformers import AutoTokenizer
from pathlib import Path
import chromadb
import os
import shutil

def generate_chunks(texto_completo):
    tokenizer = AutoTokenizer.from_pretrained(pretrained_model_name_or_path=model_name)
    text_splitter = RecursiveCharacterTextSplitter.from_huggingface_tokenizer(
    tokenizer=tokenizer,
    chunk_size=400,         # Tamaño máximo del fragmento medido en tokens
    chunk_overlap=40        # Superposición entre fragmentos para no perder contexto semántico
    )
    return text_splitter.split_text(texto_completo)

def validate_db():
    # 1. Configurar el mismo modelo que usaste para crearla
    embedding_fn = embedding_functions.SentenceTransformerEmbeddingFunction(
        model_name="paraphrase-multilingual-MiniLM-L12-v2"
    )

    # 2. Conectar a la base de datos persistente
    client = chromadb.PersistentClient(path="08_Proyecto_Final/src/data/persistent_bd")

    try:
        # 3. Obtener la colección
        collection = client.get_collection(name="comidaMIA_DB", embedding_function=embedding_fn)
        
        # 4. VALIDACIÓN 1: Verificar el número total de registros
        total_registros = collection.count()
        print(f"📊 Total de registros guardados: {total_registros}")
        
        if total_registros > 0:
            # 5. VALIDACIÓN 2: Traer los primeros 5 registros reales guardados
            datos = collection.get(limit=5)
            print("\n🔍 Primeros registros encontrados:")
            for idx, doc_id in enumerate(datos['ids']):
                print(f"--- Registro {idx + 1} ---")
                print(f"🆔 ID: {doc_id}")
                print(f"📄 Texto: {datos['documents'][idx]}")
                if datos['metadatas'] and datos['metadatas'][idx]:
                    print(f"🏷️ Metadatas: {datos['metadatas'][idx]}")
        else:
            print("⚠️ La colección existe, pero está completamente vacía.")
            
    except Exception as e:
        print(f"❌ Error al acceder a la colección: {e}")


def main() -> None:

    global model_name
    path="08_Proyecto_Final/src/data"
    archivo_pdf=path+"/grandeza-gastronomica-mexico.pdf"
    db_path=path+"/persistent_bd"
    model_name = "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"

    try:
        reader = PdfReader(archivo_pdf)
        pdf_texts = [p.extract_text().strip() for p in reader.pages]

        # Unimos con espacios para evitar romper palabras entre páginas
        texto_completo = " ".join([text for text in pdf_texts if text])

        chunks = generate_chunks(texto_completo)
        ids = [f"id_chunk_{i}" for i in range(len(chunks))]

        # 2. BORRAR la base de datos si ya existe
        if os.path.exists(db_path):
            shutil.rmtree(db_path)
            print(f"Base de datos en '{db_path}' eliminada correctamente.")

        embedding_fn = embedding_functions.SentenceTransformerEmbeddingFunction(model_name="paraphrase-multilingual-MiniLM-L12-v2")
        client = chromadb.PersistentClient(path=db_path)
        collection = client.create_collection(name="comidaMIA_DB", embedding_function=embedding_fn)

        # Al añadir datos, se guardan automáticamente en ese directorio
        collection.add(
            documents=chunks,
            ids=ids)

        print(f"Éxito: Se procesó el PDF en {len(chunks)} fragmentos y se guardaron en ChromaDB.")
        validate_db()

    except Exception as e:
        print(f"Error al leer el archivo pdf({archivo_pdf}): {e}")
        print("Please download file before continue")


if __name__ == "__main__":
    main()