from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.search import index

import datetime

class JobsIndexPage(Page):
    intro = RichTextField(blank=True)

    def get_context(self, request):
        # Update context to include only published posts, ordered by reverse-chron
        context = super().get_context(request)
        jobspages = self.get_children().live().order_by('-first_published_at')
        context['jobspages'] = jobspages
        return context

    content_panels = Page.content_panels + [
        FieldPanel('intro', classname="full")
    ]

class JobsPage(Page):
    date = models.DateField(("Post date"), default=datetime.date.today)

    intro = models.CharField(max_length=250)
    start_date = models.CharField(max_length=150)
    body = RichTextField(blank=True)

    search_fields = Page.search_fields + [
        index.SearchField('intro'),
        index.SearchField('body'),
    ]

    content_panels = Page.content_panels + [
        FieldPanel('date'),
        FieldPanel('intro'),
        FieldPanel('start_date'),
        FieldPanel('body', classname="full"),
    ]