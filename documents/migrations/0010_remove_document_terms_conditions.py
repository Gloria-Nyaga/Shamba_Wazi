# Generated by Django 5.1.1 on 2024-09-09 09:52

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("documents", "0009_document_terms_conditions_alter_document_is_draft"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="document",
            name="terms_conditions",
        ),
    ]
