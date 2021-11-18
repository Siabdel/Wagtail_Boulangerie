# Generated by Django 3.2.9 on 2021-11-18 12:48

from django.db import migrations, models
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FooterText',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', wagtail.core.fields.RichTextField()),
            ],
            options={
                'verbose_name_plural': 'Footer Text',
            },
        ),
        migrations.DeleteModel(
            name='Book',
        ),
        migrations.RemoveField(
            model_name='grocery',
            name='category',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Grocery',
        ),
    ]
