# Generated by Django 3.1.2 on 2020-11-13 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('nofp', models.IntegerField()),
                ('prize', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
