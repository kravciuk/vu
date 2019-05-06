# -*- coding: utf-8 -*-
__author__ = 'Vadim Kravciuk, vadim@kravciuk.com'

from PIL import Image, ExifTags

from logging import getLogger
log = getLogger(__name__)


class VuImage:

    @staticmethod
    def normalize_orientation(source):
        try:
            im = Image.open(source)
            for orientation in ExifTags.TAGS.keys():
                if ExifTags.TAGS[orientation] == 'Orientation':
                    break
            exif = dict(im._getexif().items())

            rotation = True
            if exif[orientation] == 3:
                image = im.rotate(180, expand=True)
            elif exif[orientation] == 6:
                image = im.rotate(270, expand=True)
            elif exif[orientation] == 8:
                image = im.rotate(90, expand=True)
            else:
                rotation = False

            if rotation is True:
                image.save(source)
                image.close()

        except Exception as e:
            log.debug("Orientation fix failed: %s" % e, exc_info=True)

    @staticmethod
    def resize(source, maxsize=(1920, 1920), target=None):
        target = target or source
        im = Image.open(source)
        w, h = im.size
        if w > maxsize[0] or h > maxsize[1]:
            im.thumbnail(maxsize, Image.ANTIALIAS)
            im.save(target)
