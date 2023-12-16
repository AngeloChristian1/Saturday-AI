<div id="top"></div>
<!-- PROJECT LOGO -->
<br />
<div align="center">
   <a href="#">
    <img src="![image](https://github.com/Eddy-dashner/Cassava-Genomics-Hack-Ai-model/assets/126165275/1a11809b-d1af-462e-93f5-f0ceea9a903e)
" alt="Logo" width="100" height="100">
   </a>
<h3 align="center">Cassava Genomic Analysis</h3>
  <p align="center">
    AI for our final for AI saturday
    <br />
    <a href="https://your-demo-url.com/"><strong>View Demo</strong></a>
  </p>
</div>
<!-- ABOUT THE PROJECT -->
## About The Project
This project focuses on leveraging the natural resistance of cassava to drought by studying its DNA and identifying specific sequences called enhancers that play a role in gene regulation. Participants will use a dataset containing 10,000-base pair DNA sequences from the cassava genome, along with associated information such as the chromosome and a target label indicating whether a specific region overlaps with an enhancer. The goal is to build predictive models for enhancer regulatory activity in the cassava genome. The project relies on a combination of genomics, natural language processing, and machine learning techniques, making use of pre-trained NLP models specifically designed to analyze DNA sequences.

### Features
* Genomic sequence analysis.
* Machine learning for enhancer prediction.
* Utilizes InstaDeep’s AgroNT model embeddings.
* Explore and visualize genomic data.
* Evaluate models with mean-pooled embeddings.

## Built With

#### Technologies

*Python
*Numpy
*Pandas
*Matplotlib
*Seaborn
*TensorFlow
*Third party code
*InstaDeep’s AgroNT
*Tools
*Jupyter Notebooks
*Google Colab
*GitHub
<p align="right">(<a href="#top">back to top</a>)</p>
<!-- GETTING STARTED -->
## Setting Up Environment:

Import necessary libraries and mount Google Drive.
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import statsmodels.api as sm
from google.colab import drive
drive.mount('/content/drive')

## Loading and Exploring Data:

Load CSV files and embeddings.

train = pd.read_csv("/content/drive/MyDrive/Cassava Project/Train.csv")
test_data = pd.read_csv("/content/drive/MyDrive/Cassava Project/Test.csv")
train_embeddings = np.load("/content/drive/MyDrive/Cassava Project/Train_embeddings.npy")
test_embeddings = np.load("/content/drive/MyDrive/Cassava Project/Test_embeddings.npy")

## Preprocessing Data:

Check for missing values, explore target distribution, and preprocess DNA sequences.

# Check for missing values
print('Missing values:', train.isnull().sum())

# Explore Target distribution
sns.catplot(x="Target", kind="count", data=train)

# Preprocess DNA sequences for training and test data
# (One-hot encoding)


