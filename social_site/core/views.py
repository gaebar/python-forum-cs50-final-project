from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic.list import ListView
from forum.models import Topic, Post, Section

# Create your views here.


class HomeView(ListView):
    queryset = Section.objects.all()
    template_name = "core/homepage.html"
    context_object_name = "sections_list"


class UserList(LoginRequiredMixin, ListView):
    model = User
    template_name = "core/users.html"


def userProfileView(request, username):
    user = get_object_or_404(User, username=username)
    user_topics = Topic.objects.filter(topic_author=user).order_by("-pk")
    context = {"user": user, "user_topics": user_topics}
    return render(request, "core/user_profile.html", context)
