# Generated by Django 4.0.3 on 2022-04-21 10:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_scores_last_choice'),
    ]

    operations = [
        migrations.CreateModel(
            name='Annotation',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='main.page')),
                ('annot_id', models.IntegerField()),
            ],
            bases=('main.page',),
        ),
        migrations.AlterField(
            model_name='scores',
            name='last_choice',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.choice'),
        ),
    ]