# Generated by Django 3.0.2 on 2020-01-31 09:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('building', '0005_auto_20200130_2008'),
    ]

    operations = [
        migrations.CreateModel(
            name='FacilityResidence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='object creation time', verbose_name='created')),
                ('modified', models.DateTimeField(auto_now=True, help_text='object modification time', verbose_name='modified')),
                ('second_title', models.CharField(help_text='second title for this facility residence', max_length=255, verbose_name='second title')),
                ('description', models.TextField(help_text='description for this facility residence', verbose_name='description')),
                ('requestable', models.BooleanField(default=False, help_text='requestable for this facility residence', verbose_name='requestable')),
                ('price', models.DecimalField(decimal_places=2, help_text='price for this facility residence', max_digits=10, verbose_name='price')),
                ('blocks', models.ManyToManyField(help_text='blocks for this this facility residence', related_name='facility_residences', to='building.Block', verbose_name='blocks')),
                ('facility', models.ForeignKey(help_text='facility for this facility residence', on_delete=django.db.models.deletion.CASCADE, to='building.Facilities', verbose_name='facility')),
                ('residence', models.ForeignKey(help_text='residence for this facility residence', on_delete=django.db.models.deletion.CASCADE, to='building.Residences', verbose_name='residence')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FacilityResidenceAccessabilities',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='object creation time', verbose_name='created')),
                ('modified', models.DateTimeField(auto_now=True, help_text='object modification time', verbose_name='modified')),
                ('type', models.CharField(choices=[('PUBLIC', 'Public'), ('BLOCK', 'Block'), ('UNIT', 'Unit'), ('RESIDENCE', 'Residence')], help_text='choose type for this accessibility', max_length=32, verbose_name='type')),
                ('accessible', models.BigIntegerField(help_text='accessible for this accessibility', verbose_name='accessible')),
                ('facility_residence', models.ForeignKey(help_text='facility residence for this object', on_delete=django.db.models.deletion.CASCADE, to='building.FacilityResidence', verbose_name='facility residence')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
