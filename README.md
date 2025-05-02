# 🍕 Pizza Review QA Bot

This project is a Question-Answering (QA) bot designed to answer questions about a pizza restaurant using realistic customer reviews. It uses [LangChain](https://www.langchain.com/), [Ollama](https://ollama.com/), and [Chroma](https://www.trychroma.com/) to provide contextual answers from a vector database built from real review data.

---

## 📌 About

This bot performs the following:

- Embeds restaurant reviews using `mxbai-embed-large`
- Stores them in a Chroma vector database
- Uses `llama3.2` via Ollama for local question answering
- Retrieves the top 5 relevant reviews to inform each answer

---

## ⚙️ How It Works

1. The app reads review data from a CSV file.
2. It generates embeddings using Ollama.
3. It stores them using Chroma DB.
4. It runs a command-line chatbot that:
   - Takes a question
   - Retrieves the top matching reviews
   - Answers with the help of a local LLM (Llama3.2)

---

## 🧪 Example Questions

- "Is the pizza crust crispy?"
- "What do people say about the prices?"
- "How is the service at this restaurant?"

---

## 📁 Project Structure

```bash
├── main.py                           # Chat loop
├── vector.py                         # Vector database setup
├── realistic_restaurant_reviews.csv  # Source data
├── chrome_langchain_db/              # Vector DB (auto-created)
├── README.md                         # This file
├── LICENSE                           # MIT License
````

---

## 🚀 Running the Project

### 1. **Install dependencies**:

Make sure you have Python 3.x installed, then install the required dependencies:

```bash
pip install -r requirements.txt
```

### 2. **Make sure Ollama is running with the required models**:

Run the following commands to start the models needed for the bot:

```bash
ollama run llama3
ollama run mxbai-embed-large
```

### 3. **Run the chatbot**:

Finally, run the chatbot script:

```bash
python main.py
```

You can ask questions related to the pizza restaurant, and the bot will answer using reviews from the vector database. Type `q` to quit the chat.

---

## 📄 License

MIT License

Copyright (c) \2025 \Hadil Sghaier

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the “Software”), to deal
in the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
of the Software, and to permit persons to whom the Software is furnished to do
so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES, OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

```


