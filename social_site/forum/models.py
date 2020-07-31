from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
import math

# Create your models here.


class Section(models.Model):
    """
     Generic model of a section of the Forum.
     The sections split the site into topic categories.
     Each section contains several topics.
     Sections are created by site administrators.
    """

    section_name = models.CharField(max_length=80)
    description = models.CharField(max_length=150, blank=True, null=True)
    logo_section = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.section_name

    def get_absolute_url(self):
        return reverse("section_view", kwargs={"pk": self.pk})

    def get_last_discussions(self):
        """ Returns the last two discussions in the section, sorted by date """
        return Topic.objects.filter(topic_section=self).order_by("-creation_date")[:2]

    def get_number_of_posts_in_section(self):
        """ Returns the number of total posts in a section instance """
        return Post.objects.filter(topic__topic_section=self).count()

    class Meta:
        verbose_name = "Section"
        verbose_name_plural = "Sections"


class Topic(models.Model):
    """
    Model of a single forum thread.
    Each topic is part of a specific section.
    Topics can be created by all users.
    """

    title = models.CharField(max_length=120)
    creation_date = models.DateTimeField(auto_now_add=True)
    topic_author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="topics"
    )
    topic_section = models.ForeignKey(Section, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("view_topic", kwargs={"pk": self.pk})

    def get_n_pages(self):
        """
        Returns the page number present in a Discussion instance.
        math.ceil https://docs.python.org/3.6/library/math.html#math.ceil
        returns the integer following the float passed as a parameter (e.g. 3.1 ==> 4)
        or returns the same number if integer
        """
        posts_topic = self.post_set.count()
        n_page = math.ceil(posts_topic / 5)
        return n_page

    class Meta:
        verbose_name = "Topic"
        verbose_name_plural = "Topics"


class Post(models.Model):
    """
     Single post model.
     Posts represent the individual messages of the topics, and for this reason
     each post is part of a specific topic.
     Any user of the site can participate in topics by adding new posts.
     """

    post_author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="posts"
    )
    content = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)

    def __str__(self):
        """ make reading easy from the admin section """
        return self.post_author.username

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"
