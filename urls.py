from django.urls import path
from . import views
from django.urls import path, include


urlpatterns = [
    path('', views.upload_pdf, name='quiz_home'),  # Home Page with Upload Form
    path('result/', views.quiz_result, name='quiz_result'),  # Result Page
    path('submit/', views.submit_quiz, name='submit_quiz'),
    path('upload/', include('quiz_app.urls')),# Quiz Submission
    path('', views.upload_pdf, name='quiz_home'),  # Home page with upload form
    path('result/', views.quiz_result, name='quiz_result'),
]


urlpatterns = [
    path('upload/', views.upload_pdf, name='upload_pdf'),  # Make sure this URL is correct
]





