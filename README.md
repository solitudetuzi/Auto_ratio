# Auto_ratio
Predicting the cell-ratio of the tissue
# Introduction
An algorithm for deconvolution of cells using deeplearning, trained using simulated single-cell RNA data, and making predictions on bulk RNA data.
# System Requirments
Hardware Requirments: Autoptcr requires only a standard computer with approximately 16 GB RAM to support the in-memory operations.
* Python      3.8
* Tensorflow	1.10.0
* Scanpy	    1.2.2
* Pandas	    0.23.4
* Numpy	      1.15.0
* Scipy      	1.1.0
* Anndata	    0.6.9
# Installation
Download the code directly from the github link and configure the environment on the development platform to run. We recommend using anaconda to configure the environment.
# Execute
## First perform data preprocessing, removing some useless genes
  processing(data_path, training_data, processed_path, var_cutoff)
## Put the data data into the deep learning model for model training
training(data_path, train_datasets, model_dir, batch_size, learning_rate, num_steps)
## Predictions are made on real BUlk RNA data
prediction(model_dir, data_path)
# Contact
You are welcome to:
* email: 15210265602@163.com
