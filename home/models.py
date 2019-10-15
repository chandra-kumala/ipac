from django.db import models

from modelcluster.fields import ParentalKey

from wagtail.core.models import Page, Orderable
from wagtail.core.fields import StreamField
from wagtail.embeds.blocks import EmbedBlock
from wagtail.core import blocks
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel, InlinePanel, MultiFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.images.blocks import ImageChooserBlock

from ipac.models import Seo


class GenericPage(Page, Seo):
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
    
    promote_panels = Page.promote_panels + [
        MultiFieldPanel(Seo.panels, heading="Extra Seo Settings ..."),
    ]

    class Meta:
        verbose_name = "Generic Page"
        verbose_name_plural = "Generic Pages"


class HomePage(Page, Seo):
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
    ]
     
    promote_panels = Page.promote_panels + [
        MultiFieldPanel(Seo.panels, heading="Extra Seo Settings ..."),
    ]


    class Meta:
        verbose_name = "Home Page"
        verbose_name_plural = "Home Pages"
