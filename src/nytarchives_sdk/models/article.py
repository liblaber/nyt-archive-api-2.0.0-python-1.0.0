from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel
from .multimedia import Multimedia
from .headline import Headline
from .keyword import Keyword
from .byline import Byline


@JsonMap({})
class Article(BaseModel):
    """Article

    :param abstract: Document abstract., defaults to None
    :type abstract: str, optional
    :param lead_paragraph: Lead paragraph., defaults to None
    :type lead_paragraph: str, optional
    :param web_url: Article URL., defaults to None
    :type web_url: str, optional
    :param snippet: snippet, defaults to None
    :type snippet: str, optional
    :param print_page: Page in print (e.g. 1)., defaults to None
    :type print_page: int, optional
    :param print_section: Section in print (e.g. A)., defaults to None
    :type print_section: str, optional
    :param source: source, defaults to None
    :type source: str, optional
    :param multimedia: multimedia, defaults to None
    :type multimedia: List[Multimedia], optional
    :param headline: headline, defaults to None
    :type headline: Headline, optional
    :param keywords: keywords, defaults to None
    :type keywords: List[Keyword], optional
    :param pub_date: Publication date., defaults to None
    :type pub_date: str, optional
    :param document_type: Document type (article, multimedia)., defaults to None
    :type document_type: str, optional
    :param news_desk: Desk in the newsroom that worked on the story (Foreign, Metro, Sports, ...)., defaults to None
    :type news_desk: str, optional
    :param section_name: Section that the article appeared in (New York, Sports, World, ...)., defaults to None
    :type section_name: str, optional
    :param subsection_name: subsection_name, defaults to None
    :type subsection_name: str, optional
    :param byline: byline, defaults to None
    :type byline: Byline, optional
    :param type_of_material: Type of asset (Correction, News, Op-Ed, Review, Video, ...)., defaults to None
    :type type_of_material: str, optional
    :param _id: _id, defaults to None
    :type _id: str, optional
    :param word_count: Number of words in the article., defaults to None
    :type word_count: int, optional
    :param uri: Uniquely identifies an asset., defaults to None
    :type uri: str, optional
    """

    def __init__(
        self,
        abstract: str = None,
        lead_paragraph: str = None,
        web_url: str = None,
        snippet: str = None,
        print_page: int = None,
        print_section: str = None,
        source: str = None,
        multimedia: List[Multimedia] = None,
        headline: Headline = None,
        keywords: List[Keyword] = None,
        pub_date: str = None,
        document_type: str = None,
        news_desk: str = None,
        section_name: str = None,
        subsection_name: str = None,
        byline: Byline = None,
        type_of_material: str = None,
        _id: str = None,
        word_count: int = None,
        uri: str = None,
    ):
        if abstract is not None:
            self.abstract = abstract
        if lead_paragraph is not None:
            self.lead_paragraph = lead_paragraph
        if web_url is not None:
            self.web_url = web_url
        if snippet is not None:
            self.snippet = snippet
        if print_page is not None:
            self.print_page = print_page
        if print_section is not None:
            self.print_section = print_section
        if source is not None:
            self.source = source
        if multimedia is not None:
            self.multimedia = self._define_list(multimedia, Multimedia)
        if headline is not None:
            self.headline = self._define_object(headline, Headline)
        if keywords is not None:
            self.keywords = self._define_list(keywords, Keyword)
        if pub_date is not None:
            self.pub_date = pub_date
        if document_type is not None:
            self.document_type = document_type
        if news_desk is not None:
            self.news_desk = news_desk
        if section_name is not None:
            self.section_name = section_name
        if subsection_name is not None:
            self.subsection_name = subsection_name
        if byline is not None:
            self.byline = self._define_object(byline, Byline)
        if type_of_material is not None:
            self.type_of_material = type_of_material
        if _id is not None:
            self._id = _id
        if word_count is not None:
            self.word_count = word_count
        if uri is not None:
            self.uri = uri
