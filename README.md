Cassava-Genomics-Hack-Ai-model
About
This project focuses on leveraging the natural resistance of cassava to drought by studying its DNA and identifying specific sequences called enhancers that play a role in gene regulation. Participants will use a dataset containing 10,000-base pair DNA sequences from the cassava genome, along with associated information such as the chromosome and a target label indicating whether a specific region overlaps with an enhancer. The goal is to build predictive models for enhancer regulatory activity in the cassava genome. The project relies on a combination of genomics, natural language processing, and machine learning techniques, making use of pre-trained NLP models specifically designed to analyze DNA sequences. The competition's evaluation metric is accuracy, and participants are provided with mean-pooled embeddings of a specialized NLP model for their analysis.

Dataset
Each training sample is a 1000-base pair (bp) DNA sequence fetched from the cassava genome. The sequences are represented as a string of 1000 letters corresponding to the nucleotides (i.e., A, G, C, & T for the 4 nucleotide bases). For each sample, the associated class is labeled as 1 (positive) if the middle 200 bp region of the given sequence overlaps with an enhancer region by more than 50% of its length. Otherwise, it is labeled as 0 (negative). To strictly divide the training and test sets in a non-overlapping manner, we split them up by chromosomes, which are distinct organizational units of the cassava genome.

The dataset consists of a CSV file with the following columns:

ID: Unique ID for each row.
Sequence: 1000-base pair DNA sequence.
Chromosome: Distinct organizational units of the cassava genome.
Region: The region of the considered Sequence.
Target: This is what you are predicting: 1 if the middle 200 bp region of the given sequence overlaps with an enhancer region by more than 50% of its length. Otherwise, 0.
The training dataset consists of 13,225 sequences with roughly balanced classes, containing 6,464 positive and 6,761 negative sequences. The test dataset contains 5,668 sequences. The public leaderboard represents approximately 30% of the test data.

In addition to the CSV files, mean-pooled embeddings of InstaDeep’s AgroNT model are provided. These embeddings are calculated by passing the nucleotide sequence through AgroNT, taking the hidden representation of the sequence at the final layer (layer 40), and taking the mean along the sequence length. This results in a 1500-dimensional embedding for each sequence. These embeddings are provided in Train_embeddings.npy and Test_embeddings.npy files, following the same order as the Train and Test CSV files respectively. These files are saved as Numpy arrays; use np.load(...) to read them in. See the starter notebook for an example of how to use them!

Project Workflow
Setting Up Environment:

Import necessary libraries and mount Google Drive.
