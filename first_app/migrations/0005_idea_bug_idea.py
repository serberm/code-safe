# Generated by Django 3.0.5 on 2020-05-07 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0004_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='idea_bug',
            name='idea',
            field=models.BooleanField(default=False),
        ),
    ]
