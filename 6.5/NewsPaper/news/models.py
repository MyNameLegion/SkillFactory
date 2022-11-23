from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum
from django.urls import reverse


class Author(models.Model):
    authorUser = models.OneToOneField(User, on_delete=models.CASCADE)
    authorRating = models.SmallIntegerField(default=0)

    def update_rating(self):
            postRat = self.post_set.aggregate(postRating=Sum('rating'))
            if postRat.get('postRating') is None:
                print("Вы еще не создавали пост")
                pRat = 0
            else:
                pRat = 0
                pRat += postRat.get('postRating')

            commentRat = self.authorUser.comment_set.aggregate(commentRating=Sum('rating'))
            if commentRat.get('commentRating') is None:
                print("Вы еще не оставляли комментарий")
                cRat = 0
            else:
                cRat = 0
                cRat += commentRat.get('commentRating')

            self.authorRating = pRat * 3 + cRat
            self.save()

    def __str__(self):
        return self.authorUser.username

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'


class Category(models.Model):
    category = models.CharField(max_length=64, unique=True, )
    subscribers = models.ManyToManyField(User, related_name='categories')

    def __str__(self):
        return f'{self.category}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Post(models.Model):
    NEWS = 'NW'
    ARTICLE = 'AR'

    CATEGORIES = [
        (NEWS, 'Новость'),
        (ARTICLE, 'статья'),
    ]
    author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name='Автор')
    categoryType = models.CharField(max_length=2, choices=CATEGORIES, default=NEWS, blank=False, verbose_name='Тип')
    date_time = models.DateTimeField(auto_now_add=True)
    category = models.ManyToManyField("Category", through="PostCategory", verbose_name='Категория')
    title = models.CharField(max_length=64, verbose_name='Заголовок')
    text = models.TextField(verbose_name='Текст')
    rating = models.SmallIntegerField(default=0, verbose_name='Рейтинг')

    def preview(self):
        return f"{self.text[0:124]} ..."

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

    def __str__(self):
        return f'{self.title} : {self.text[0:10]}...'

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'


class PostCategory(models.Model):
    post = models.ForeignKey("Post", on_delete=models.CASCADE)
    category = models.ForeignKey("Category", on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.post.title} | {self.category.category}'

    class Meta:
        verbose_name = 'Выбор категории'
        verbose_name_plural = 'Выбор категории'


class Comment(models.Model):
    post = models.ForeignKey("Post", on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    commentText = models.TextField()
    commentTime = models.DateTimeField(auto_now_add=True)
    rating = models.SmallIntegerField(default=0)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return f'{self.commentText}'
