from google.cloud import storage
import pandas as pd
from sklearn import linear_model
import numpy as np
import joblib

### GCP configuration - - - - - - - - - - - - - - - - - - -

# /!\ you should fill these according to your account

### GCP Project - - - - - - - - - - - - - - - - - - - - - -

# not required here

### GCP Storage - - - - - - - - - - - - - - - - - - - - - -

BUCKET_NAME = 'project_delphi_bucket'

##### Data  - - - - - - - - - - - - - - - - - - - - - - - -

# train data file location
# /!\ here you need to decide if you are going to train using the provided and uploaded data/train_1k.csv sample file
# or if you want to use the full dataset (you need need to upload it first of course)
BUCKET_TRAIN_DATA_PATH = None

##### Training  - - - - - - - - - - - - - - - - - - - - - -

# not required here

##### Model - - - - - - - - - - - - - - - - - - - - - - - -

# model folder name (will contain the folders for all trained model versions)
MODEL_NAME = 'delphi'

# model version folder name (where the trained model.joblib file will be stored)
MODEL_VERSION = 'v1'

### GCP AI Platform - - - - - - - - - - - - - - - - - - - -

# not required here

# GCP Links for streamlit app
link_current_poll = f"gs://{BUCKET_NAME}/streamlit/latest_poll.csv"
link_historic_polls = f"gs://{BUCKET_NAME}/streamlit/polls.csv"
link_tweet_kpis = f"gs://{BUCKET_NAME}/streamlit/tweet_kpis.csv"
link_most_liked_tweets = f"gs://{BUCKET_NAME}/streamlit/most_liked_tweets.csv"
link_most_retweeted_tweets = f"gs://{BUCKET_NAME}/streamlit/most_retweeted_tweets.csv"
link_logo = f"gs://{BUCKET_NAME}/streamlit/delphi_project_logo_dark.png"
link_predicition = f"gs://{BUCKET_NAME}/streamlit/prediction_database/prediction_database.csv"
link_no_of_tweets = f"gs://{BUCKET_NAME}/streamlit/no_of_tweets.csv"

