# Generated by Django 5.1.1 on 2024-09-21 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agendamento', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Servico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
            ],
        ),
    ]
