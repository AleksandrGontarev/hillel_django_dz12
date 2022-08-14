from reminder import views

from django.urls import path

app_name = 'reminder'

urlpatterns = [
    path('reminder/', views.reminder, name='reminder'),
]
