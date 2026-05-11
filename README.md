
# Local Bangalore Zomato AI Agent

A local RAG (Retrieval-Augmented Generation) system that uses AI to recommend restaurants in Bangalore based on real Zomato data. It runs entirely on your local machine using **Ollama** and **ChromaDB**.

## 🚀 Features
- **Semantic Search**: Finds restaurants based on cuisines and "People Known For" descriptions.
- **Local Privacy**: No data leaves your machine; everything runs via Ollama.
- **Interactive Chat**: A simple terminal interface to ask questions about local dining.

## 🛠️ Prerequisites
1. **Ollama**: [Download and install Ollama](https://ollama.com/).
2. **Python 3.12+**: Ensure you have Python installed.
3. **Required Models**:
   ```bash
   ollama pull llama3:latest
   ollama pull nomic-embed-text
   ```

## 📦 Installation
Install the necessary Python libraries:
```bash
pip3 install langchain langchain-ollama langchain-chroma pandas
```

## 📂 Project Structure
- `main.py`: The main chat interface. It uses the retriever to find relevant restaurants and passes them to the LLM.
- `vector.py`: Handles data processing. It reads the CSV, creates embeddings, and stores them in a local ChromaDB.
- `BangaloreZomatoData.csv`: The dataset containing restaurant names, ratings, cuisines, and reviews.
- `chrome_langchain_db/`: (Generated) The local folder where your vector database is stored.

## 🚦 How to Run
1. **Initialize the Database**: 
   The first time you run the app, it will process the CSV and create the local database. This might take a few minutes depending on your CPU/GPU.
   
2. **Start the Agent**:
   Run the following command in your terminal:
   ```bash
   python3 main.py
   ```

3. **Usage**:
   - Type your question (e.g., "suggest a spicy biryani place in Indiranagar").
   - Press **`q`** to quit the chat.

## 💡 Troubleshooting
- **Missing Module Error**: If you see `ModuleNotFoundError`, ensure you have run the `pip3 install` command above.
- **Ollama Error**: Ensure the Ollama application is running in your menu bar before starting the script.
- **CSV Data Errors**: If you get a `TypeError`, ensure your code uses `str()` to handle empty cells in the CSV (this is already implemented in the current version).
```

### Key Implementation Details (For your reference)
*   **Embeddings**: Uses `nomic-embed-text` for high-quality, fast vector creation.
*   **LLM**: Uses `llama3:latest` for natural language responses.
*   **Vector DB**: Uses `Chroma` to store and retrieve data locally in the `./chrome_langchain_db` folder.
