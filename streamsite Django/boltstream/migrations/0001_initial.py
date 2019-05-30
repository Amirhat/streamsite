# Generated by Django 2.2.1 on 2019-05-27 15:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.crypto
import functools


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Stream',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(default=functools.partial(django.utils.crypto.get_random_string, *(20,), **{}), max_length=20, unique=True)),
                ('started_at', models.DateTimeField(blank=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='stream', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
