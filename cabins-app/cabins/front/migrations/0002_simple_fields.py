# Generated by Django 3.1.3 on 2020-12-19 04:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0059_apply_collection_ordering'),
        ('cabinsfront', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sitecontent',
            name='site',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='site_content', to='wagtailcore.site'),
        ),
    ]