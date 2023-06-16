from django.urls import path, include
from .views import chat_view
#from . import views

urlpatterns = [
    path('', chat_view, name='chat'),
    path("register/", views.register, name="register"),
    path('chat/', include('chatgpt_app.urls')), # include URLs of chatgpt_app
]

