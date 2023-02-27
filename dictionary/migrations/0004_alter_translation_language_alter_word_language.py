# Generated by Django 4.1.7 on 2023-02-27 18:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dictionary', '0003_alter_word_language'),
    ]

    operations = [
        migrations.AlterField(
            model_name='translation',
            name='language',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dictionary.language', verbose_name="Translation's language"),
        ),
        migrations.AlterField(
            model_name='word',
            name='language',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='words', to='dictionary.language', verbose_name="Word's language"),
        ),
    ]
