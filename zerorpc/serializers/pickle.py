#coding=utf-8
import cPickle

__author__ = 'nemo'

class Serializer(object):

    def pack(self, data):
        return cPickle.dumps(data)


    def unpack(self, blob):
        return cPickle.loads(blob)
