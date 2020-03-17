# -*- coding: utf-8 -*-
__author__ = 'Vadim Kravciuk, vadim@kravciuk.com'

try:
    import pygeoip2 as pygeoip
    pygeoip_verision = 2
except:
    import pygeoip as pygeoip
    pygeoip_verision = 1

from logging import getLogger
log = getLogger(__name__)


class GeoIP:
    def __init__(self, datafile):
        if pygeoip_verision == 1:
            self.gi = pygeoip.GeoIP(datafile)

    def country_code(self, default=None, ip=None):
        if pygeoip_verision == 1:
            try:
                code = self.gi.country_code_by_addr(ip or self.ip)
            except:
                return default

        return code or default

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
