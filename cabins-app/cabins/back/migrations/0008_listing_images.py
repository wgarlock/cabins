# Generated by Django 3.1.3 on 2020-12-22 01:13

import django.db.models.deletion
import modelcluster.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0022_uploadedimage'),
        ('cabinsback', '0007_website'),
    ]

    operations = [
        migrations.CreateModel(
            name='ListingImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wagtailimages.image')),
                ('listing_page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='listing_images', to='cabinsback.listingpage')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
    ]
