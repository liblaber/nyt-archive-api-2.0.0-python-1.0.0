from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap({})
class Person(BaseModel):
    """Person

    :param firstname: firstname, defaults to None
    :type firstname: str, optional
    :param middlename: middlename, defaults to None
    :type middlename: str, optional
    :param lastname: lastname, defaults to None
    :type lastname: str, optional
    :param qualifier: qualifier, defaults to None
    :type qualifier: str, optional
    :param title: title, defaults to None
    :type title: str, optional
    :param role: role, defaults to None
    :type role: str, optional
    :param organization: organization, defaults to None
    :type organization: str, optional
    :param rank: rank, defaults to None
    :type rank: int, optional
    """

    def __init__(
        self,
        firstname: str = None,
        middlename: str = None,
        lastname: str = None,
        qualifier: str = None,
        title: str = None,
        role: str = None,
        organization: str = None,
        rank: int = None,
    ):
        if firstname is not None:
            self.firstname = firstname
        if middlename is not None:
            self.middlename = middlename
        if lastname is not None:
            self.lastname = lastname
        if qualifier is not None:
            self.qualifier = qualifier
        if title is not None:
            self.title = title
        if role is not None:
            self.role = role
        if organization is not None:
            self.organization = organization
        if rank is not None:
            self.rank = rank
