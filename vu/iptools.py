# -*- coding: utf-8 -*-
__author__ = 'Vadim Kravciuk, vadim@kravciuk.com'

from django.contrib.gis.geoip2 import GeoIP2

from logging import getLogger
log = getLogger(__name__)


class GeoIP:
    ip_headers = ['HTTP_X_FORWARDED_FOR', 'HTTP_X_REAL_IP', 'HTTP_CF_CONNECTING_IP']

    def __init__(self, request):
        self.gi = GeoIP2()
        self.ip = GeoIP.get_client_ip(request)
        self.ips = []

    @property
    def country(self, default=None, ip=None):
        try:
            return self.gi.country(self.ip)
        except:
            return {
               'country_code': None,
               'country_name': None,
            }

    @staticmethod
    def get_client_ip(request, get_version=False, only_remote_ip=False):
        ip = request.META.get('HTTP_CF_CONNECTING_IP') or request.META.get('HTTP_X_REAL_IP')
        if ip is None or only_remote_ip is True:
            ip = request.META.get('REMOTE_ADDR')

        if get_version is False:
            return ip
        else:
            version = 'ipv6' if len(ip) > 16 else 'ipv4'
            return [version, ip]
