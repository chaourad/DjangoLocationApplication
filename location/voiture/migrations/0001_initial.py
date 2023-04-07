# Generated by Django 4.1.7 on 2023-04-06 09:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Ville',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Voiture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matricule', models.CharField(max_length=100, null=True, unique=True)),
                ('modele', models.CharField(max_length=100, null=True)),
                ('marque', models.CharField(max_length=100, null=True)),
                ('prix_jour', models.DecimalField(decimal_places=2, max_digits=8)),
                ('isdisponibilite', models.BooleanField(default=False)),
                ('nombre_siege', models.IntegerField()),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='types', to='voiture.type')),
                ('ville', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='villes', to='voiture.ville')),
            ],
        ),
    ]