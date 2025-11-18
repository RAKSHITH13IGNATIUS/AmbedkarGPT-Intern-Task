# AmbedkarGPT-Intern-Task

## 🧠 Assignment Overview: RAG Q&A System Prototype

This repository contains the functional prototype for the Kalpit Pvt Ltd AI Intern Assignment. The task was to implement a simple command-line Question & Answer system using the Retrieval-Augmented Generation (RAG) architectural pattern.

The system is designed to answer user questions based **solely** on the content of the provided `speech.txt` file (an excerpt from Dr. B.R. Ambedkar's "Annihilation of Caste").

---

## 🛠️ Technical Stack & Requirements

| Component | Technology Used | Constraint Source |
| :--- | :--- | :--- |
| **Orchestration** | [cite_start]LangChain (Python) | [cite: 15] |
| **Vector Store** | [cite_start]ChromaDB (Local, Open-Source) | [cite: 16] |
| **Embeddings** | [cite_start]HuggingFaceEmbeddings (`sentence-transformers/all-MiniLM-L6-v2`) | [cite: 17] |
| **Large Language Model (LLM)** | [cite_start]Ollama with Mistral 7B (Local, Free) | [cite: 18] |
| **Data Source** | [cite_start]`speech.txt` (Provided Excerpt) | [cite: 8, 26] |

---

## 🚀 Setup and Installation Guide

This guide assumes you have **Python 3.8+** installed on your system. It is highly recommended to use **Python 3.11 or 3.12** for maximum compatibility with the LangChain/Pydantic stack.

### 1. Install Ollama and Pull the Model

Ollama must be running in the background for the LLM to be available via the local API.

1.  **Download and Install Ollama:**
    Follow the instructions on the official Ollama website.
2.  **Pull the Required Model:**
    Open your terminal/command prompt and run:
    ```bash
    ollama pull mistral
    ```
    *(Note: This model is approximately 4.1GB and requires sufficient system memory/VRAM to run.)*

### 2. Project Setup and Dependencies

Navigate to the project root directory in your terminal.

1.  **Create a Virtual Environment** (Recommended):
    ```bash
    python -m venv venv
    ```
2.  **Activate the Environment:**
    * **Windows (PowerShell):** `.\venv\Scripts\Activate`
    * **macOS/Linux:** `source venv/bin/activate`
3.  **Install Required Libraries:**
    The necessary dependencies are listed in the `requirements.txt` file.
    ```bash
    pip install -r requirements.txt
    ```

---

## ▶️ How to Run the System

The system is executed via a single Python script that handles the entire RAG pipeline orchestration.

1.  Ensure the **Ollama application is running** in the background.
2.  Run the main application script from the activated virtual environment:

    ```bash
    python main.py
    ```

### Expected Output & Interaction

The system will first initialize, performing the RAG setup steps:

1.  [cite_start]Load the text[cite: 8].
2.  [cite_start]Split the text into chunks[cite: 9].
3.  [cite_start]Create and store embeddings in ChromaDB[cite: 10].

Once initialized, the system will enter an interactive Q&A loop:
