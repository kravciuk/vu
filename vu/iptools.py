# -*- coding: utf-8 -*-
__author__ = 'Vadim Kravciuk, vadim@kravciuk.com'

import ipaddress
from django.contrib.gis.geoip2 import GeoIP2

from logging import getLogger
log = getLogger(__name__)


class GeoIP:
    ip_headers = ['REMOTE_ADDR', 'HTTP_X_FORWARDED_FOR', 'HTTP_X_REAL_IP', 'HTTP_CF_CONNECTING_IP']

    def __init__(self, request):
        self.request = request
        self.gi = GeoIP2()
        self.ip = GeoIP.get_client_ip(request)

    @property
    def country(self):
        return self.get_country(self.ip)

    def get_country(self, ip):
        try:
            return self.gi.country(ip)
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

    @property
    def ip_info(self):
        local_subnets = ['10.0.0.0/8', '172.16.0.0/12', '192.168.0.0/16']
        x = []
        for header in self.ip_headers:
            if ip := self.request.META.get(header):
                for ip in ip.split(','):
                    if ip not in x:
                        is_local = False
                        for local_ip in local_subnets:
                            if ipaddress.ip_address(ip.strip()) in ipaddress.ip_network(local_ip):
                                is_local = True
                                break
                        if is_local is False:
                            x.append({
                                'ip': ip,
                                'geo': self.get_country(ip),
                            })
        if len(x)==0:
            x.append({
                'ip': GeoIP.get_client_ip(self.request),
                'geo': {
                    'country_code': 'n/a',
                    'country_name': 'local network',
                }

            })
        return x