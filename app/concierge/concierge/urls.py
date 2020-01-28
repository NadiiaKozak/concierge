"""concierge URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.decorators import permission_required
from django.urls import path, include
from django.views.decorators.cache import cache_page
from django.views.generic import TemplateView
from mycore.views import api_serializer, RoomView, TenantView, JournalView, RoomListView, RoomDetailView, \
    TenantListView, TenantDetailView, JournalListView, JournalDetailView

from .views import health_check

static_patterns = static(settings.MEDIA_URL,
                         document_root=settings.MEDIA_ROOT) + \
                  static(settings.STATIC_URL,
                         document_root=settings.STATIC_ROOT)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('healthcheck/', health_check, name='health_check'),
    path('index/', TemplateView.as_view(template_name='index.html')),
    path('api/<str:object_model>/<int:object_id>', api_serializer, name='api_serializer'),
    path('form-room/', RoomView.as_view(), name='form_room'),
    path('allrooms/', cache_page(300)(RoomListView.as_view()), name='all_room'),
    path('allrooms/<slug:pk>/', RoomDetailView.as_view(), name='room'),
    path('form-tenant/', TenantView.as_view(), name='form_tenant'),
    path('alltenants/', permission_required('mycore.view_tenant')(TenantListView.as_view()), name='all_tenants'),
    path('alltenants/<slug:pk>/', TenantDetailView.as_view(), name='tenant'),
    path('form-journal/', JournalView.as_view(), name='form_journal'),
    path('alljournal/', JournalListView.as_view(), name='all_journal'),
    path('alljournal/<slug:pk>/', JournalDetailView.as_view(), name='journal_entry'),
] + static_patterns
