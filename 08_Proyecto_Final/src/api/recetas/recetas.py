import chromadb
from contextlib import asynccontextmanager
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from chromadb.utils import embedding_functions

vector_db = {}

def cargar_model_embedding():
    return embedding_functions.SentenceTransformerEmbeddingFunction(model_name="paraphrase-multilingual-MiniLM-L12-v2")

def cargar_database():
    try:
        print("Cargando base de datos vectorial existente...")
        client = chromadb.PersistentClient(path="../../data/persistent_bd")

        vector_db["collection"] = client.get_collection(name="comidaMIA_DB" , embedding_function=cargar_model_embedding())
        print("¡Base de datos vectorial cargada con éxito!")
    except Exception as e:
        print(f"Error al cargar la base de datos: {e}")


@asynccontextmanager
async def lifespan(app: FastAPI):
    cargar_database()

    yield

    print("Cerrando recursos...")
    vector_db.clear()


app = FastAPI(lifespan=lifespan)

class QueryModel(BaseModel):
    consulta: str
    resultados: int = 3


@app.post("/buscar")
async def buscar_vectores(consulta: QueryModel):
    collection = vector_db.get("collection")
    if not collection:
        raise HTTPException(
            status_code=500, detail="La base de datos no está disponible"
        )

    try:
        # Realizamos la búsqueda
        # Nota: Recuerda usar el mismo modelo de embeddings que usaste al crearla
        resultados = collection.query(
            query_texts=[consulta.texto], n_results=consulta.resultados
        )

        return {"resultados": resultados}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
