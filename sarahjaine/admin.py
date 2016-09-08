from django.contrib import admin
from .models import Project, Tag


class ProjectAdmin(admin.ModelAdmin):
	model = Project
	list_display = ('name', 'order', 'featured')
	prepopulated_fields = {'slug': ('name',)}
	filter_horizontal = ('tags',)


class TagAdmin(admin.ModelAdmin):
    model = Tag
    list_display = ('name',)
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Project, ProjectAdmin)
admin.site.register(Tag, TagAdmin)
