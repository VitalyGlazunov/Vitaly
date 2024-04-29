from django.http import HttpResponse
from django.urls import reverse
from .models import BugReport, FeatureRequest
from django.shortcuts import get_object_or_404
from django.views import View
from django.views.generic import ListView, DetailView


def index(request):
    bugs_page_url = reverse('quality_control:bug_list')
    features_page_url = reverse('quality_control:feature_list')
    html = f"<h1>Система контроля качества</h1><a href='{bugs_page_url}'>Список всех багов</a><br>" \
           f"<a href='{features_page_url}'>Запросы на улучшение</a>"
    return HttpResponse(html)


#-------------------------Function-Based Views-------------------------
def bug_list(request):
    bugs = BugReport.objects.all()
    bugs_html = '<h1>Cписок отчетов об ошибках</h1><ul>'
    for bug in bugs:
        bugs_html += f'<li><a href="{bug.id}/">{bug.title} ({bug.status})</a></li>'
    bugs_html += '</ul>'
    return HttpResponse(bugs_html)


def feature_list(request):
    features = FeatureRequest.objects.all()
    features_html = '<h1>Список запросов на улучшение</h1><ul>'
    for feature in features:
        features_html += f'<li><a href="{feature.id}/">{feature.title} ({feature.status})</a></li>'
    features_html += '</ul>'
    return HttpResponse(features_html)


def bug_detail(request, bug_id):
    bug = get_object_or_404(BugReport, id=bug_id)
    response_html = f'<h1>Детали бага {bug_id}</h1><p>Title: {bug.title}</p>' \
                    f'<p>Description: {bug.description}</p><p>Status: {bug.status}</p>' \
                    f'<p>Priority: {bug.priority}</p><p>Project: {bug.project}</p><p>Task: {bug.task}</p>'
    return HttpResponse(response_html)


def feature_detail(request, feature_id):
    feature = get_object_or_404(FeatureRequest, id=feature_id)
    response_html = f'<h1>Детали улучшения {feature_id}</h1><p>Title: {feature.title}</p>' \
                    f'<p>Description: {feature.description}</p><p>Status: {feature.status}</p>' \
                    f'<p>Priority: {feature.priority}</p><p>Project: {feature.project}</p><p>Task: {feature.task}</p>'
    return HttpResponse(response_html)


#-------------------------Class-Based Views-------------------------
class IndexView(View):
    def get(self, request, *args, **kwargs):
        bugs_page_url = reverse('quality_control:bug_list')
        features_page_url = reverse('quality_control:feature_list')
        html = f"<h1>Система контроля качества</h1><a href='{bugs_page_url}'>Список всех багов</a><br>" \
               f"<a href='{features_page_url}'>Запросы на улучшение</a>"
        return HttpResponse(html)


class BugReportListView(ListView):
    model = BugReport

    def get(self, request, *args, **kwargs):
        bugs = self.get_queryset()
        bugs_html = '<h1>Cписок отчетов об ошибках</h1><ul>'
        for bug in bugs:
            bugs_html += f'<li><a href="{bug.id}/">{bug.title} ({bug.status})</a></li>'
        bugs_html += '</ul>'
        return HttpResponse(bugs_html)


class FeatureRequestListView(ListView):
    model = FeatureRequest

    def get(self, request, *args, **kwargs):
        features = self.get_queryset()
        features_html = '<h1>Список запросов на улучшение</h1><ul>'
        for feature in features:
            features_html += f'<li><a href="{feature.id}/">{feature.title} ({feature.status})</a></li>'
        features_html += '</ul>'
        return HttpResponse(features_html)


class BugReportDetailView(DetailView):
    model = BugReport
    pk_url_kwarg = 'bug_id'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        bug = self.object
        response_html = f'<h1>Детали бага {bug.id}</h1><p>Title: {bug.title}</p>' \
                        f'<p>Description: {bug.description}</p><p>Status: {bug.status}</p>' \
                        f'<p>Priority: {bug.priority}</p><p>Project: {bug.project}</p><p>Task: {bug.task}</p>'
        return HttpResponse(response_html)


class FeatureRequestDetailView(DetailView):
    model = FeatureRequest
    pk_url_kwarg = 'feature_id'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        feature = self.object
        response_html = f'<h1>Детали улучшения {feature.id}</h1><p>Title: {feature.title}</p>' \
                        f'<p>Description: {feature.description}</p><p>Status: {feature.status}</p>' \
                        f'<p>Priority: {feature.priority}</p><p>Project: {feature.project}</p>' \
                        f'<p>Task: {feature.task}</p>'
        return HttpResponse(response_html)
