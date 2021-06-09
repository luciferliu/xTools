# -*- coding: utf-8 -*-

import zlib

from xTool.plugins.plugin import register_plugin, PluginType
from .compress_type import CompressType


@register_plugin(
    PluginType.COMPRESS, CompressType.ZLIB
)
class ZlibCompress:
    @classmethod
    def compress(cls, data: bytes, compression_level: int = 6) -> bytes:
        if data is None:
            return data
        return zlib.compress(data, compression_level)

    @classmethod
    def decompress(cls, data: bytes) -> bytes:
        if data is None:
            return data
        return zlib.decompress(data)