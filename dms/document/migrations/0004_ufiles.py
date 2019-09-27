# Generated by Django 2.2 on 2019-05-21 18:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('document', '0003_auto_20190521_2340'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ufiles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Description1', models.TextField()),
                ('File', models.FileField(upload_to='')),
                ('Receiver1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receiver1', to='document.AddUser')),
                ('Sender1', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sender1', to='document.AddUser')),
            ],
        ),
    ]
