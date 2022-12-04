# Generated by Django 3.2 on 2022-11-24 07:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('catalog', '0002_auto_20221110_1328'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookinstance',
            name='borrowed',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='author',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True, verbose_name='born'),
        ),
        migrations.AlterField(
            model_name='bookinstance',
            name='id',
            field=models.UUIDField(default=uuid.UUID('18057272-ff13-421f-92e0-cdf7d4c01462'), help_text='Unique ID for this particular book across whole library', primary_key=True, serialize=False),
        ),
    ]
