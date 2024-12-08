# Text Summarization

## Overview

This repository demonstrates how to use the t5_samsum_summarization model from the Hugging Face Transformers library to summarize conversational text.

## Features

- Summarize multi-turn conversations into concise summaries.
- Built with Hugging Face Transformers and Streamlit for an interactive web interface.
- Compatible with TensorFlow as backends.


## Installation and Usage 

To set up the  **Text Summarization** locally, follow these steps:

1. **Clone the Repository**:
```bash
 git clone https://github.com/Raanjeetsgolu/text-summarization
 cd text-summarization
```

2. **Install Dependencies**:
Make sure you have Python installed, then install the required packages:

```bash
pip install -r requirements.txt
```
3. **Run the streamlit application**:

```bash
streamlit run app.py
```

4. Access the App: Open your browser and navigate to `http://127.0.0.1:8501`.

## 🐳 Docker setup


**Option 1: Pull from Docker Hub**

```bash
docker run -td -p 8501:8501 --name text-summarization-app  raanjeetsgolu/text-summarization-app:3.0-1
```
Access the application: Open your browser and navigate to `http://127.0.0.1:8501`.

**Option 2: Build Locally**


1.***Build the Docker image***:

```bash
docker build -t text-summarization-app  .
  ```
2.***Run the Docker container***:

   ```bash
docker run -td -p 8501:8501 --name text-summarization-app text-summarization-app
   ```

3.***Access the application***:
 Open your browser and navigate to http://127.0.0.1:8501

## 🛠 Technologies

+ Python 3.10
+ Streamlit (for the web server)
+ Docker (for containerization)

## Model Information

This T5 Transformer model is fine-tuned on the SAMSum dataset, specifically designed for summarizing conversations.