# AmbedkarGPT-Intern-Task

## 🧠 Assignment Overview: RAG Q&A System Prototype

This repository contains the functional prototype for the Kalpit Pvt Ltd AI Intern Assignment. The task was to implement a simple command-line Question & Answer system using the **Retrieval-Augmented Generation (RAG)** architectural pattern.

The system is designed to answer user questions based **solely** on the content of the provided `speech.txt` file (an excerpt from Dr. B.R. Ambedkar's "Annihilation of Caste").

---

## 🛠️ Technical Stack & Requirements

| Component | Technology Used |
| :--- | :--- |
| **Orchestration** | LangChain (Python 3.8+) |
| **Vector Store** | ChromaDB (Local, Open-Source) |
| **Embeddings** | HuggingFaceEmbeddings (`sentence-transformers/all-MiniLM-L6-v2`) |
| **Large Language Model (LLM)** | Ollama with Mistral 7B (Local, Free) |
| **Data Source** | `speech.txt` (Provided Excerpt) |

---

## 🚀 Setup and Installation Guide

This guide assumes you have **Python 3.8+** installed on your system. It is highly recommended to use **Python 3.11 or 3.12** for maximum compatibility with the LangChain stack.

### 1. Install Ollama and Pull the Model

Ollama must be running in the background for the LLM to be available via the local API.

1.  **Download and Install Ollama:**
    Follow the instructions on the official Ollama website.
2.  **Pull the Required Model:**
    Open your terminal/command prompt and run:
    ```bash
    ollama pull mistral
    ```
    *(Note: This model is approximately 4.5GB and requires sufficient system memory/VRAM to run.)*

### 2. Project Setup and Dependencies

Navigate to the project root directory in your terminal.

1.  **Create a Virtual Environment** (Recommended):
    ```bash
    python -m venv venv
    ```
2.  **Activate the Environment:**
    * **Windows (PowerShell):** `.\venv\Scripts\activate`
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
    <img width="1852" height="991" alt="Screenshot 2025-11-18 234039" src="https://github.com/user-attachments/assets/f778c2a6-9e20-46d8-882d-df2cc4149107" />
<img width="1309" height="563" alt="Screenshot 2025-11-18 234058" src="https://github.com/user-attachments/assets/d78303ae-0f30-44af-a055-0976b85bd9c5" />


### Expected Output & Interaction

The system will first initialize, performing the RAG setup steps (loading, splitting, embedding, and storing in ChromaDB). Once initialized, the system enters an interactive Q&A loop:
