"""
This module describes the most basic usage of Surprise: you define a prediction
algorithm, (down)load a dataset and run a cross-validation procedure.
"""


from surprise import Dataset, SVD
from surprise.model_selection import cross_validate


# Load the movielens-100k dataset (download it if needed),
data = Dataset.load_builtin("ml-100k")

# We'll use the famous SVD algorithm.
algo = SVD()

# Run 5-fold cross-validation and print results
cross_validate(algo, data, measures=["RMSE", "MAE"], cv=5, verbose=True)
