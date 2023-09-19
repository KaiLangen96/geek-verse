# Generated by Django 3.2.20 on 2023-09-19 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=122)),
                ('email', models.EmailField(max_length=254)),
                ('questions_regarding', models.CharField(choices=[('ORDER', 'the order'), ('DELIVERT', 'the delivery'), ('RETURN', 'returning an order'), ('PAYMENT', 'the payment'), ('ACCOUNT', 'my account'), ('NEWSLETTER', 'the newsletter subscription'), ('OTHER', 'other')], default='O', max_length=254)),
                ('message', models.TextField(default='', max_length=500)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
