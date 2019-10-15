from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel
from wagtail.search import index

from ipac.models import Seo


class Classes(Page, Seo):
    parent_page_types = ['home.HomePage']
    subpage_types = ['classes.ClassesPage']
    intro = RichTextField(blank=True)

    def get_context(self, request):
        # Update context to include only published posts, ordered by reverse-chron
        context = super().get_context(request)
        classes = self.get_children().live().order_by('-first_published_at')
        context['classes'] = classes
        return context

    content_panels = Page.content_panels + [
        FieldPanel('intro', classname="full")
    ]
    
    promote_panels = Page.promote_panels + [
        MultiFieldPanel(Seo.panels, heading="Extra Seo Settings ..."),
    ]



class ClassesPage(Page, Seo):
    parent_page_types = ['classes.Classes']
    intro = models.CharField(max_length=250)
    body = RichTextField(blank=True)

    search_fields = Page.search_fields + [
        index.SearchField('intro'),
        index.SearchField('body'),
    ]

    content_panels = Page.content_panels + [
        FieldPanel('intro'),
        FieldPanel('body', classname="full"),
    ]

    promote_panels = Page.promote_panels + [
        MultiFieldPanel(Seo.panels, heading="Extra Seo Settings ..."),
    ]
