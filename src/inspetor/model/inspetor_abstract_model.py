import base64
import re
from datetime import datetime
from src.inspetor.exception.model_exception.inspetor_general_exception import InspetorGeneralException


class InspetorAbstractModel(object):

    def encodeArray(self, array, isObject):
        encodedArray = []
        if array is None:
            return None
        for item in array:
            if isObject is True:
                encodedArray.append(self.encodeObject(item))
            else:
                encodedArray.append(self.encodeData(item))
        return

    def encodeData(self, data):
        if data is not None:
            # We have to make data an string so we can incode a bool
            data = str(base64.b64encode(str(data).encode("utf-8")), "utf-8")

        return data

    def encodeObject(self, object):
        if object is not None:
            return object.jsonSerialize()

        return object

    def inspetorDateFormatter(self, timestamp):
        if timestamp is None:
            return None

        if not isinstance(int(timestamp), int):
            raise InspetorGeneralException(
                InspetorGeneralException.WRONG_TIMESTAMP_TYPE
            )

        return datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%dT%H:%M:%S+0000')

    def onlyNumbersFormat(self, data):
        if data is not None:
            return str(re.match(r'^([\d]+)$', data))

        return data