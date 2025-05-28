from djongo import models
from django.urls import reverse
from bson import ObjectId

class Book(models.Model):
    _id = models.ObjectIdField(primary_key=True, default=ObjectId, editable=False)
    CATEGORY_CHOICES = [
        ('fiction', 'Fiction'),
        ('non-fiction', 'Non-Fiction'),
        ('science', 'Science'),
        ('technology', 'Technology'),
        ('history', 'History'),
        ('biography', 'Biography'),
        ('mystery', 'Mystery'),
        ('romance', 'Romance'),
        ('fantasy', 'Fantasy'),
        ('other', 'Other'),
    ]
    
    AVAILABILITY_CHOICES = [
        ('available', 'Available'),
        ('borrowed', 'Borrowed'),
        ('reserved', 'Reserved'),
        ('maintenance', 'Under Maintenance'),
    ]
    
    title = models.CharField(max_length=200, verbose_name="Titulli")
    author = models.CharField(max_length=150, verbose_name="Autori")
    isbn = models.CharField(max_length=13, unique=True, verbose_name="ISBN")
    description = models.TextField(blank=True, verbose_name="Përshkrimi")
    category = models.CharField(
        max_length=20, 
        choices=CATEGORY_CHOICES, 
        default='other',
        verbose_name="Kategoria"
    )
    image = models.ImageField(
        upload_to='books/', 
        blank=True, 
        null=True,
        verbose_name="Imazhi"
    )
    availability = models.CharField(
        max_length=15,
        choices=AVAILABILITY_CHOICES,
        default='available',
        verbose_name="Disponueshmëria"
    )
    publication_date = models.DateField(blank=True, null=True, verbose_name="Data e Publikimit")
    pages = models.PositiveIntegerField(blank=True, null=True, verbose_name="Numri i Faqeve")
    publisher = models.CharField(max_length=150, blank=True, verbose_name="Shtëpia Botuese")
    language = models.CharField(max_length=50, default='Albanian', verbose_name="Gjuha")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = "Libër"
        verbose_name_plural = "Libra"
    
    def __str__(self):
        return f"{self.title} - {self.author}"
    
    def get_absolute_url(self):
        return reverse('book_detail', kwargs={'pk': self.pk})
    
    def is_available(self):
        return self.availability == 'available'