from django.urls import path
from .views import AjaxHandlerView, contact

urlpatterns = [
    path('', AjaxHandlerView.as_view()),
    path('contacts/', contact, name='contact'),
]