from django import forms
from django.views.generic import TemplateView

from mycore.models import Room, Tenant, Journal


class TenantForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    date_of_birth = forms.DateField()
    phone = forms.CharField()
    notes = forms.CharField()

    def save_tenant(self):
        tenant = Tenant(first_name=self.data['first_name'], last_name=self.data['last_name'],
                        date_of_birth=self.data['date_of_birth'],
                        phone=self.data['phone'], notes=self.data['notes'])
        tenant.save()


class RoomForm(forms.Form):
    number_room = forms.NumberInput()
    max_tenants = forms.NumberInput()
    status_room = forms.CharField()

    def save_room(self):
        room = Room(number_room=int(self.data['number_room']), max_tenants=int(self.data['max_tenants']),
                    status=self.data['status_room'])
        room.save()


class JournalForm(forms.Form):
    number_room = forms.NumberInput()
    tenant_id = forms.NumberInput()
    tenants = forms.NumberInput()

    def save_journal(self):
        room = Room.objects.get(id=int(self.data['room_id']))
        tenant = Tenant.objects.get(id=int(self.data['tenant_id']))
        journal_object = Journal(room_id=room, tenant_id=tenant, tenants=int(self.data['tenants']))
        journal_object.save()

