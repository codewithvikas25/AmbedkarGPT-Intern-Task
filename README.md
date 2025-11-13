# AmbedkarGPT Intern Task

A simple command-line Q&A system built for **Kalpit Pvt Ltd (UK)** AI Internship Assignment.

## 🔧 Tech Stack
- **Python 3.8+**
- **LangChain**
- **ChromaDB**
- **HuggingFace Embeddings**
- **Ollama with Mistral 7B**

---

## ⚙️ Setup Instructions

1. Clone this repository:
   ```bash
   git clone https://github.com/<your-username>/AmbedkarGPT-Intern-Task.git
   cd AmbedkarGPT-Intern-Task
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate   # for Linux/Mac
   venv\Scripts\activate    # for Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Install and start Ollama:
   ```bash
   curl -fsSL https://ollama.ai/install.sh | sh
   ollama pull mistral
   ```

5. Run the program:
   ```bash
   python main.py
   ```

---

## 📜 Example Usage

**User Input:**
```
You: What does Ambedkar mean by the real remedy?
```

**Output:**
```
AmbedkarGPT: He says the real remedy is to destroy the belief in the sanctity of the shastras, since caste persists as long as people hold these texts sacred.
```

---

## 📁 Deliverables
- main.py
- requirements.txt
- README.md
- speech.txt

---

## 🧩 Notes
- No API keys are required.
- All components run locally.
- Verified with Python 3.10 and Ollama (Mistral 7B).
