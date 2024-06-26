
from django.urls import path
from basic_app import views

app_name='basic_app'

urlpatterns = [
    path('',views.SchoolListView.as_view(),name='list'),
    # path('list/',views.SchoolListView.as_view(),name='list'),
    path('list/<slug:id>/',views.SchoolDetailView.as_view(),name='details'),
    path('create/',views.SchoolCreateView.as_view(),name='create'),
    path('update/<slug:id>/',views.SchoolUpdateView.as_view(),name='update'),
    path('delete/<slug:id>/',views.SchoolDeleteView.as_view(),name='delete'),

]
