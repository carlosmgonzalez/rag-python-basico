# Contexto del repositorio

## Propósito
Proyecto educativo de RAG en Python: genera embeddings con OpenAI, almacena/busca fragmentos con ChromaDB y usa un chat OpenAI para responder únicamente con el contexto recuperado. Incluye demos de similitud semántica, ChromaDB, una base de conocimiento de ejemplo y un flujo de indexación/chat sobre PDFs.

## Archivos recuperados
1. `pyproject.toml:1-19` — metadatos, Python >=3.12, dependencias y grupo de desarrollo.
2. `src/main.py:1-21` — punto de entrada actual; ejecuta la demo de embeddings.
3. `src/ai/openai_client.py:1-6` — cliente OpenAI creado desde `OPENAI_API_KEY` cargada por dotenv.
4. `src/rag/embeddings_demo.py:1-56` — embeddings `text-embedding-3-small`, similitud coseno y comparación de frases.
5. `src/rag/chromadb_demo.py:1-96` — cliente persistente/efímero, colección, carga de `KNOWLEDGE_BASE` y búsquedas de demostración.
6. `src/rag/knowledge_base.py:1-669` — seis documentos operativos (`KNOWLEDGE_BASE`) y el gran texto `INVESTOR_DATA` para indexación.
7. `src/rag/rag_pipeline.py:1-185` — pipeline central de indexación, chunking, recuperación y generación.
8. `src/rag/chat_with_pdfs.py:1-208` — extracción PDF, registro incremental por tamaño, interfaz interactiva y estado.
9. `README.md` (vacío) — no documenta instalación ni operación.
10. `.env:1` — contiene una clave privada de OpenAI en texto plano.
11. `.gitignore:1-14` — ignora `.env`, entornos virtuales y artefactos Python, pero no garantiza que secretos previamente versionados queden protegidos.

## Flujo de ejecución y datos
- `src/main.py` llama `demonstrate_semantic_similarity()`, que solicita un embedding para la frase base y para cada candidato en OpenAI, calcula coseno y devuelve el candidato más similar.
- `src/rag/chromadb_demo.py` crea `PersistentClient("./data/chromadb")`, crea la colección `knowledge_base` con embedding OpenAI, añade los seis documentos si está vacía y consulta siete preguntas de ejemplo. `data/chromadb/chroma.sqlite3` y binarios existentes son estado persistido.
- `RAGPipeline` (`src/rag/rag_pipeline.py:26-185`) usa Chroma persistente; `index_text` crea IDs UUID; `index_chunks` corta por caracteres aproximados (500 tokens * 4, solape 50 * 4) y añade metadatos; `retrieve_context` consulta hasta N fragmentos y conserva los de similitud calculada `1-distance` superior a 0.3; `answer` construye el prompt con fragmentos y llama al chat OpenAI.
- `ChatWithPDFs` (`src/rag/chat_with_pdfs.py:96-208`) busca PDFs en `./data/pdfs`, extrae texto página a página con pypdf, indexa en colección `knowledge_base` bajo `./data/chromadb_pdfs`, y mantiene `./data/pdfs_indexed.txt` según nombre/tamaño. La interfaz acepta `estado`, `reindexar` y `salir`.
- El bloque `__main__` de `chat_with_pdfs.py` actualmente solo extrae/imprime `./proton-recovery-phrase.pdf`; no instancia ni lanza `ChatWithPDFs`. El bloque de `rag_pipeline.py` sí puede consultar `investors_knowledge_base`, pero la línea que indexaría `INVESTOR_DATA` está comentada.

## Dependencias y comandos
Dependencias declaradas: `chromadb`, `openai`, `pydantic`, `pypdf`, `python-dotenv`, `rich`; desarrollo: `ruff` (`pyproject.toml:7-19`). El lockfile `uv.lock` fija el entorno. No hay tests ni configuración pytest detectables; README vacío.

Comandos razonables con uv (no ejecutados):
- `uv sync`
- `uv run python -m src.main` (demo de embeddings; requiere API key y red)
- `uv run python -m src.rag.chromadb_demo` (indexación/búsquedas; requiere API key)
- `uv run python -m src.rag.chat_with_pdfs` (solo extracción del PDF raíz en el estado actual)
- `uv run ruff check .`

