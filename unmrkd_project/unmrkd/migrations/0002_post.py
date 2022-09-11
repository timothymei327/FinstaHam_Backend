# Generated by Django 4.1.1 on 2022-09-11 07:07

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('unmrkd', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo_urls', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), size=10)),
                ('caption', models.TextField()),
                ('hashtags', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), size=10)),
                ('forum', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='unmrkd.forum')),
            ],
        ),
    ]
