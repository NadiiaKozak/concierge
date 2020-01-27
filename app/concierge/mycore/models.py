from django.core.exceptions import ValidationError
from django.db import models

# Create your models here.
from django.db.models import ForeignKey, DO_NOTHING, Model, CharField, IntegerField, DateTimeField, SET_NULL


class Tenant(models.Model):
    """
    Room's owner/tenant
    """
    first_name = models.CharField(
        'First name',
        max_length=250,
    )
    last_name = models.CharField(
        'Last name',
        max_length=250,
    )
    date_of_birth = models.DateField(
        blank=True,
        null=True,
        db_index=True,
    )
    phone = models.CharField(
        'Phone num',
        max_length=20,
        blank=True,
        null=True,
    )
    photo = models.ImageField(
        'Photo',
        upload_to='tenant',
        help_text='Photo of the tenant',
        null=True,
        blank=True
    )
    notes = models.TextField(
        blank=True,
        null=True,
    )

    @property
    def fullname(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return self.fullname

    class Meta:
        ordering = ['first_name', 'last_name']
        indexes = [
            models.Index(fields=['first_name', 'last_name']),
        ]


class Room(models.Model):
    number_room = IntegerField('Number room', blank=True, null=True)
    max_tenants = IntegerField('Max tenants')
    status = CharField('Status', max_length=10, default='free')
    tenant = ForeignKey(Tenant, on_delete=SET_NULL, null=True, blank=True)

    def __str__(self):
        return f'Room {self.number_room} have max_tenant {self.max_tenant} and status {self.status}'


class Journal(Model):
    room_id = ForeignKey(Room, on_delete=DO_NOTHING, null=True, blank=True)
    tenant_id = ForeignKey(Tenant, on_delete=DO_NOTHING, null=True, blank=True)
    key_out = DateTimeField('Key out', null=True, blank=True,)
    key_in = DateTimeField('Key in', null=True, blank=True,)
    tenants = IntegerField('Tenants', null=True, blank=True, default=0)

    def __str__(self):
        return f'Journal {self.room_id}, {self.tenant_id}, {self.tenants}, {self.key_in}, {self.key_out}'

    def save(self, *args, **kwargs):
        room = self.room_id
        if self.key_out:
            return ValidationError(f'the room  {self.room_id} is occupied')
        elif self.tenants > room.max_tenants:
            return ValidationError(f'not enough beds in the room  {self.room_id}')
        super().save(*args, **kwargs)
