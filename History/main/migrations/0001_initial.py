# Generated by Django 3.2.9 on 2022-03-31 07:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('photo', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('description', models.CharField(max_length=600)),
                ('last', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chapterId', models.IntegerField()),
                ('action', models.TextField()),
                ('result', models.BooleanField()),
                ('score', models.IntegerField()),
                ('page', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='main.page')),
            ],
        ),
    ]
