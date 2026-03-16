from google.cloud import bigquery


def get_db():
    return bigquery.Client()
