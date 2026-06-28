from django.contrib import admin
from .models import Reporter, Categories, Articles, Image, Video, Tag, Comments

# Register your models here.

admin.site.register(Reporter)
admin.site.register(Categories)
admin.site.register(Articles)
admin.site.register(Image)
admin.site.register(Video)
admin.site.register(Tag)
admin.site.register(Comments)