# -*- coding:utf-8 -*-

from rest_framework import serializers


class ResponseInfo(object):
    def __init__(self, height=None, width=None):
        self.height = height
        self.width = width

class ResponseSerializer(serializers.Serializer):
    height = serializers.IntegerField()
    width = serializers.IntegerField()

