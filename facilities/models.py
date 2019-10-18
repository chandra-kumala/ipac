from django.db import models

from modelcluster.fields import ParentalKey

from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel, MultiFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.search import index

from ipac.models import Seo

class Facilities(Page, Seo):
    parent_page_types = ['home.HomePage']
    subpage_types = ['facilities.FacilitiesPage']
    intro = RichTextField(blank=True)

    def get_context(self, request):
        # Update context to include only published posts, ordered by reverse-chron
        context = super().get_context(request)
        facilities = self.get_children().live().order_by('-first_published_at')
        context['facilities'] = facilities
        return context

    content_panels = Page.content_panels + [
        FieldPanel('intro', classname="full")
    ]

    promote_panels = Page.promote_panels + [
        MultiFieldPanel(Seo.panels, heading="Extra Seo Settings ..."),
    ]


class FacilitiesPage(Page, Seo):
    parent_page_types = ['facilities.Facilities']
    intro = models.CharField(max_length=250)
    body = RichTextField(blank=True)

    def main_image(self):
        gallery_item = self.gallery_images.first()
        if gallery_item:
            return gallery_item.image
        else:
            return None

    search_fields = Page.search_fields + [
        index.SearchField('intro'),
        index.SearchField('body'),
    ]

    content_panels = Page.content_panels + [
        FieldPanel('intro'),
        FieldPanel('body', classname="full"),
        InlinePanel('gallery_images', label="Gallery images"),
    ]

    promote_panels = Page.promote_panels + [
        MultiFieldPanel(Seo.panels, heading="Extra Seo Settings ..."),
    ]

class FacilitiesPageGalleryImage(Orderable):
    page = ParentalKey(FacilitiesPage, on_delete=models.CASCADE, related_name='gallery_images')
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
    )
    caption = models.CharField(blank=True, max_length=250)

    panels = [
        ImageChooserPanel('image'),
        FieldPanel('caption'),
    ]