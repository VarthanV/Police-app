from django.urls import path
from .import views
urlpatterns =[
    path('',views.HomePageView.as_view(),name="home"),
    path('add/',views.AddPoliceView.as_view(),name ='add'),
    path('view/',views.PoliceView.as_view(),name="view"),
    path("delete/<str:pk>/",views.PoliceDeleteView.as_view(),name='delete')
]