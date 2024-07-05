from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap({})
class Headline(BaseModel):
    """Headline

    :param main: main, defaults to None
    :type main: str, optional
    :param kicker: kicker, defaults to None
    :type kicker: str, optional
    :param content_kicker: content_kicker, defaults to None
    :type content_kicker: str, optional
    :param print_headline: print_headline, defaults to None
    :type print_headline: str, optional
    :param name: name, defaults to None
    :type name: str, optional
    :param seo: seo, defaults to None
    :type seo: str, optional
    :param sub: sub, defaults to None
    :type sub: str, optional
    """

    def __init__(
        self,
        main: str = None,
        kicker: str = None,
        content_kicker: str = None,
        print_headline: str = None,
        name: str = None,
        seo: str = None,
        sub: str = None,
    ):
        if main is not None:
            self.main = main
        if kicker is not None:
            self.kicker = kicker
        if content_kicker is not None:
            self.content_kicker = content_kicker
        if print_headline is not None:
            self.print_headline = print_headline
        if name is not None:
            self.name = name
        if seo is not None:
            self.seo = seo
        if sub is not None:
            self.sub = sub
