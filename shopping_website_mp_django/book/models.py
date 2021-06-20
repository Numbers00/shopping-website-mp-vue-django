from django.db import models

class BookType(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField()

    class Meta:
        ordering = ('name',)
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/{self.slug}/'

class Author(models.Model):
    name = models.CharField(max_length=255)
    country_of_origin = models.CharField(max_length=255, blank=True, null=True)
    image = models.CharField(max_length=255, default='https://s.gr-assets.com/assets/nophoto/user/m_200x266-d279b33f8eec0f27b7272477f09806be.png')
    description = models.CharField(max_length=255, blank=True, null=True)
    slug = models.SlugField()

    class Meta:
        ordering = ('name',)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return f'/{self.slug}/'

class Book(models.Model):
    ONGOING = 'ongoing'
    COMPLETED = 'completed'
    DISCONTINUED = 'discontinued'

    STATUS_CHOICES = (
        (ONGOING, 'Ongoing'),
        (COMPLETED, 'Completed'),
        (DISCONTINUED, 'Discontinued')
    )

    book_type = models.ForeignKey(BookType, related_name='books', on_delete=models.CASCADE)
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    sypnosis = models.CharField(max_length=9999)
    image = models.CharField(max_length=255)
    genres = models.CharField(max_length=9999)
    status = models.CharField(max_length=255, choices=STATUS_CHOICES, blank=True, null=True)
    publish_date = models.CharField(max_length=255, blank=True, null=True)
    publishers = models.CharField(max_length=255, blank=True, null=True)
    is_bestseller = models.BooleanField(default=False)
    number_of_pages = models.IntegerField()
    slug = models.SlugField()

    class Meta:
        ordering = ('title',)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return f'/{self.book_type.slug}/{self.author.slug}/{self.slug}/'