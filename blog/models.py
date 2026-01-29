from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255, unique=True,
                            verbose_name="Название")
    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name="Дата создания")
    slug = models.SlugField(unique=True)

    def __str__(self):
        return f"ID: {self.id} --- NAME: {self.name}"

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

class Tag(models.Model):
    name = models.CharField(max_length=255, unique=True,
                            verbose_name="Название")
    slug = models.SlugField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name="Дата создания")

    def __str__(self):
        return f"ID: {self.id} --- NAME: {self.name}"

    class Meta:
        verbose_name = "Тег"
        verbose_name_plural = "Теги"

class Post(models.Model):
    title = models.CharField(max_length=255, unique=True,
                             verbose_name="Заголовок")
    content = models.TextField(verbose_name="Содержание")
    category = models.ForeignKey(Category, on_delete=models.CASCADE,
                                 verbose_name="Категория")
    tags = models.ManyToManyField(Tag, related_name='posts',
                                  verbose_name="Теги")
    photo = models.ImageField(upload_to="posts/", null=True, blank=True,
                              verbose_name="Изображение")
    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True,
                                      verbose_name="Дата обновления")
    slug = models.SlugField(unique=True)
    views = models.PositiveIntegerField(default=0,
                                        verbose_name="Просмотры")
    reading_time = models.PositiveIntegerField(default=0,
                                               verbose_name="Время для чтения")

    def __str__(self):
        return f"ID: {self.id} --- NAME: {self.title}"

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"