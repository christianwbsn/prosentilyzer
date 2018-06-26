# Prosentilyzer
#### Product Review Sentiment Analyzer

----
## Description
    This repository is a task for Graphics and Artificial Intelligence Laboratory assistant selection. Build a model for sentiment analysis of product review in Bahasa Indonesia.

----
## Dataset
1. Dataset scraped from Lazada contains 2 columns

    ratings | review
    ---- | ----

2. Indonesian stopwords by [oswinrh](https://www.kaggle.com/oswinrh/indonesian-stoplist)

## Requirements
* Python 3.5
* Jupyter Notebook
* Scikit-learn
* Matplotlib
* Pandas
* Numpy
* NLTK

## Project Structure
    ```
    | input
        | raw
            | lazada_review.csv
        | preprocessed
            | lazada_review.csv
            | lazada_review_labelled.csv
        | train
            | train.csv
        | test
            | test.csv
    | src
        | scraper
            | lazada_scraper.py
    ```

## Installation
* Run the ipython notebook in jupyter notebook
    ```
    jupyter notebook
    ```

## Author
* **[Christian Wibisono](https://github.com/christianwbsn)** - 13516147
