# Prosentilyzer - Product Review Sentiment Analyzer

----
## Description
This repository is a task for Graphics and Artificial Intelligence Laboratory assistant selection. Build a model for sentiment analysis of product review in Bahasa Indonesia.

----
## Dataset
1. Dataset scraped from Lazada contains 2 columns

    ratings | review
    ---- | ----

## Dictionary
1. Indonesian stopwords by [oswinrh](https://www.kaggle.com/oswinrh/indonesian-stoplist)
2. Dictionary gathered from Github [Rama Prakoso](https://github.com/ramaprakoso/analisis-sentimen)

## Requirements
* Python 3.5
* Jupyter Notebook
* Scikit-learn
* Matplotlib
* Pandas
* Numpy
* NLTK

## Project Structure
----

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py


## Installation
* Run the ipython notebook in jupyter notebook
    ```
    jupyter notebook
    ```

## Author
* **[Christian Wibisono](https://github.com/christianwbsn)** - 13516147
