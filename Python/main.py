import abc
import json
import typing
import xml.etree.ElementTree as et


class BaseSerializer(abc.ABC):
    @abc.abstractmethod
    def serialize(self, obj: typing.Any) -> str:
        pass


class JsonSerializer(BaseSerializer):
    def serialize(self, obj: typing.Any) -> str:
        if isinstance(obj, list):
            return json.dumps([row.asdict() for row in obj])
        return json.dumps(obj.asdict())


class XmlSerializer(BaseSerializer):
    def __init__(self):
        self._element = None

    def _start_xml(self):
        self._element = et.Element('data')

    def serialize(self, obj: typing.Union[typing.Any, typing.List[typing.Any]]):
        self._start_xml()
        if isinstance(obj, list):
            for row in obj:
                self._serialize_single_object(row)
        else:
            self._serialize_single_object(obj)
        return et.tostring(self._element, encoding='unicode')

    def _serialize_single_object(self, obj: typing.Any):
        parent_element = self._add_property(self._element, str(
            obj.__class__.__name__), attrib={'id': str(id(obj))})
        for k, v in obj.asdict().items():
            self._add_property(parent_element, k, v)

    def _add_property(self, parent_element, name, value=None, attrib={}):
        prop = et.SubElement(parent_element, name, attrib=attrib)
        if value:
            prop.text = value
        return prop
