from django.contrib import admin
from Admin.models import Notice

admin.site.site_header='Admin'
admin.site.index_title='Master Admin Panel'

class NoticeAdmin(admin.ModelAdmin):
    list_display=['id','Subject','Description','Date_Posted','Date_Updated']
    search_fields=['name','title']
admin.site.register(Notice,NoticeAdmin)