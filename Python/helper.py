import typing
import logging

import serializer_factory

logger = logging.getLogger(__name__)


def exportTo(serialization_format: str, data: typing.List):
    serializer = serializer_factory.factory.get_serializer(
        serialization_format)

    return serializer.serialize(data)
