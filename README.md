# VLM Chatbot

## Overview

The VLM (Vision-Language Model) Chatbot is an advanced AI-driven assistant designed to handle:

- **Text-to-Text Question Answering:** Engage in natural language conversations.
- **PDF Question Answering:** Extract and interpret information from PDF documents.
- **Image Question Answering:** Analyze images to provide insightful responses.

Built upon the [LangChain](https://github.com/hwchase17/langchain) framework, this chatbot integrates various offline models from [Ollama](https://ollama.com/) to deliver efficient and accurate responses across multiple modalities.

## Features

- **Text-to-Text Interaction:** Seamlessly process and respond to user queries in natural language.
- **PDF Analysis:** Upload PDF files and ask questions to extract pertinent information.
- **Image Interpretation:** Submit images and receive detailed descriptions or answers to specific questions.

## Motivation

In today's data-rich environment, accessing and interpreting information from diverse sources—text, documents, and images—is crucial. This project aims to provide a unified solution that caters to:

- **Students:** Assisting in research by extracting information from academic papers.
- **Researchers:** Streamlining data retrieval from various document formats.
- **Customer Support:** Offering quick insights by analyzing product manuals or related images.

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/vlm-chatbot.git
   cd vlm-chatbot

2. **Set Up a Virtual Environment:**

  python3 -m venv venv
  source venv/bin/activate  # On Windows, use venv\Scripts\activate
  
3. **Install Dependencies:**

  pip install -r requirements.txt
  
4. Usage

  streamlit run app.py

**Challenges & Learnings**

Throughout the development of this project, we encountered and addressed several challenges:

    Latency Issues: Initial response times were high due to model complexity. We optimized by implementing efficient data processing pipelines and leveraging optimized models.
    Model Accuracy: Ensuring accurate answers across different modalities required extensive fine-tuning and validation against diverse datasets.
    Integration Hurdles: Combining various models and ensuring seamless interaction between components posed significant challenges, which we overcame through modular design and rigorous testing.

Future Scope & Improvements

Potential enhancements include:

    Advanced Models: Integrating more sophisticated models to improve accuracy and response times.
    Cloud Deployment: Transitioning to cloud-based solutions for better scalability and accessibility.
    Enhanced UI: Developing a more intuitive and user-friendly interface to improve user experience.

Contributors

We extend our gratitude to the following individuals for their invaluable contributions:

    Yash Aoute
    Ishan Zade
    Raman Gerawal
    Saurabh Ingale

