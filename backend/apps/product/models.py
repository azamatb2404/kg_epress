from django.db import models

class Category(models.Model):
    name = models.CharField('название', max_length=50, unique=True)
    slug = models.SlugField('Слаг', max_length=60, unique=True)


    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['name']


    def __str__(self):
        return self.name

class SubCategory(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="subcategories"
    )
    name = models.CharField('название', max_length=50, unique=True)
    slug = models.SlugField('Слаг', max_length=60, unique=True)

    class Meta:
        verbose_name = "Подкатегория"
        verbose_name_plural = "Подкатегории"
        ordering = ['category', 'name']

    def __str__(self):
        return self.name




class Product(models.Model):
    name = models.CharField("название", max_length=225)
    description = models.TextField("описание")
    price = models.DecimalField(
        "цена",
        max_digits=10,
        decimal_places=2
    )
    image = models.ImageField("Фото", upload_to="product_image/")
    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT
    )
    subcategory = models.ForeignKey(
        SubCategory,
        on_delete=models.PROTECT
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField("активный", default=True)


    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
        ordering = ['-created']

    def __str__(self):
        return self.name

class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='review')
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="review")
    text = models.TextField("Отзыв")
    created = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField("Активный", default=True)


    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
        ordering = ['-created']

    def __str__(self):
        return f'{self.id}'

