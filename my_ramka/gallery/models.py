from django.db import models
from django.conf import settings
from django.urls import reverse


User = settings.AUTH_USER_MODEL
MAX_LENGTH_FIELD = 15
MAX_LENGTH_SUBSTRING = 35


class CreatedAtModel(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True,
        null=True,
        verbose_name="Добавлено",
    )

    class Meta:
        abstract = True


class IsPublishedModel(models.Model):
    is_published = models.BooleanField(
        default=True,
        verbose_name="Опубликовано",
        help_text="Снимите галочку, чтобы скрыть публикацию.",
    )

    class Meta:
        abstract = True


class Location(CreatedAtModel, IsPublishedModel):
    name = models.CharField(
        max_length=MAX_LENGTH_FIELD,
        verbose_name="Название места",
    )

    class Meta:
        verbose_name = "местоположение"
        verbose_name_plural = "Местоположения"

    def __str__(self):
        return self.name[:MAX_LENGTH_SUBSTRING]


class Category(CreatedAtModel):
    title = models.CharField(
        max_length=MAX_LENGTH_FIELD, verbose_name="Заголовок"
    )
    description = models.TextField(verbose_name="Описание")
    slug = models.SlugField(
        unique=True,
        verbose_name="Идентификатор",
        help_text=(
            "Идентификатор страницы для URL;"
            "разрешены символы латиницы, цифры, дефис и подчёркивание."
        )
    )

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.title[:MAX_LENGTH_SUBSTRING]

    def get_absolute_url(self):
        return reverse("blog:category_posts", args=[self.slug])


class Post(CreatedAtModel, IsPublishedModel):
    title = models.CharField(
        max_length=MAX_LENGTH_FIELD,
        verbose_name="Заголовок",
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="Автор публикации",
    )
    location = models.ForeignKey(
        Location,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        verbose_name="Местоположение",

    )
    category = models.ForeignKey(
        Category,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        verbose_name="Категория",

    )
    image = models.ImageField(
        "Фото", upload_to="posts_images", blank=True)

    class Meta:
        verbose_name = "публикация"
        verbose_name_plural = "Публикации"
        default_related_name = "posts"

    def __str__(self):
        return self.title[:MAX_LENGTH_SUBSTRING]

    # def get_absolute_url(self):
    #     return reverse("blog:post_detail", args=[self.pk])
