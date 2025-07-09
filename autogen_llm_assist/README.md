
# 🤖 AutoGen LLM Assistant (Zero-Cost Local AI Agent Framework)

This project is a multi-mode intelligent assistant framework using [Microsoft AutoGen](https://github.com/microsoft/autogen) with local LLMs served via [Ollama](https://ollama.com/). It enables zero-cost AI operations for screen analysis, DevOps automation, and multi-agent code generation.

---

## 📦 Modes & Use Cases

| Mode               | Description                                                                 |
|--------------------|-----------------------------------------------------------------------------|
| `screenshot`       | Takes a screenshot, extracts text via OCR, analyzes with LLM, and responds. |
| `devops`           | Accepts DevOps prompts (e.g., Ansible), responds with LLM-generated scripts.|
| `coder`            | Multi-agent system for coding, planning, reviewing, and execution loops.    |

---

## ✅ Features

- 🔁 **Multi-agent chat orchestration** using AutoGen
- 🧠 **Local LLM integration** via Ollama (no OpenAI billing)
- 🧩 **Three pluggable modes** for DevOps, OCR, and code generation
- 🖼️ **Screenshot OCR** using Tesseract and Pillow
- 💬 **Autonomous chat loop** with controlled user input handling

---

## 🛠️ Requirements

- Python 3.10+
- [Ollama](https://ollama.com/download) (installed and running locally)
- A local LLM model (e.g., `llama3`)
- Tesseract OCR installed (`tesseract.exe` in PATH or configured in script)

---

## 🔧 Installation

```bash
git clone https://github.com/your-username/autogen-llm-assist.git
cd autogen-llm-assist
python -m venv autogen_env
autogen_env\Scripts\activate  # On Windows
pip install -r requirements.txt



Execute 
```bash
python main.py 
Or ( for individual bot )
python main.py --mode screenshot
python main.py --mode devops
python main.py --mode coder
```

🖼️ Screenshot Mode
Purpose:
Feed screen content to LLM and get suggestions.

Steps:
Save a screenshot as: assets/screenshot.png

Run:

```bash
python main.py --mode screenshot
```

⚙️ DevOps Mode
Purpose:
Give DevOps instructions (e.g., write Ansible playbook).

```bash
python main.py --mode devops
```
The assistant will answer and ask:

Would you like to continue or end the conversation?

👨‍💻 Coder Mode
Purpose:
Multi-agent planner → coder → reviewer → user approval loop.

```bash
python main.py --mode coder
```bash
Optimized for building and reviewing code in steps via local LLM.


🚫 Limitations
Docker-based code execution is disabled (use_docker: False)

Tesseract must be installed and properly referenced

Only .png screenshots are supported (customizable)
