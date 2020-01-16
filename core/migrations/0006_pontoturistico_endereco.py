# Generated by Django 3.0.2 on 2020-01-16 18:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('localizacao', '0001_initial'),
        ('core', '0005_pontoturistico_avaliacoes'),
    ]

    operations = [
        migrations.AddField(
            model_name='pontoturistico',
            name='endereco',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='localizacao.Localizacao'),
            preserve_default=False,
        ),
    ]
