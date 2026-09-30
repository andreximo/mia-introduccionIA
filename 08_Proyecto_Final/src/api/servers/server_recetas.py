"""
Servidor MCP: búsqueda semántica de recetas sobre una base vectorial (Chroma).

"""

import sys
from pathlib import Path

import chromadb
from chromadb.utils import embedding_functions
from mcp.server.mcpserver import MCPServer

mcp = MCPServer("servidor-recetas")

# Ruta a la carpeta persistente de Chroma. Ajusta esto si tu carpeta
# "persistent_bd" no vive en <raíz-del-proyecto>/data/persistent_bd.
SRC_DIR = Path(__file__).resolve().parents[2]
RUTA_BD = SRC_DIR / "data" / "persistent_bd"

_collection = None


def _cargar_modelo_embedding():
    return embedding_functions.SentenceTransformerEmbeddingFunction(
        model_name="paraphrase-multilingual-MiniLM-L12-v2"
    )


def _cargar_coleccion() -> None:
    """
    Carga la colección de Chroma. Se llama una sola vez, al arrancar este
    servidor (ver el bloque __main__ al final), no en cada consulta.
    """
    global _collection
    print("[recetas] Cargando base de datos vectorial existente...", file=sys.stderr)
    try:
        client = chromadb.PersistentClient(path=str(RUTA_BD))
        _collection = client.get_collection(
            name="comidaMIA_DB", embedding_function=_cargar_modelo_embedding()
        )
        print("[recetas] ¡Base de datos vectorial cargada con éxito!", file=sys.stderr)
    except Exception as e:
        print(f"[recetas] Error al cargar la base de datos: {e}", file=sys.stderr)


@mcp.tool()
def buscar_recetas(consulta: str, resultados: int = 3) -> dict:
    """El menú del restaurante esta basado en este recetario. 
       Permite buscar los platillos de la gastronomia mexicana que se preparan en el restaurante.
       Recuerda no inventar ingredites ya que eso afecta la reputacoin del restaurante.
       """
    if _collection is None:
        return {"error": "La base de datos no está disponible."}

    try:
        resultado = _collection.query(query_texts=[consulta], n_results=resultados)
        return {"resultados": resultado}
    except Exception as e:
        return {"error": str(e)}


if __name__ == "__main__":
    _cargar_coleccion()
    mcp.run(transport="stdio")