from django.db import models

from modelcluster.fields import ParentalKey

from wagtail.core.models import Page, Orderable
from wagtail.core.fields import StreamField
from wagtail.embeds.blocks import EmbedBlock
from wagtail.core import blocks
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel, InlinePanel, MultiFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.images.blocks import ImageChooserBlock

from tools.models import Streamer, Seo


class HomePage(Page, Streamer, Seo):
    parent_page_types = ['wagtailcore.page', 'home.HomePage']
    subpage_types = ['tools.Index', 'home.HomePage']


    content_panels = Page.content_panels + Streamer.panels + [
        InlinePanel('carousel_items', label="Carousel images"),
    ]
     
    promote_panels = Page.promote_panels + Seo.panels


    class Meta:
        verbose_name = "Home Page"
        verbose_name_plural = "Home Pages"


class Carousel(Orderable):
    page = ParentalKey(HomePage, on_delete=models.CASCADE, related_name='carousel_items')
    title = models.CharField(blank=True, max_length=250)
    caption = models.CharField(blank=True, max_length=250)
    image = models.ForeignKey('wagtailimages.Image',  null=True, blank=True, on_delete=models.CASCADE, related_name='+')

    panels = [
        FieldPanel('title'),
        FieldPanel('caption'),
        ImageChooserPanel('image'),
    ]