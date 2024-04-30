from django.urls import path
from quality_control import views

app_name = 'quality_control'

urlpatterns = [

    #path('', views.index, name='index'),
    #path('bugs/', views.bug_list, name='bug_list'),
    #path('features/', views.feature_list, name='feature_list'),
    #path('bugs/<int:bug_id>/', views.bug_detail, name='bug_detail'),
    #path('features/<int:feature_id>/', views.feature_detail, name='feature_detail'),
    #path('add_bug_report/', views.add_bug_report, name='add_bug_report'),
    #path('add_feature_request/', views.add_feature_request, name='add_feature_request'),
    #path('bugs/<int:bug_id>/update/', views.bug_report_update, name='bug_report_update'),
    #path('features/<int:feature_id>/update/', views.feature_request_update, name='feature_request_update'),
    #path('bugs/<int:bug_id>/delete/', views.bug_report_delete, name='bug_report_delete'),
    #path('features/<int:feature_id>/delete/', views.feature_request_delete, name='feature_request_delete'),

    path('', views.IndexView.as_view(), name='index'),
    path('bugs/', views.BugReportListView.as_view(), name='bug_list'),
    path('features/', views.FeatureRequestListView.as_view(), name='feature_list'),
    path('bugs/<int:bug_id>/', views.BugReportDetailView.as_view(), name='bug_detail'),
    path('features/<int:feature_id>/', views.FeatureRequestDetailView.as_view(), name='feature_detail'),
    path('add_bug_report/', views.BugReportCreateView.as_view(), name='add_bug_report'),
    path('add_feature_request/', views.FeatureRequestCreateView.as_view(), name='add_feature_request'),
    path('bugs/<int:bug_id>/update/', views.BugReportUpdateView.as_view(), name='bug_report_update'),
    path('features/<int:feature_id>/update/', views.FeatureRequestUpdateView.as_view(), name='feature_request_update'),
    path('bugs/<int:bug_id>/delete/', views.BugReportDeleteView.as_view(), name='bug_report_delete'),
    path('features/<int:feature_id>/delete/', views.FeatureRequestDeleteView.as_view(), name='feature_request_delete'),
]
