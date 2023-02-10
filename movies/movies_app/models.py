from datetime import date
from email.policy import default
from enum import unique
from pickle import TRUE
from tabnanny import verbose
from django.db import models
from django.urls import reverse
from mptt.models import MPTTModel, TreeForeignKey

class Category(models.Model):
    # films by category
    name =models.CharField('Категорія', max_length=150)
    description = models.TextField('Опис')
    url =models.SlugField(max_length=160)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = 'Kатегорія'
        verbose_name_plural = 'Kатегорії'
        

class Actor(models.Model):
    # actors 
    name = models.CharField('Ім\'я', max_length=100)
    age = models.PositiveSmallIntegerField('Вік', default=0)
    image = models.ImageField('Зображення', upload_to='actors/')
    description = models.TextField('Опис')

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return reverse('actor', kwargs={'slug' : self.name})

    class Meta:
        verbose_name = 'Актор'
        verbose_name_plural = 'Актори'

class Genre(models.Model):
    name = models.CharField('Назва', max_length=100)
    description = models.TextField('Опис')
    url =models.SlugField(max_length=160, unique=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанри'

class Movie(models.Model):
    title = models.CharField('Назва', max_length=100)
    tagline = models.CharField(verbose_name='Слоган', max_length=100, default='')
    description = models.TextField('Опис')
    poster = models.ImageField('Постер', upload_to='movies/')
    year = models.PositiveSmallIntegerField('Рік прем\'єри')
    country = models.CharField('Країна', max_length=30)
    director = models.ManyToManyField(Actor, verbose_name='режисер', related_name='film_director')
    actors = models.ManyToManyField(Actor, verbose_name='актори', related_name='film_actors')
    genres = models.ManyToManyField(Genre, verbose_name='жанри')
    world_premiere =models.DateField('Дата прем\'єри', default=date.today)
    budget = models.PositiveIntegerField('Бюджет', default=0, help_text='вказати суму в доларах США')
    fees_in_usa = models.PositiveIntegerField('Збори в світі', default=0, help_text='вказати суму в доларах США')
    category = models.ForeignKey(Category, verbose_name='Категорія', on_delete=models.SET_NULL, null=True)
    url = models.SlugField(max_length=160, unique=True)
    draft = models.BooleanField('Чорновик', default=False)

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'Фільм'
        verbose_name_plural = 'Фільми'

    def get_absolute_url(self):
        return reverse('single_movie',kwargs={'slug':self.url})


class MovieShot(models.Model):
    #кадри з фільму
    title = models.CharField('Назва', max_length=100)
    description = models.TextField('Опис')
    image = models.ImageField('Зображення', upload_to='movie_shots/')
    movie = models.ForeignKey(Movie, verbose_name='Фільм', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'Кадр'
        verbose_name_plural = 'Кадри'


class RatingStar(models.Model):
    value = models.PositiveSmallIntegerField('Значення', default=0)

    def __str__(self) -> str:
        return f'{self.value}'

    class Meta:
        verbose_name = 'Зірка рейтингу'
        verbose_name_plural = 'Зірки рейтингу'
        ordering = ['-value']

class Rating(models.Model):
    ip = models.CharField('ip адреса', max_length=15)
    star = models.ForeignKey(RatingStar, on_delete=models.CASCADE, verbose_name='зірка')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, verbose_name='фільм')

    def __str__(self) -> str:
        return f'{self.star} - {self.movie}' 

    class Meta:
        verbose_name = 'Рейтинг'
        verbose_name_plural = 'Рейтинги'

class Review(models.Model):
    email = models.EmailField()
    name = models.CharField('Назва', max_length=100)
    text = models.TextField(verbose_name='Повідомлення', max_length=5000)
    parent = models.ForeignKey('self', verbose_name='батько', on_delete=models.SET_NULL, null=True, blank=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, verbose_name='фільм')
    
    def __str__(self) -> str:
        return f'{self.name} - {self.movie}'


    class Meta:
        verbose_name = 'Відгук'
        verbose_name_plural = 'Відгуки'

class ReviewViaMptt(MPTTModel):
    email = models.EmailField()
    name = models.CharField('Назва', max_length=100)
    text = models.TextField(verbose_name='Повідомлення', max_length=5000)
    parent = TreeForeignKey('self', verbose_name='батько', on_delete=models.SET_NULL, null=True, blank=True, related_name='children')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, verbose_name='фільм')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return f'{self.name} - {self.movie}'


    class MPTTMeta:
        order_insertion_by = ['-created_at']
        
    

        









    
    

