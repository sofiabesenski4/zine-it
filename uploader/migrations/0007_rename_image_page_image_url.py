# Generated by Django 5.1.2 on 2025-02-12 07:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('uploader', '0006_alter_page_zine'),
    ]

    operations = [
        migrations.RenameField(
            model_name='page',
            old_name='image',
            new_name='image_url',
        ),
    ]
