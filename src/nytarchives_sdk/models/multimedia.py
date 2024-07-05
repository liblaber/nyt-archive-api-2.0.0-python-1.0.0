from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap({})
class Legacy(BaseModel):
    """Legacy

    :param xlarge: xlarge, defaults to None
    :type xlarge: str, optional
    :param xlargewidth: xlargewidth, defaults to None
    :type xlargewidth: int, optional
    :param xlargeheight: xlargeheight, defaults to None
    :type xlargeheight: int, optional
    :param thumbnail: thumbnail, defaults to None
    :type thumbnail: str, optional
    :param thumbnailwidth: thumbnailwidth, defaults to None
    :type thumbnailwidth: int, optional
    :param thumbnailheight: thumbnailheight, defaults to None
    :type thumbnailheight: int, optional
    """

    def __init__(
        self,
        xlarge: str = None,
        xlargewidth: int = None,
        xlargeheight: int = None,
        thumbnail: str = None,
        thumbnailwidth: int = None,
        thumbnailheight: int = None,
    ):
        if xlarge is not None:
            self.xlarge = xlarge
        if xlargewidth is not None:
            self.xlargewidth = xlargewidth
        if xlargeheight is not None:
            self.xlargeheight = xlargeheight
        if thumbnail is not None:
            self.thumbnail = thumbnail
        if thumbnailwidth is not None:
            self.thumbnailwidth = thumbnailwidth
        if thumbnailheight is not None:
            self.thumbnailheight = thumbnailheight


@JsonMap({"sub_type": "subType", "type_": "type"})
class Multimedia(BaseModel):
    """Multimedia

    :param rank: rank, defaults to None
    :type rank: int, optional
    :param subtype: subtype, defaults to None
    :type subtype: str, optional
    :param sub_type: sub_type, defaults to None
    :type sub_type: str, optional
    :param caption: caption, defaults to None
    :type caption: str, optional
    :param credit: credit, defaults to None
    :type credit: str, optional
    :param type_: type_, defaults to None
    :type type_: str, optional
    :param url: url, defaults to None
    :type url: str, optional
    :param height: height, defaults to None
    :type height: int, optional
    :param width: width, defaults to None
    :type width: int, optional
    :param legacy: legacy, defaults to None
    :type legacy: Legacy, optional
    :param crop_name: crop_name, defaults to None
    :type crop_name: str, optional
    """

    def __init__(
        self,
        rank: int = None,
        subtype: str = None,
        sub_type: str = None,
        caption: str = None,
        credit: str = None,
        type_: str = None,
        url: str = None,
        height: int = None,
        width: int = None,
        legacy: Legacy = None,
        crop_name: str = None,
    ):
        if rank is not None:
            self.rank = rank
        if subtype is not None:
            self.subtype = subtype
        if sub_type is not None:
            self.sub_type = sub_type
        if caption is not None:
            self.caption = caption
        if credit is not None:
            self.credit = credit
        if type_ is not None:
            self.type_ = type_
        if url is not None:
            self.url = url
        if height is not None:
            self.height = height
        if width is not None:
            self.width = width
        if legacy is not None:
            self.legacy = self._define_object(legacy, Legacy)
        if crop_name is not None:
            self.crop_name = crop_name
