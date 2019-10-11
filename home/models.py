from django.db import models

from modelcluster.fields import ParentalKey

from wagtail.core.models import Page, Orderable
from wagtail.core.fields import StreamField
from wagtail.embeds.blocks import EmbedBlock
from wagtail.core import blocks
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel, InlinePanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.images.blocks import ImageChooserBlock

class GenericPage(Page):
    template = "home/generic_page.html"
    
    desc = models.CharField("Description shown on Social Media", max_length=255, null=True, blank=True)
    body = StreamField([
        ('heading', blocks.CharBlock(classname="full title")),
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
        ('embed', EmbedBlock()),
    ])
    
    content_panels = Page.content_panels + [
        FieldPanel('desc'),
        InlinePanel('desc_images', label="Social Image"),
        StreamFieldPanel('body'),
    ]
    class Meta:
        verbose_name = "Generic Page"
        verbose_name_plural = "Generic Pages"


class HomePage(Page):
    parent_page_types = ['wagtailcore.page']
    subpage_types = ['classes.Classes', 'jobs.Jobs', 'facilities.Facilities', 'home.GenericPage']

    desc = models.CharField("Description shown on Social Media", max_length=255, null=True, blank=True)
    body = StreamField([
        ('heading', blocks.CharBlock(classname="full title")),
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
        ('embed', EmbedBlock()),
    ])

    content_panels = Page.content_panels + [
        FieldPanel('desc'),
        InlinePanel('desc_images', label="Social Image"),
        StreamFieldPanel('body'),
    ]

    class Meta:
        verbose_name = "Home Page"
        verbose_name_plural = "Home Pages"

class DescImage(Orderable):
    page = ParentalKey(Page, on_delete=models.CASCADE, related_name='desc_images')
    image = models.ForeignKey(
        'wagtailimages.Image', null=True, blank=True, on_delete=models.CASCADE, related_name='+'
    )

    panels = [
        ImageChooserPanel('image'),
    ]