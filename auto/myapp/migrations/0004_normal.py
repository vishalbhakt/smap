# Generated by Django 5.1.6 on 2025-02-22 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_rename_tmmaddress_team_tmaddress_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Normal',
            fields=[
                ('name', models.CharField(max_length=100)),
                ('cpname', models.CharField(max_length=50)),
                ('cpcontactno', models.CharField(max_length=15)),
                ('cpemailaddress', models.EmailField(max_length=50, primary_key=True, serialize=False)),
                ('gstno', models.CharField(max_length=15)),
                ('regdate', models.CharField(max_length=20)),
            ],
        ),
    ]
