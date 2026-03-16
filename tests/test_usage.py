import pytest
import datetime
from app.models import MessageDataModel


@pytest.fixture()
def message():
    return MessageDataModel(
        **{
            "devId": "string",
            "dataId": "string",
            "productId": "string",
            "properties": [{"code": "temp_interior", "dpId": 0, "time": 0, "value": 0}],
        }
    )


def test_usage_insert(usage_service, message):
    usage_service.save(message)
    assert list(usage_service.list()) == [
        {
            "devId": "string",
            "productId": "string",
            "code": "temp_interior",
            "value": 0,
            "time": datetime.datetime(1970, 1, 1, 1, 0),
        }
    ]


@pytest.fixture()
def large_message():
    return MessageDataModel(
        **{
            "devId": "string",
            "dataId": "string",
            "productId": "string",
            "properties": [
                {"code": "temp_interior", "dpId": 0, "time": i * 1800, "value": i * 100}
                for i in range(64)
            ],
        }
    )


def test_usage_report(usage_service, large_message):
    usage_service.save(large_message)

    report = usage_service.report()

    assert report['1970-01-01']['01:00'] == 100
    assert report['1970-01-01']['12:00'] == 4500
    assert report['1970-01-01']['23:00'] == 8900
    assert report['1970-01-02']['00:00'] == 9300
    assert report['1970-01-02']['08:00'] == 12500
