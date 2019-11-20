from django.contrib import admin

from .models import Site, Page, Section, Image

admin.site.register(Site)
admin.site.register(Page)
admin.site.register(Section)
admin.site.register(Image)
