from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel
from .article import Article


@JsonMap({})
class Meta(BaseModel):
    """Meta

    :param hits: hits, defaults to None
    :type hits: int, optional
    """

    def __init__(self, hits: int = None):
        if hits is not None:
            self.hits = hits


@JsonMap({})
class Response(BaseModel):
    """Response

    :param meta: meta, defaults to None
    :type meta: Meta, optional
    :param docs: docs, defaults to None
    :type docs: List[Article], optional
    """

    def __init__(self, meta: Meta = None, docs: List[Article] = None):
        if meta is not None:
            self.meta = self._define_object(meta, Meta)
        if docs is not None:
            self.docs = self._define_list(docs, Article)


@JsonMap({})
class GetByYearMonthJsonOkResponse(BaseModel):
    """GetByYearMonthJsonOkResponse

    :param copyright: copyright, defaults to None
    :type copyright: str, optional
    :param response: response, defaults to None
    :type response: Response, optional
    """

    def __init__(self, copyright: str = None, response: Response = None):
        if copyright is not None:
            self.copyright = copyright
        if response is not None:
            self.response = self._define_object(response, Response)
