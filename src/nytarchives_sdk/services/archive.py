from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..models.utils.cast_models import cast_models
from ..models.get_by_year_month_json_ok_response import GetByYearMonthJsonOkResponse


class ArchiveService(BaseService):

    @cast_models
    def get_by_year_month_json(
        self, year: int, month: int
    ) -> GetByYearMonthJsonOkResponse:
        """Pass in year and month and get back JSON with all articles for that month. The response can be big (~20 megabytes) and contain thousands of articles, depending on the year and month.

        :param year: Year: 1851-2019
        :type year: int
        :param month: Year: 1-12
        :type month: int
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: An array of articles.
        :rtype: GetByYearMonthJsonOkResponse
        """

        Validator(int).validate(year)
        Validator(int).validate(month)

        serialized_request = (
            Serializer(
                f"{self.base_url}/{{year}}/{{month}}.json", self.get_default_headers()
            )
            .add_path("year", year)
            .add_path("month", month)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)

        return GetByYearMonthJsonOkResponse._unmap(response)
