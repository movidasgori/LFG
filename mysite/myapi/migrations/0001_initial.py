# Generated by Django 3.2.7 on 2021-09-30 16:38

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
            name='Juego',
            fields=[
                ('nombre', models.CharField(max_length=200, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Party',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=200)),
                ('nombre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapi.juego')),
            ],
        ),
        migrations.CreateModel(
            name='PartyPlayers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jugador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('party', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapi.party')),
            ],
        ),
        migrations.CreateModel(
            name='PartyChat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comentario', models.CharField(max_length=200)),
                ('jugador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapi.partyplayers')),
                ('sala', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapi.party')),
            ],
        ),
        migrations.AddConstraint(
            model_name='partyplayers',
            constraint=models.UniqueConstraint(fields=('party', 'jugador'), name='jugador unico party'),
        ),
    ]
