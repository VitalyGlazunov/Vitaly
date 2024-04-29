from django.urls import path
from quality_control import views

app_name = 'quality_control'

urlpatterns = [

    #path('', views.index, name='main_page'),
    #path('bugs/', views.bug_list, name='bug_list'),
    #path('features/', views.feature_list, name='feature_list'),
    #path('bugs/<int:bug_id>/', views.bug_detail, name='bug_detail'),
    #path('features/<int:feature_id>/', views.feature_detail, name='feature_detail'),

    path('', views.IndexView.as_view(), name='main_page'),
    path('bugs/', views.BugReportListView.as_view(), name='bug_list'),
    path('features/', views.FeatureRequestListView.as_view(), name='feature_list'),
    path('bugs/<int:bug_id>/', views.BugReportDetailView.as_view(), name='bug_detail'),
    path('features/<int:feature_id>/', views.FeatureRequestDetailView.as_view(), name='feature_detail'),

]
