# Generated by Django 4.2.10 on 2024-02-28 22:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_comment_options_alter_comment_author'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-created_on']},
        ),
    ]
