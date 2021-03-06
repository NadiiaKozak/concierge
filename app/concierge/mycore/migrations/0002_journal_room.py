# Generated by Django 3.0.1 on 2020-01-17 15:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mycore', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_room', models.IntegerField(blank=True, null=True, verbose_name='Number room')),
                ('max_tenants', models.IntegerField(verbose_name='Max tenants')),
                ('status', models.CharField(default='free', max_length=10, verbose_name='Status')),
                ('tenant', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='mycore.Tenant')),
            ],
        ),
        migrations.CreateModel(
            name='Journal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key_out', models.DateTimeField(blank=True, null=True, verbose_name='Key out')),
                ('key_in', models.DateTimeField(blank=True, null=True, verbose_name='Key in')),
                ('tenants', models.IntegerField(blank=True, default=0, null=True, verbose_name='Tenants')),
                ('room_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='mycore.Room')),
                ('tenant_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='mycore.Tenant')),
            ],
        ),
    ]
