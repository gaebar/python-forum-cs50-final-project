from django.contrib import admin
from .models import Topic, Post, Section

# Register your models here.


class TopicModelAdmin(admin.ModelAdmin):
    model = Topic
    list_display = ["title", "topic_section", "topic_author"]
    search_fields = ["title", "topic_author"]
    list_filter = ["topic_section", "creation_date"]


class PostModelAdmin(admin.ModelAdmin):
    model = Post
    list_display = ["post_author", "topic"]
    search_fields = ["content"]
    list_filter = ["creation_date", "post_author"]


class SectionModelAdmin(admin.ModelAdmin):
    model = Section
    list_display = ["section_name", "description"]


admin.site.register(Topic, TopicModelAdmin)
admin.site.register(Post, PostModelAdmin)
admin.site.register(Section, SectionModelAdmin)
