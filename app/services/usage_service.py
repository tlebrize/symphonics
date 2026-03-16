from datetime import datetime
from app.settings import settings

class UsageService:
    def __init__(self, db):
        self.db = db
        self.table = f'symphonics-test.{settings.DB_DATASET}.usage'

    def save(self, data):
        rows = []
        for property in data.properties:
            rows.append({
                "code": property.code.value,
                "value": property.value,
                "time": datetime.fromtimestamp(property.time).isoformat(),
                "devId": data.devId,
                "productId": data.productId,
            })
        return self.db.load_table_from_json(rows, self.table).result()


    def list(self):
        for row in self.db.query(f'select * from `{self.table}`'):
            yield dict(row)
