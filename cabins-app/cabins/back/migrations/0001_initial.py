# Generated by Django 3.1.3 on 2020-12-19 17:28

import cabins.page.models
from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0059_apply_collection_ordering'),
        ('cabinscore', '0002_add_simple_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomePage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('description', wagtail.core.fields.RichTextField()),
                ('meta_description', models.CharField(blank=True, max_length=120, null=True)),
                ('og_description', models.CharField(blank=True, max_length=300, null=True)),
                ('og_image', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='cabinscore.image')),
            ],
            options={
                'abstract': False,
            },
            bases=(cabins.page.models.AbstractBasePage, 'wagtailcore.page'),
        ),
    ]