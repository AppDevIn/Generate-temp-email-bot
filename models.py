# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = mail_from_dict(json.loads(json_string))

from dataclasses import dataclass
from typing import Optional, Any, List, TypeVar, Callable, Type, cast


T = TypeVar("T")


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def from_none(x: Any) -> Any:
    assert x is None
    return x


def from_union(fs, x):
    for f in fs:
        try:
            return f(x)
        except:
            pass
    assert False


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


def from_float(x: Any) -> float:
    assert isinstance(x, (float, int)) and not isinstance(x, bool)
    return float(x)


def to_float(x: Any) -> float:
    assert isinstance(x, float)
    return x


@dataclass
class CreatedAt:
    milliseconds: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'CreatedAt':
        assert isinstance(obj, dict)
        milliseconds = from_union([from_int, from_none], obj.get("milliseconds"))
        return CreatedAt(milliseconds)

    def to_dict(self) -> dict:
        result: dict = {}
        result["milliseconds"] = from_union([from_int, from_none], self.milliseconds)
        return result


@dataclass
class ID:
    oid: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'ID':
        assert isinstance(obj, dict)
        oid = from_union([from_str, from_none], obj.get("oid"))
        return ID(oid)

    def to_dict(self) -> dict:
        result: dict = {}
        result["oid"] = from_union([from_str, from_none], self.oid)
        return result


@dataclass
class Attachment:
    filename: Optional[str] = None
    id: Optional[int] = None
    size: Optional[int] = None
    mimetype: Optional[str] = None
    cid: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Attachment':
        assert isinstance(obj, dict)
        filename = from_union([from_str, from_none], obj.get("filename"))
        id = from_union([from_int, from_none], obj.get("_id"))
        size = from_union([from_int, from_none], obj.get("size"))
        mimetype = from_union([from_str, from_none], obj.get("mimetype"))
        cid = from_union([from_str, from_none], obj.get("cid"))
        return Attachment(filename, id, size, mimetype, cid)

    def to_dict(self) -> dict:
        result: dict = {}
        result["filename"] = from_union([from_str, from_none], self.filename)
        result["_id"] = from_union([from_int, from_none], self.id)
        result["size"] = from_union([from_int, from_none], self.size)
        result["mimetype"] = from_union([from_str, from_none], self.mimetype)
        result["cid"] = from_union([from_str, from_none], self.cid)
        return result


@dataclass
class MailAttachments:
    attachment: Optional[List[Attachment]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'MailAttachments':
        assert isinstance(obj, dict)
        attachment = from_union([lambda x: from_list(Attachment.from_dict, x), from_none], obj.get("attachment"))
        return MailAttachments(attachment)

    def to_dict(self) -> dict:
        result: dict = {}
        result["attachment"] = from_union([lambda x: from_list(lambda x: to_class(Attachment, x), x), from_none], self.attachment)
        return result


@dataclass
class Datum:
    id: Optional[ID] = None
    created_at: Optional[CreatedAt] = None
    mail_id: Optional[str] = None
    mail_address_id: Optional[str] = None
    mail_from: Optional[str] = None
    mail_subject: Optional[str] = None
    mail_preview: Optional[str] = None
    mail_text_only: Optional[str] = None
    mail_text: Optional[str] = None
    mail_html: Optional[str] = None
    mail_timestamp: Optional[float] = None
    mail_attachments_count: Optional[int] = None
    mail_attachments: Optional[MailAttachments] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Datum':
        assert isinstance(obj, dict)
        id = from_union([ID.from_dict, from_none], obj.get("_id"))
        created_at = from_union([CreatedAt.from_dict, from_none], obj.get("createdAt"))
        mail_id = from_union([from_str, from_none], obj.get("mail_id"))
        mail_address_id = from_union([from_str, from_none], obj.get("mail_address_id"))
        mail_from = from_union([from_str, from_none], obj.get("mail_from"))
        mail_subject = from_union([from_str, from_none], obj.get("mail_subject"))
        mail_preview = from_union([from_str, from_none], obj.get("mail_preview"))
        mail_text_only = from_union([from_str, from_none], obj.get("mail_text_only"))
        mail_text = from_union([from_str, from_none], obj.get("mail_text"))
        mail_html = from_union([from_str, from_none], obj.get("mail_html"))
        mail_timestamp = from_union([from_float, from_none], obj.get("mail_timestamp"))
        mail_attachments_count = from_union([from_int, from_none], obj.get("mail_attachments_count"))
        mail_attachments = from_union([MailAttachments.from_dict, from_none], obj.get("mail_attachments"))
        return Datum(id, created_at, mail_id, mail_address_id, mail_from, mail_subject, mail_preview, mail_text_only, mail_text, mail_html, mail_timestamp, mail_attachments_count, mail_attachments)

    def to_dict(self) -> dict:
        result: dict = {}
        result["_id"] = from_union([lambda x: to_class(ID, x), from_none], self.id)
        result["createdAt"] = from_union([lambda x: to_class(CreatedAt, x), from_none], self.created_at)
        result["mail_id"] = from_union([from_str, from_none], self.mail_id)
        result["mail_address_id"] = from_union([from_str, from_none], self.mail_address_id)
        result["mail_from"] = from_union([from_str, from_none], self.mail_from)
        result["mail_subject"] = from_union([from_str, from_none], self.mail_subject)
        result["mail_preview"] = from_union([from_str, from_none], self.mail_preview)
        result["mail_text_only"] = from_union([from_str, from_none], self.mail_text_only)
        result["mail_text"] = from_union([from_str, from_none], self.mail_text)
        result["mail_html"] = from_union([from_str, from_none], self.mail_html)
        result["mail_timestamp"] = from_union([to_float, from_none], self.mail_timestamp)
        result["mail_attachments_count"] = from_union([from_int, from_none], self.mail_attachments_count)
        result["mail_attachments"] = from_union([lambda x: to_class(MailAttachments, x), from_none], self.mail_attachments)
        return result


@dataclass
class Mail:
    error: Optional[str] = None
    data: Optional[List[Datum]] = None

    def hasData(self) -> bool:
        return self.data is []

    @staticmethod
    def from_dict(obj: Any) -> 'Mail':
        assert isinstance(obj, dict)
        error = from_union([from_str, from_none], obj.get("error"))
        data = from_union([lambda x: from_list(Datum.from_dict, x), from_none], obj.get("data"))
        return Mail(error, data)

    def to_dict(self) -> dict:
        result: dict = {}
        result["error"] = from_union([from_str, from_none], self.error)
        result["data"] = from_union([lambda x: from_list(lambda x: to_class(Datum, x), x), from_none], self.data)
        return result


def mail_from_dict(s: Any) -> Mail:
    return Mail.from_dict(s)


def mail_to_dict(x: Mail) -> Any:
    return to_class(Mail, x)
