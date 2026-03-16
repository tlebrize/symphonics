from google.cloud import bigquery
from google.cloud.bigquery.enums import SqlTypeNames as t

from app.settings import settings


def migrate(db):
    db.create_table(
        bigquery.Table(
            f'symphonics-test.{settings.DB_DATASET}.usage',
            schema=[
                bigquery.SchemaField("devId", t.STRING, mode="REQUIRED"),
                bigquery.SchemaField("productId", t.STRING, mode="REQUIRED"),
                bigquery.SchemaField("code", t.STRING, mode="REQUIRED"),
                bigquery.SchemaField("value", t.INTEGER, mode="REQUIRED"),
                bigquery.SchemaField("time", t.DATETIME, mode="REQUIRED"),
            ],
        )
    )


def destroy(db):
    db.delete_table(f'symphonics-test.{settings.DB_DATASET}.usage')
