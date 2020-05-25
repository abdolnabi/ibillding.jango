# Generated by Django 3.0.2 on 2020-05-25 05:31

from django.db import migrations, models
import django.db.models.deletion

from building.models import AccountingTarget


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('building', '0016_auto_20200409_2036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accountingtarget',
            name='content_type',
            field=models.ForeignKey(choices=AccountingTarget.get_accounting_target_choice(), help_text='content type', limit_choices_to=models.Q(models.Q(('app_label', 'building'), ('model', 'residence')), models.Q(('app_label', 'building'), ('model', 'block')), models.Q(('app_label', 'building'), ('model', 'unit')), _connector='OR'), on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType', verbose_name='content type'),
        ),
    ]
