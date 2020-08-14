from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator  # , EmptyPage, PageNotAnInteger
from django.http import HttpResponseRedirect, HttpResponseBadRequest
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic.edit import CreateView, DeleteView
from .forms import TopicModelForm, PostModelForm
from .mixins import StaffMixing
from .models import Topic, Post, Section


class CreateSection(StaffMixing, CreateView):
    model = Section
    fields = "__all__"
    template_name = "forum/create_section.html"
    success_url = "/"


def sectionView(request, pk):
    section = get_object_or_404(Section, pk=pk)
    section_topics = Topic.objects.filter(topic_section=section).order_by(
        "-creation_date"
    )
    context = {"section": section, "topics": section_topics}
    return render(request, "forum/individual_section.html", context)


@login_required
def createTopic(request, pk):
    section = get_object_or_404(Section, pk=pk)
    if request.method == "POST":
        form = TopicModelForm(request.POST)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.topic_section = section
            topic.topic_author = request.user
            topic.save()
            first_post = Post.objects.create(
                topic=topic,
                post_author=request.user,
                content=form.cleaned_data["content"],
            )
            return HttpResponseRedirect(topic.get_absolute_url())
    else:
        form = TopicModelForm()
    context = {"form": form, "section": section}
    return render(request, "forum/create_topic.html", context)


# def viewTopic(request, pk):
#     """
#     link: https://docs.djangoproject.com/en/2.0/topics/pagination/
#     """
#     topic = get_object_or_404(Topic, pk=pk)
#     posts_topic = Post.objects.filter(topic=topic)

#     paginator = Paginator(posts_topic, 5)
#     page = request.GET.get("page")
#     posts = paginator.get_page(page)

#     answer_form = PostModelForm()
#     context = {
#         "topic": topic,
#         "posts_topic": posts,
#         "answer_form": answer_form,
#     }
#     return render(request, "forum/individual_topic.html", context)


def viewTopic(request, pk):
    """
    link: https://docs.djangoproject.com/en/2.0/topics/pagination/
    """
    topic = get_object_or_404(Topic, pk=pk)
    posts_topic = Post.objects.filter(topic=topic)

    paginator = Paginator(posts_topic, 5)
    page = request.GET.get("page")
    posts = paginator.get_page(page)

    answer_form = PostModelForm()
    context = {"topic": topic, "posts_topic": posts, "answer_form": answer_form}
    return render(request, "forum/individual_topic.html", context)


@login_required
def addAnswer(request, pk):
    topic = get_object_or_404(Topic, pk=pk)
    if request.method == "POST":
        form = PostModelForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            form.instance.topic = topic
            form.instance.post_author = request.user
            form.save()

            url_topic = reverse("view_topic", kwargs={"pk": pk})
            page_in_topic = topic.get_n_pages()
            if page_in_topic > 1:
                success_url = url_topic + "?page=" + str(page_in_topic)
                return HttpResponseRedirect(success_url)
            else:
                return HttpResponseRedirect(url_topic)
    else:
        return HttpResponseBadRequest()


class DeletePost(DeleteView):
    model = Post
    success_url = "/"

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(post_author_id=self.request.user.id)
