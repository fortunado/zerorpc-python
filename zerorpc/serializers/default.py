#coding=utf-8
import msgpack

__author__ = 'nemo'

class Serializer(object):

    def pack(self, data):
        return msgpack.Packer().pack(data)

    def unpack(self, blob):
        unpacker = msgpack.Unpacker()
        unpacker.feed(blob)
        return unpacker.unpack()
