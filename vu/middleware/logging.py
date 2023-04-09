# -*- coding: utf-8 -*-
__author__ = 'Vadim Kravciuk, vadim@kravciuk.com'

import logging


class IpLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        logger = logging.getLogger('django.request')
        logger.info('Request finished', extra={'ip': request.META.get('REMOTE_ADDR')})

        return response