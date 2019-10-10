from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.embeds.blocks import EmbedBlock
from wagtail.core import blocks
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.images.blocks import ImageChooserBlock

class GenericPage(Page):
    template = "home/generic_page.html"
    body = StreamField([
        ('heading', blocks.CharBlock(classname="full title")),
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
        ('embed', EmbedBlock()),
    ])
    
    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
    ]
    class Meta:
        verbose_name = "Generic Page"
        verbose_name_plural = "Generic Pages"


class HomePage(Page):
    parent_page_types = ['wagtailcore.page']
    subpage_types = ['classes.Classes', 'jobs.Jobs', 'facilities.Facilities', 'home.GenericPage']

    body = StreamField([
        ('heading', blocks.CharBlock(classname="full title")),
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
        ('embed', EmbedBlock()),
    ])

    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
    ]    class Meta:
        verbose_name = "Home Page"
        verbose_name_plural = "Home Pages"