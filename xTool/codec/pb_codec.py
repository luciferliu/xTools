# -*- coding: utf-8 -*-

from xTool.plugins.plugin import register_plugin, PluginType
from .codec_type import CodecType


@register_plugin(
    PluginType.CODEC, CodecType.PB
)
class ProtocCodec:
    @classmethod
    def encode(cls, obj: object) -> bytes:
        return obj.SerializeToString()

    @classmethod
    def decode(cls, obj: object, data: bytes) -> None:
        obj.ParseFromString(data)
