# Generated by Django 3.2.9 on 2022-04-19 09:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_scores'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scores',
            name='last_page',
        ),
        migrations.AddField(
            model_name='choice',
            name='result_page',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='result_page', to='main.page'),
        ),
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='main.page')),
            ],
        ),
        migrations.AddField(
            model_name='scores',
            name='last_chapter',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='main.chapter'),
        ),
    ]