## Observaciones y riesgos
- **Crítico — secreto expuesto:** `.env:1` contiene una clave `sk-proj-...` real en texto plano. Aunque `.gitignore` ignora `.env`, el archivo existe localmente y debe revocarse/rotarse inmediatamente; nunca debe compartirse ni versionarse.
- **Alto — modelo posiblemente inválido/no estándar:** `rag_pipeline.py:153` y `chat_with_pdfs.py:137` usan `gpt-5.6-luna`; una cuenta OpenAI normal podría no tener ese modelo, causando fallo en cada respuesta.
- **Alto — manejo de errores silencioso:** `chat_with_pdfs.py:199-200` captura cualquier `Exception` y hace `pass`, ocultando fallos de API, Chroma o parsing.
- **Medio — bug de citas/contexto:** `rag_pipeline.py:126` obtiene `fragment['metadata'].get('')`, siempre una clave vacía, por lo que no incorpora realmente la fuente en `context_text`.
- **Medio — riesgo de colección duplicada:** `index_new_pdfs` registra por nombre/tamaño, pero si cambia un PDF indexado no elimina chunks anteriores; pueden coexistir versiones y duplicar resultados.
- **Medio — chunking frágil:** `index_chunks` (`rag_pipeline.py:65-93`) usa aproximación fija caracteres/token, no separa por límites semánticos y puede producir comportamiento inesperado con `overlap >= chunk_size`.
- **Medio — recuperación no defensiva:** `n_results=min(n_fragments, count)` puede pasar 0 a Chroma con colección vacía si se llama directamente; no hay validación de parámetros ni de distancias/modelo.
- **Bajo — calidad/mantenibilidad:** `from ast import While` es import no usado; `README.md` está vacío; no hay tests, CLI formal ni instrucciones reproducibles.
- **Privacidad:** el repositorio contiene `proton-recovery-phrase.pdf` (posible material sensible) y una extensa guía financiera en `knowledge_base.py`; revisar si ambos pueden distribuirse.

## Arquitectura
Entrada/demo -> cliente OpenAI -> embeddings. Para RAG: documentos o PDFs -> extracción/chunking -> OpenAI embeddings -> Chroma persistente -> consulta semántica -> filtro de similitud -> prompt restringido -> chat OpenAI -> respuesta y fragmentos usados. Hay dos almacenes independientes: `./data/chromadb` para la demo y `./data/chromadb_pdfs` para PDFs.

## Start Here
Abrir primero `src/rag/rag_pipeline.py:26-185`, porque contiene el contrato y flujo principal de indexación, recuperación y respuesta; después `src/rag/chat_with_pdfs.py:19-208` para el flujo de documentos reales.

## Acceptance
```acceptance-report
{
  "criteriaSatisfied": [
    {
      "id": "criterion-1",
      "status": "satisfied",
      "evidence": "Se inspeccionaron directamente pyproject.toml, src/main.py, todos los módulos RAG, README, .gitignore y .env; se documentaron rutas, rangos, flujo, dependencias y riesgos con severidad."
    }
  ],
  "changedFiles": ["context.md"],
  "testsAddedOrUpdated": [],
  "commandsRun": [
    {"command": "find/ls/read del repositorio", "result": "passed", "summary": "Inventario y lectura directa completados"},
    {"command": "wc -l archivos principales", "result": "passed", "summary": "Rangos de archivos verificados"},
    {"command": "uv run tests", "result": "not-run", "summary": "No existe suite de tests detectada"}
  ],
  "validationOutput": ["README vacío; no se detectaron tests ni configuración pytest."],
  "residualRisks": ["Revocar/rotar inmediatamente la clave expuesta en .env", "Validar el modelo gpt-5.6-luna", "Corregir excepciones silenciosas y duplicación de chunks"],
  "noStagedFiles": true,
  "diffSummary": "No se modificó código; se generó únicamente este informe solicitado.",
  "reviewFindings": ["critical: .env:1 - clave OpenAI expuesta", "high: src/rag/rag_pipeline.py:153 - modelo de chat posiblemente no disponible", "high: src/rag/chat_with_pdfs.py:199-200 - excepciones silenciadas", "medium: src/rag/rag_pipeline.py:126 - fuente no interpolada en contexto"],
  "manualNotes": "El archivo context.md es el único artefacto generado para esta tarea."
}
```
