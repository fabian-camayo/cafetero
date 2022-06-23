# Generated by Django 3.2.7 on 2021-09-26 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_batch_history'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='batch',
            name='history',
        ),
        migrations.AddField(
            model_name='batch',
            name='history_almacenado',
            field=models.TextField(default={}),
        ),
        migrations.AddField(
            model_name='batch',
            name='history_despulpado',
            field=models.TextField(default={}),
        ),
        migrations.AddField(
            model_name='batch',
            name='history_etiquetado',
            field=models.TextField(default={}),
        ),
        migrations.AddField(
            model_name='batch',
            name='history_fermentacion',
            field=models.TextField(default={}),
        ),
        migrations.AddField(
            model_name='batch',
            name='history_lavado',
            field=models.TextField(default={}),
        ),
        migrations.AddField(
            model_name='batch',
            name='history_recoleccion',
            field=models.TextField(default={}),
        ),
        migrations.AddField(
            model_name='batch',
            name='history_secado',
            field=models.TextField(default={}),
        ),
        migrations.AddField(
            model_name='batch',
            name='history_tostado',
            field=models.TextField(default={}),
        ),
        migrations.AddField(
            model_name='batch',
            name='history_trillado',
            field=models.TextField(default={}),
        ),
        migrations.AlterField(
            model_name='batch',
            name='coffe_type',
            field=models.CharField(choices=[('1', 'ARABIGO'), ('2', 'ROBUSTA')], max_length=15),
        ),
    ]