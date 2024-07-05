from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap({})
class Keyword(BaseModel):
    """Keyword

    :param name: name, defaults to None
    :type name: str, optional
    :param value: value, defaults to None
    :type value: str, optional
    :param rank: rank, defaults to None
    :type rank: int, optional
    :param major: major, defaults to None
    :type major: str, optional
    """

    def __init__(
        self, name: str = None, value: str = None, rank: int = None, major: str = None
    ):
        if name is not None:
            self.name = name
        if value is not None:
            self.value = value
        if rank is not None:
            self.rank = rank
        if major is not None:
            self.major = major
