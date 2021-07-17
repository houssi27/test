from dataclasses import asdict, dataclass
import typing


class EntityBase:
    def asdict(self):
        return asdict(self)


@dataclass
class PrivatePerson(EntityBase):
    first_name: str
    last_name: str
    city: str


class PublicPerson(object):
    def __init__(self, first_name: str, last_name, c: str):
        self.firstName = first_name
        self.lastName = last_name
        self.city = c
        self.year = None

    def asdict(self) -> typing.Dict[str, str]:
        return {
            "first_name": self.firstName,
            "last_name": self.lastName,
            "city": self.city,
        }


@dataclass
class organization(EntityBase):
    name: str
    city: str


@dataclass
class Other(EntityBase):
    name: str
