# Generated by Django 3.2.4 on 2021-06-13 11:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('country_of_origin', models.CharField(blank=True, max_length=255, null=True)),
                ('image', models.CharField(default='https://s.gr-assets.com/assets/nophoto/user/m_200x266-d279b33f8eec0f27b7272477f09806be.png', max_length=255)),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('slug', models.SlugField()),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='BookType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField()),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('sypnosis', models.CharField(max_length=9999)),
                ('image', models.CharField(max_length=255)),
                ('genres', models.CharField(max_length=9999)),
                ('publish_date', models.CharField(blank=True, max_length=255, null=True)),
                ('publishers', models.CharField(max_length=255)),
                ('is_bestseller', models.BooleanField(default=False)),
                ('number_of_pages', models.IntegerField()),
                ('slug', models.SlugField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='books', to='book.author')),
                ('book_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='books', to='book.booktype')),
            ],
            options={
                'ordering': ('-title',),
            },
        ),
    ]
