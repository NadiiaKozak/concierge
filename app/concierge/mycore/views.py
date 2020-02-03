# Create your views here.
import time
from http import HTTPStatus

from django.core import serializers
from django.core.serializers import SerializerDoesNotExist
from django.http import HttpResponse
from django.views.generic import FormView, ListView, DetailView
from mycore.forms import RoomForm, TenantForm, JournalForm

from . import models


def health_check(request):
    return HttpResponse("OK")


def api_serializer(request, object_model, object_id):
    try:
        model_name = getattr(models, object_model.capitalize())
        model = [model_name.objects.get(id=object_id)]
        return HttpResponse(
            serializers.serialize('json', model)
        )
    except (AttributeError, SerializerDoesNotExist):
        return HttpResponse(status=HTTPStatus.NOTFOUND)


class TenantView(FormView):
    template_name = 'form_tenant.html'
    form_class = TenantForm
    success_url = '/alltenants/'

    def form_valid(self, form):
        form.save_tenant()
        return super().form_valid(form)


class TenantListView(ListView):
    model = models.Tenant
    data = models.Tenant.objects.all()
    template_name = 'alltenants.html'
    paginate_by = 100


class TenantDetailView(DetailView):
    model = models.Tenant
    template_name = 'tenant_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tenant'] = models.Tenant.objects.get(id=self.kwargs.get('pk'))
        return context


class RoomView(FormView):
    template_name = 'form_room.html'
    form_class = RoomForm
    success_url = '/allrooms/'

    def form_valid(self, form):
        form.save_room()
        return super().form_valid(form)


class RoomListView(ListView):
    model = models.Room
    data = models.Room.objects.all()
    template_name = 'allrooms.html'
    paginate_by = 100


class RoomDetailView(DetailView):
    model = models.Room
    template_name = 'room_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['room'] = models.Room.objects.get(id=self.kwargs.get('pk'))
        time.sleep(2)
        return context


class JournalView(FormView):
    template_name = 'form_journal.html'
    form_class = JournalForm
    success_url = '/alljournal/'

    def form_valid(self, form):
        form.save_journal()
        return super().form_valid(form)


class JournalListView(ListView):
    model = models.Journal
    data = models.Journal.objects.all()
    template_name = 'alljournal.html'
    paginate_by = 100


class JournalDetailView(DetailView):
    model = models.Journal
    template_name = 'journal_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['journal'] = models.Journal.objects.get(id=self.kwargs.get('pk'))
        return context
