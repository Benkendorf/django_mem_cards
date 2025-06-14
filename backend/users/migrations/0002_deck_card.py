# Generated by Django 5.1.1 on 2024-11-01 16:23

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Deck',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deck_name', models.CharField(max_length=50, verbose_name='Название колоды')),
                ('review_in_progress', models.BooleanField(default=False, verbose_name='В процессе ревью')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='decks', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=50, verbose_name='Текст вопроса')),
                ('answer_1', models.CharField(blank=True, max_length=50, null=True, verbose_name='Первый ответ')),
                ('answer_2', models.CharField(blank=True, max_length=50, null=True, verbose_name='Второй ответ')),
                ('answer_3', models.CharField(blank=True, max_length=50, null=True, verbose_name='Третий ответ')),
                ('right_guesses', models.PositiveSmallIntegerField(default=0, verbose_name='Количество правильных ответов')),
                ('wrong_guesses', models.PositiveSmallIntegerField(default=0, verbose_name='Количество неправильных ответов')),
                ('datetime_created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('datetime_reviewed', models.DateTimeField(auto_now=True, verbose_name='Дата последнего ревью')),
                ('in_queue', models.BooleanField(default=False, verbose_name='В очереди на ревью')),
                ('srs_level', models.PositiveSmallIntegerField(default=0, verbose_name='Уровень SRS')),
                ('srs_xp', models.PositiveSmallIntegerField(default=0, verbose_name='Опыт SRS')),
                ('deck', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cards', to='users.deck')),
            ],
        ),
    ]
