# Generated by Django 3.0.2 on 2020-02-10 11:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('building', '0006_facilityresidence_facilityresidenceaccessabilities'),
    ]

    operations = [
        migrations.CreateModel(
            name='BoardOfDirector',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='object creation time', verbose_name='created')),
                ('modified', models.DateTimeField(auto_now=True, help_text='object modification time', verbose_name='modified')),
                ('role', models.CharField(help_text='role of board', max_length=255, verbose_name='role')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Residence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='object creation time', verbose_name='created')),
                ('modified', models.DateTimeField(auto_now=True, help_text='object modification time', verbose_name='modified')),
                ('name', models.CharField(help_text='residence name', max_length=255, verbose_name='name')),
                ('type', models.CharField(choices=[('BUILDING', 'Building'), ('COMPLEX', 'Complex'), ('LOCAL_SHOP', 'Local shop'), ('TOWN', 'Town')], default='BUILDING', help_text='type of this residence', max_length=32, verbose_name='type')),
                ('address', models.TextField(help_text='Address of residence', verbose_name='Address')),
                ('rules', models.TextField(help_text='rules for this residence', verbose_name='rules')),
                ('appendix_to_statute', models.TextField(help_text='appendix to statute for this residence', verbose_name='appendix to statute')),
                ('manager', models.ForeignKey(help_text='manager for this residence', on_delete=django.db.models.deletion.PROTECT, related_name='managers', to=settings.AUTH_USER_MODEL, verbose_name='manager')),
                ('parent_residence', models.ForeignKey(blank=True, help_text='parent residence for this residence', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='residence_parent', to='building.Residence', verbose_name='parent residence')),
                ('users_board', models.ManyToManyField(help_text='users board', through='building.BoardOfDirector', to=settings.AUTH_USER_MODEL, verbose_name='users board')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='residences',
            name='manager',
        ),
        migrations.RemoveField(
            model_name='residences',
            name='parent_residences',
        ),
        migrations.RemoveField(
            model_name='residences',
            name='users_board',
        ),
        migrations.RenameField(
            model_name='facilities',
            old_name='Units',
            new_name='units',
        ),
        migrations.RemoveField(
            model_name='unit',
            name='residences',
        ),
        migrations.AlterField(
            model_name='facilityresidence',
            name='blocks',
            field=models.ManyToManyField(help_text='blocks for this this facility residence', related_name='facility_residence', to='building.Block', verbose_name='blocks'),
        ),
        migrations.DeleteModel(
            name='BoardOfDirectors',
        ),
        migrations.AddField(
            model_name='boardofdirector',
            name='residence',
            field=models.ForeignKey(help_text='residence of board', on_delete=django.db.models.deletion.CASCADE, to='building.Residence', verbose_name='residence'),
        ),
        migrations.AddField(
            model_name='boardofdirector',
            name='user',
            field=models.ForeignKey(help_text='user of board', on_delete=django.db.models.deletion.CASCADE, related_name='residence_board', to=settings.AUTH_USER_MODEL, verbose_name='user'),
        ),
        migrations.AddField(
            model_name='unit',
            name='residence',
            field=models.ForeignKey(default=1, help_text='residence of this unit', on_delete=django.db.models.deletion.CASCADE, to='building.Residence', verbose_name='residence'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='block',
            name='residence',
            field=models.ForeignKey(help_text='residence for this block', on_delete=django.db.models.deletion.PROTECT, to='building.Residence', verbose_name='residence'),
        ),
        migrations.AlterField(
            model_name='facilityresidence',
            name='residence',
            field=models.ForeignKey(help_text='residence for this facility residence', on_delete=django.db.models.deletion.CASCADE, to='building.Residence', verbose_name='residence'),
        ),
        migrations.DeleteModel(
            name='Residences',
        ),
    ]
