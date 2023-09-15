# Generated by Django 4.2.5 on 2023-09-15 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eleicao', '0003_alter_cidades_muni_alter_urnas_apta_alter_urnas_apto_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cidades',
            name='muni',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='urnas',
            name='apta',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='urnas',
            name='apto',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='urnas',
            name='bran',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='urnas',
            name='carg',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='urnas',
            name='comp',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='urnas',
            name='datab',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='urnas',
            name='dtfc',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='urnas',
            name='dtpl',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='urnas',
            name='falt',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='urnas',
            name='hrab',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='urnas',
            name='hrfc',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='urnas',
            name='idca',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='urnas',
            name='idel',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='urnas',
            name='idue',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='urnas',
            name='loca',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='urnas',
            name='nomi',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='urnas',
            name='nulo',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='urnas',
            name='plei',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='urnas',
            name='proc',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='urnas',
            name='seca',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='urnas',
            name='tipo',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='urnas',
            name='totc',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='urnas',
            name='turn',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='urnas',
            name='verc',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='urnas',
            name='vrch',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='urnas',
            name='zona',
            field=models.CharField(max_length=100),
        ),
    ]
