# FashionFinder: Multimodal Fashion Search and Attribute Prediction

## Project Overview

FashionFinder is a multimodal fashion search and analysis tool that leverages state-of-the-art NLP and computer vision models to enable semantic search over a large collection of fashion images. Users can search for outfits by natural language descriptions and retrieve visually and semantically similar images. The project also includes tools for dataset preparation, image combination, and attribute prediction using deep learning models.

## Features

- **Semantic Search**: Search for fashion images using natural language queries.
- **Streamlit Web App**: User-friendly interface for searching and visualizing results.
- **Image Embedding & Indexing**: Uses Sentence Transformers and FAISS for efficient similarity search.
- **Attribute Prediction**: Deep learning models for predicting fashion attributes from images.
- **Dataset Preparation**: Scripts for sorting, combining, and filtering image datasets.
- **Jupyter Notebooks**: For training, embedding, and experimenting with models.

## Installation

1. **Clone the repository**
   ```bash
   git clone <repo-url>
   cd NLP_Project
   ```
2. **Install dependencies**
   It is recommended to use a virtual environment:
   ```bash
   python3 -m venv env
   source env/bin/activate
   pip install -r requirements.txt
   ```

## Usage

### 1. Prepare Data

- Use `dataSorting.py` and `combine_images.py` to organize and combine your image datasets as needed.
- Notebooks like `embedding-combinednlp.ipynb` and `nlp-combinedprojectllavafinal.ipynb` are used to generate embeddings and descriptions.

### 2. Run the Streamlit App

```bash
streamlit run StreamlitChat.py
```

- The app will launch in your browser. Enter a fashion description to search for matching images.

### 3. Notebooks

- Explore the Jupyter notebooks for training, embedding, and attribute prediction:
  - `FineTuningResnet50.ipynb`: Fine-tune ResNet50 for attribute prediction.
  - `embedding-combinednlp.ipynb`: Generate and index text embeddings for image descriptions.
  - `nlp-combinedprojectllavafinal.ipynb`: Generate unified descriptions using LLaVA.
  - `PredictingAttributes.ipynb`: Predict fashion attributes from images.

## File Structure

- `StreamlitChat.py` — Main Streamlit web app for semantic search.
- `combine_images.py` — Script to combine images from multiple sources.
- `dataSorting.py` — Script to sample and sort images for sandboxing.
- `embedding-combinednlp.ipynb`, `nlp-combinedprojectllavafinal.ipynb`, etc. — Jupyter notebooks for embedding, training, and analysis.
- `combined_images/` — Directory containing all combined images for search.
- `unifiedDescriptions.csv`, `unifiedDesc.index`, `unifiedimage_ids.pkl` — Data files for semantic search.
- `requirements.txt` — Python dependencies.

## Acknowledgements

- [Sentence Transformers](https://www.sbert.net/)
- [FAISS](https://github.com/facebookresearch/faiss)
- [Streamlit](https://streamlit.io/)
- [LLaVA](https://llava-vl.github.io/)
- [PyTorch](https://pytorch.org/)
# NLP_Project
