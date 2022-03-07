# Generated by Django 4.0.2 on 2022-03-06 07:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mtb', '0006_alter_notes_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notes',
            name='owner',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
    ]
