# Generated by Django 3.0.2 on 2020-01-30 19:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('building', '0003_auto_20200130_1741'),
    ]

    operations = [
        migrations.CreateModel(
            name='UnitUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='object creation time', verbose_name='created')),
                ('modified', models.DateTimeField(auto_now=True, help_text='object modification time', verbose_name='modified')),
                ('type', models.CharField(choices=[('RESIDENT', 'Resident'), ('BOTH', 'Both'), ('OWNER', 'Owner')], default='RESIDENT', help_text='type of user', max_length=32, verbose_name='type')),
                ('confirmed', models.BooleanField(default=True, help_text='confirmation for user', verbose_name='confirmed')),
                ('unit', models.ForeignKey(help_text='unit for this user unit', on_delete=django.db.models.deletion.CASCADE, to='building.Unit', verbose_name='unit')),
                ('user', models.ForeignKey(help_text='user for this user unit', on_delete=django.db.models.deletion.CASCADE, related_name='Units', to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Block',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='object creation time', verbose_name='created')),
                ('modified', models.DateTimeField(auto_now=True, help_text='object modification time', verbose_name='modified')),
                ('name', models.CharField(help_text='name of block', max_length=255, verbose_name='name')),
                ('number_of_floors', models.PositiveIntegerField(help_text='number of block floors', verbose_name='number of floors')),
                ('number_of_units', models.PositiveIntegerField(help_text='number of block Units', verbose_name='number of Units')),
                ('residence', models.ForeignKey(help_text='residence for this block', on_delete=django.db.models.deletion.PROTECT, to='building.Residences', verbose_name='residences')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='unit',
            name='users',
            field=models.ManyToManyField(help_text='users for Units', through='building.UnitUser', to=settings.AUTH_USER_MODEL, verbose_name='users'),
        ),
    ]
