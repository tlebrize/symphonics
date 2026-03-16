class MessageService:
    def __init__(self, db):
        self.db = db

    def save(self, data):
        print(data)
