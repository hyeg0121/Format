# Generated by Django 4.1.13 on 2024-06-13 03:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0002_question'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('responses', models.JSONField(default=list, verbose_name='Responses')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('survey', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='app.survey', verbose_name='설문조사')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'Answer',
                'verbose_name_plural': 'Answers',
            },
        ),
    ]