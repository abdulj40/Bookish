# Generated by Django 2.1 on 2019-11-14 14:46

import books.validator
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_auto_20191106_1450'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='afri_books',
            field=models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='pdf',
            field=models.FileField(upload_to='books/pdfs/', validators=[books.validator.FileValidator(content_types=('application/pdf',), max_size=25062000)]),
        ),
    ]
