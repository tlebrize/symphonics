import json
from app.settings import settings

class DeviceService():
	def __init__(self, publisher):
		self.publisher = publisher
		self.topic_path = publisher.topic_path('symphonics-test', settings.PUBSUB_TOPIC)

	def switch(self, *, switch, devId):
		message = json.dumps({"switch": switch, "devId": devId})
		return self.publisher.publish(
			self.topic_path,
			message.encode("utf-8")
		).result()

