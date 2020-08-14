from django import forms

from .models import Topic, Post


class TopicModelForm(forms.ModelForm):
    content = forms.CharField(
        widget=forms.Textarea(attrs={"placeholder": "What do you want to talk about?"}),
        max_length=4000,
        label="First Message",
    )

    class Meta:
        model = Topic
        fields = ["title", "content"]
        widgets = {"title": forms.TextInput(attrs={"placeholder": "Topic Title"})}


class PostModelForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["content"]
        widgets = {"content": forms.Textarea(attrs={"rows": "5"})}
        labels = {"content": "Text"}
