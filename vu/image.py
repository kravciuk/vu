# -*- coding: utf-8 -*-
__author__ = 'Vadim Kravciuk, vadim@kravciuk.com'

from PIL import Image, ExifTags, ImageOps

from logging import getLogger
log = getLogger(__name__)


class VuImage:

    @staticmethod
    def get_exif(image):
        result = {}
        if isinstance(image, str):
            image = Image.open(image)

        for k,v in image.getexif().items():
            if k in ExifTags.TAGS:
                k = ExifTags.TAGS[k]
            result[k] = v
        return result


    @staticmethod
    def normalize_orientation(source, quality='web_high'):

        image = Image.open(source)
        exif = VuImage.get_exif(image)
        if 'Orientation' in exif:
            image = ImageOps.exif_transpose(image)
            image.save(source, exif=image.getexif(), quality=quality)
        image.close()


    @staticmethod
    def resize(source, maxsize=(1920, 1920), target=None, quality='web_high'):
        target = target or source
        im = Image.open(source)
        w, h = im.size
        if w > maxsize[0] or h > maxsize[1]:
            im.thumbnail(maxsize, Image.ANTIALIAS)
            im.save(target, quality=quality)
