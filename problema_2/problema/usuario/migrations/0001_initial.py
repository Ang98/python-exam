# Generated by Django 3.1.2 on 2020-10-05 00:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.CharField(blank=True, default='', max_length=45)),
                ('apellido_p', models.CharField(blank=True, default='', max_length=45)),
                ('apellido_m', models.CharField(blank=True, default='', max_length=45)),
                ('edad', models.IntegerField()),
            ],
        ),
    ]
