from datetime import datetime
from app.settings import settings
from collections import defaultdict


class UsageService:
    def __init__(self, db):
        self.db = db
        self.table = f"symphonics-test.{settings.DB_DATASET}.usage"

    def save(self, data):
        rows = []
        for property in data.properties:
            rows.append(
                {
                    "code": property.code.value,
                    "value": property.value,
                    "time": datetime.fromtimestamp(property.time).isoformat(),
                    "devId": data.devId,
                    "productId": data.productId,
                }
            )
        self.db.load_table_from_json(rows, self.table).result()
        return rows

    def list(self):
        for row in self.db.query(f"select * from `{self.table}`"):
            yield dict(row)

    def report(self):
        data = defaultdict(dict)

        for row in self.db.query(f"""
            SELECT
              sum(value) as value,
              FORMAT_TIMESTAMP('%Y-%m-%d', time) AS date,
              FORMAT_TIMESTAMP('%H', time) AS hour
            FROM `{self.table}`
            GROUP BY date, hour
            ORDER BY date, hour
        """):
            data[row.date][f"{row.hour}:00"] = row.value

        return data
