# This file was generated by liblab | https://liblab.com/

from .services.archive import ArchiveService
from .net.environment import Environment


class NytArchives:
    def __init__(self, api_key: str = None, base_url: str = Environment.DEFAULT.value):
        """
        Initializes NytArchives the SDK class.
        """
        self.archive = ArchiveService(base_url=base_url)
        self.set_additional_variables(api_key)

    def set_base_url(self, base_url):
        """
        Sets the base URL for the entire SDK.
        """
        self.archive.set_base_url(base_url)

        return self

    def set_additional_variables(self, api_key: str = None):
        """
        Sets the additional variables for the entire SDK.
        """
        self.archive.set_additional_variables(api_key)

        return self


# c029837e0e474b76bc487506e8799df5e3335891efe4fb02bda7a1441840310c
