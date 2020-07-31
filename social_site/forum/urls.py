from django.urls import path
from . import views

urlpatterns = [
    path("new-section/", views.CreateSection.as_view(), name="create_section"),
    path("section/<int:pk>/", views.sectionView, name="section_view"),
    path("section/<int:pk>/create-topic/", views.createTopic, name="create_topic"),
    path("topic/<int:pk>/", views.viewTopic, name="view_topic"),
    path("topic/<int:pk>/answer/", views.addAnswer, name="answer_topic"),
    # path(
    #     "topic/<int:id>/delete-post/<int:pk>/",
    #     views.DeletePost.as_view(),
    #     name="delete_post",
    # ),
]

