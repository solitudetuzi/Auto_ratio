

# Imports
import logging
import tensorflow as tf
from anndata import read_h5ad
from scaden.model.architectures import architectures
from  model.scaden import Scaden

logger = logging.getLogger(__name__)




def prediction(model_dir, data_path, seed=0):


    # Small model predictions
    cdn256 = Scaden(
        model_dir=model_dir + "/m256",
        model_name="m256",
        seed=seed,
        #hidden_units=M256_HIDDEN_UNITS,
        #do_rates=M256_DO_RATES,
    )
    # Predict ratios
    preds_256 = cdn256.predict(
        input_path=data_path
    )


    # Average predictions
    preds = preds_256
    preds.to_csv('scaden_predictions.txt', sep="\t")
    #logger.info(f"[bold]Created cell composition predictions: [green]{out_name}[/]")
    print('Created cell composition predictions')

