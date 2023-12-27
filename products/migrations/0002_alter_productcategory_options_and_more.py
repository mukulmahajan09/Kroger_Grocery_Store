# Generated by Django 5.0 on 2023-12-27 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productcategory',
            options={'verbose_name': 'ProductCategory', 'verbose_name_plural': 'Product Categories'},
        ),
        migrations.RenameField(
            model_name='product',
            old_name='stock_status',
            new_name='stock_quantity',
        ),
        migrations.RemoveField(
            model_name='product',
            name='product_id',
        ),
        migrations.RemoveField(
            model_name='productcategory',
            name='category_id',
        ),
        migrations.AddField(
            model_name='product',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='id',
            field=models.BigAutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='is_available',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='product',
            name='modified_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(default='slug', max_length=500, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='productcategory',
            name='category_desc',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='productcategory',
            name='category_image',
            field=models.ImageField(blank=True, upload_to='products_categories/'),
        ),
        migrations.AddField(
            model_name='productcategory',
            name='id',
            field=models.BigAutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='productcategory',
            name='slug',
            field=models.SlugField(default='slug', max_length=500, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='product_image',
            field=models.ImageField(upload_to='products_images/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_name',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='productcategory',
            name='category_name',
            field=models.CharField(max_length=250),
        ),
    ]