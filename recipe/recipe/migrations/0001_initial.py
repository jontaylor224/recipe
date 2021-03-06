# Generated by Django 2.2.3 on 2020-01-31 20:51

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
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('bio', models.TextField(blank=True, null=True, verbose_name='Bio')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=200)),
                ('time_req', models.CharField(max_length=20)),
                ('instructions', models.TextField(blank=True, null=True, verbose_name='Instructions')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipe.Author')),
                ('favorites', models.ManyToManyField(blank=True, related_name='favorite', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
