# E-commerce Product Search

A Gradio product-search application using a product CSV, FAISS vector search, and OpenAI models.

## Setup

Create and activate a virtual environment, then install the dependencies:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

Set your OpenAI API key in a local `.env` file at the project root:

```env
OPENAI_API_KEY=your_api_key_here
```

Do not commit `.env` or expose the key in source control. If an API key has been exposed, revoke it and create a replacement.

## Run

Start the Gradio app from the project root:

```bash
python gradio_ui.py
```

Open the local URL printed by Gradio in your browser and enter a product question.

## Data

The product catalog is stored at `src/prod_small2.csv` and is loaded relative to `src/main.py`, so the application does not depend on a developer-specific absolute path. Keep the CSV in the repository when it is small and non-sensitive. For a large or private catalog, store it in object storage and download it during deployment instead.

## Project Files

- `gradio_ui.py`: Gradio interface and application entry point.
- `src/main.py`: Loads the catalog, creates embeddings and the FAISS index, and builds the retrieval chain.
- `src/prod_small2.csv`: Product catalog used by the application.
- `requirements.txt`: Python dependencies.
