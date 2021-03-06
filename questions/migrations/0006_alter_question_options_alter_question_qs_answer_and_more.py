# Generated by Django 4.0.2 on 2022-03-07 08:20

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('questions', '0005_remove_question_qs_likes_question_qs_likes_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='question',
            options={'ordering': ['-id']},
        ),
        migrations.AlterField(
            model_name='question',
            name='qs_answer',
            field=models.TextField(verbose_name='Answer'),
        ),
        migrations.RemoveField(
            model_name='question',
            name='qs_dislikes',
        ),
        migrations.AddField(
            model_name='question',
            name='qs_dislikes',
            field=models.ManyToManyField(blank=True, related_name='questions_dislike', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='question',
            name='qs_likes',
            field=models.ManyToManyField(blank=True, related_name='questions_like', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='question',
            name='qs_title',
            field=models.CharField(max_length=1000, unique=True, verbose_name='Question'),
        ),
        migrations.AlterField(
            model_name='question',
            name='qs_type',
            field=models.CharField(choices=[('General', 'General'), ('Definition', 'Definition'), ('Signs', 'Signs'), ('Mtb', 'Mtb')], max_length=1000, verbose_name='Type'),
        ),
    ]
