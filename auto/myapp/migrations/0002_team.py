# Generated by Django 5.1.6 on 2025-02-22 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('tmmname', models.CharField(max_length=100)),
                ('tmmwork', models.TextField()),
                ('tmmaddress', models.TextField()),
                ('tmname', models.CharField(max_length=50)),
                ('tmcontactno', models.CharField(max_length=15)),
                ('tmemailaddress', models.EmailField(max_length=50, primary_key=True, serialize=False)),
                ('aadharno', models.CharField(max_length=12)),
                ('panno', models.CharField(max_length=10)),
                ('regdate', models.CharField(max_length=20)),
            ],
        ),
    ]
