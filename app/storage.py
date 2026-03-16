from google.cloud import bigquery, pubsub_v1


def get_db():
    return bigquery.Client()

def get_publisher():
    return pubsub_v1.PublisherClient()
