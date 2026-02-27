from django.contrib import admin
from .models import *

# Register your models here.
class tblcontactAdmin(admin.ModelAdmin):
    list_display=("name","email","mobile","message")
admin.site.register(tblcontact,tblcontactAdmin)


class tblgalleryAdmin(admin.ModelAdmin):
    list_display=("title","picture")
admin.site.register(tblgallery,tblgalleryAdmin)


class tblregisterAdmin(admin.ModelAdmin):
    list_display=("name","email","mobile","password","picture","batch","address","regdate")
admin.site.register(tblregister,tblregisterAdmin)


class batchAdmin(admin.ModelAdmin):
    list_display=("id","batchname")
admin.site.register(batch,batchAdmin)


class categoryAdmin(admin.ModelAdmin):
    list_display=("id","title","picture","batch_name")
admin.site.register(category,categoryAdmin)


class softwarekitAdmin(admin.ModelAdmin):
    list_display=("id","title","software_info","thumbnail","download_link","posted_date")
admin.site.register(softwarekit,softwarekitAdmin)

class mylectureAdmin(admin.ModelAdmin):
    list_display=("id","title","video_info","vlink","batch","category","posted_date")
admin.site.register(mylecture,mylectureAdmin)


class notesAdmin(admin.ModelAdmin):
    list_display=("id","title","notes_info","batch","notesfile","posted_date")
admin.site.register(notes,notesAdmin)

class mytaskAdmin(admin.ModelAdmin):
    list_display=("id","title","task_info","batch","taskfile","posted_date")
admin.site.register(mytask,mytaskAdmin)


class submittedtaskAdmin(admin.ModelAdmin):
    list_display=("id","userid","tid","upload_task","marks","title")
admin.site.register(submittedtask,submittedtaskAdmin)