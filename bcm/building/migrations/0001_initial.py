# Generated by Django 3.0.2 on 2020-01-30 16:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Residences',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='object creation time', verbose_name='created')),
                ('modified', models.DateTimeField(auto_now=True, help_text='object modification time', verbose_name='modified')),
                ('name', models.CharField(help_text='residences name', max_length=255, verbose_name='name')),
                ('type', models.CharField(choices=[('BUILDING', 'Building'), ('COMPLEX', 'Complex'), ('LOCAL_SHOP', 'Local shop'), ('TOWN', 'Town')], default='BUILDING', help_text='type of this residences', max_length=32, verbose_name='type')),
                ('address', models.TextField(help_text='Address of residences', verbose_name='Address')),
                ('rules', models.TextField(help_text='rules for this residences', verbose_name='rules')),
                ('appendix_to_statute', models.TextField(help_text='appendix to statute for this residences', verbose_name='appendix to statute')),
                ('manager', models.ForeignKey(help_text='manager for this residences', on_delete=django.db.models.deletion.PROTECT, related_name='managers', to=settings.AUTH_USER_MODEL, verbose_name='manager')),
                ('parent_residences', models.ForeignKey(help_text='parent residences for this residences', on_delete=django.db.models.deletion.PROTECT, related_name='residences_parent', to='building.Residences', verbose_name='parent residences')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
