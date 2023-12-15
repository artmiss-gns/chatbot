# chatbot
This repository contains a Python chatbot project with a Streamlit web interface for conversations. It allows you to interact with conversational AI models like LLama through an easy-to-use chat UI.

## Overview

- `streamlit_app.py` - Streamlit web application providing chatbot UI
- `src/model_interaction.py` - Python module for calling LLama via Ollama  
- Uses [Ollama](https://github.com/jmorganca/ollama) (allows you to run open-source large language models, such as Llama 2, locally)
- LLama server runs locally to power chatbot conversations 

## Getting Started

### Prerequisites

- Python 3.7+
- [Ollama](https://github.com/jmorganca/ollama)
- LLama model installed and running locally through Ollama  
- Streamlit 

```
pip install streamlit
```
to install Ollama, check their github page for installation instructions  
    [Ollama github page](https://github.com/jmorganca/ollama)
### Usage

1. Start LLama server with Ollama

```bash
ollama run llama2
```
instead of `llama2`, you can put any other supported models by Ollama.

2. Run Streamlit app

```bash
streamlit run app.py
```

3. Chat with the bot at http://localhost:8501!

## Code Overview
**model_interaction.py**
- Makes API calls to localhost Ollama server
- Handles LLama response payload

**streamlit_app.py**

- Initializes Streamlit app
- Manages chat message state in session_state  
- Displays chat UI using Streamlit components
- Calls model_interaction to get bot responses
- Displays bot messages and responses