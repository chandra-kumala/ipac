from django.db import models

from modelcluster.fields import ParentalKey

from wagtail.core.models import Page, Orderable
from wagtail.core.fields import StreamField
from wagtail.embeds.blocks import EmbedBlock
from wagtail.core import blocks
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel, InlinePanel, MultiFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.images.blocks import ImageChooserBlock

from ipac.models import Streamer, Seo


class HomePage(Page, Streamer, Seo):
    parent_page_types = ['wagtailcore.page', 'home.HomePage']
    subpage_types = ['section.Index', 'jobs.Jobs', 'home.HomePage']


    content_panels = Page.content_panels + Streamer.panels
     
    promote_panels = Page.promote_panels + Seo.panels


    class Meta:
        verbose_name = "Home Page"
        verbose_name_plural = "Home Pages"
