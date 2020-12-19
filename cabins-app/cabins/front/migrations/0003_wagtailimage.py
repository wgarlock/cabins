# Generated by Django 3.1.3 on 2020-12-19 17:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0022_uploadedimage'),
        ('cabinsfront', '0002_simple_fields'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sitecontent',
            name='logo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='site_logo', to='wagtailimages.image'),
        ),
    ]