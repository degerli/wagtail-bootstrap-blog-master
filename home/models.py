from __future__ import absolute_import, unicode_literals

from django.db import models

import wagtail
from wagtail.core.models import Page
from wagtail.images.blocks import ImageChooserBlock
from wagtail.images.edit_handlers import ImageChooserPanel

class HomePage(Page):
    pass