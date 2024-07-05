from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel
from .person import Person


@JsonMap({})
class Byline(BaseModel):
    """Byline

    :param original: original, defaults to None
    :type original: str, optional
    :param person: person, defaults to None
    :type person: List[Person], optional
    :param organization: organization, defaults to None
    :type organization: str, optional
    """

    def __init__(
        self,
        original: str = None,
        person: List[Person] = None,
        organization: str = None,
    ):
        if original is not None:
            self.original = original
        if person is not None:
            self.person = self._define_list(person, Person)
        if organization is not None:
            self.organization = organization
