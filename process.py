


import tensorflow as tf
from anndata import read_h5ad
from scaden.model.functions import get_signature_genes, preprocess_h5ad_data
import numpy as np
import pandas as pd


def processing(data_path, training_data, processed_path, var_cutoff):

    raw_input = read_h5ad(training_data)
    print(raw_input.obs)
    print(raw_input.var_names)
    print(raw_input.uns)
    print(raw_input.X)
    rawinputX=pd.DataFrame(raw_input.X)
    print(rawinputX)
    part=rawinputX.iloc[0:,[0,1]]
    print(part)
    sig_genes_complete = list(raw_input.var_names)
    sig_genes = get_signature_genes(input_path=data_path, sig_genes_complete=sig_genes_complete, var_cutoff=var_cutoff)

    preprocess_h5ad_data(raw_input_path=training_data,
                         processed_path=processed_path,
                         sig_genes=sig_genes)

processing(data_path='D:/data/master/code_cbcconcnn/cbcconmodel_canrun/sample_label/PBMC2_monaco/monaco_samples.txt', training_data='D:/data/master/code_cbcconcnn/processeddata/pbmc_data.h5ad', processed_path='D:/data/master/code_cbcconcnn/processeddata/processed_PBMC2_Monaca.h5ad', var_cutoff=0)
