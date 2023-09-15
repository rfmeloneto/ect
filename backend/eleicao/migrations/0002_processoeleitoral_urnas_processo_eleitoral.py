# Generated by Django 4.2.5 on 2023-09-15 18:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eleicao', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProcessoEleitoral',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('numero', models.CharField(max_length=100)),
                ('is_valid', models.BooleanField()),
            ],
        ),
        migrations.AddField(
            model_name='urnas',
            name='processo_eleitoral',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='eleicao.processoeleitoral'),
            preserve_default=False,
        ),
    ]