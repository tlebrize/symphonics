import json
from google.cloud import pubsub_v1
from app import settings

# todo too slow, most likely unreliable.
async def test_device_switch(device_service):
	def callback(message):
		message.ack()
		assert json.loads(message.data)['devId'] == '123'
		acknowledged = True

	client = pubsub_v1.SubscriberClient()
	sub_path = client.subscription_path('symphonics-test', f'{settings.PUBSUB_TOPIC}-sub')
	future = client.subscribe(sub_path, callback=callback)

	result = device_service.switch(switch=True, devId="123")

	with client:
		try:
			future.result(timeout=1.0)
		except TimeoutError:
			future.cancel()
			future.result()
