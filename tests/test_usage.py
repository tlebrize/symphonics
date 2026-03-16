import pytest
import datetime
from app.models import MessageDataModel

@pytest.fixture()
def message():
    return MessageDataModel(**{
            "devId": "string",
            "dataId": "string",
            "productId": "string",
            "properties": [{"code": "temp_interior", "dpId": 0, "time": 0, "value": 0}],
    })


def test_usage_insert(usage_service, message):
	response = usage_service.save(message)
	assert list(usage_service.list()) == [
		{'devId': 'string', 'productId': 'string', 'code': 'temp_interior', 'value': 0, 'time': datetime.datetime(1970, 1, 1, 1, 0)}
	]
