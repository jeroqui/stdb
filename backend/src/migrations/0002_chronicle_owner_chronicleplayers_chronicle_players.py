# Generated by Django 4.1.5 on 2023-01-28 23:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('src', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='chronicle',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='chronicles_owned_set', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='ChroniclePlayers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.PositiveSmallIntegerField(choices=[(1, 'Story teller'), (2, 'Player'), (3, 'Guest')], default=1)),
                ('chronicle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='src.chronicle')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='chronicle',
            name='players',
            field=models.ManyToManyField(related_name='chronicles_as_player_set', through='src.ChroniclePlayers', to=settings.AUTH_USER_MODEL),
        ),
    ]
