from django.db import models
from django.utils.text import slugify
from datetime import timedelta

class Service(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    duration = models.DurationField(default=timedelta(minutes=30))  # Тривалість процедури

    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(upload_to='services/', blank=True, null=True)

    @property
    def duration_str(self):
        """Повертає тривалість у зручному форматі — для відображення в шаблоні"""
        total_minutes = int(self.duration.total_seconds() // 60)
        hours = total_minutes // 60
        minutes = total_minutes % 60
        if hours and minutes:
            return f"{hours} год {minutes} хв"
        elif hours:
            return f"{hours} год"
        else:
            return f"{minutes} хв"
    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.name)
            slug = base_slug
            num = 1
            while Service.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{num}"
                num += 1
            self.slug = slug
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Master(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='masters/', blank=True, null=True)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Appointment(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    master = models.ForeignKey(Master, on_delete=models.CASCADE)
    client_name = models.CharField(max_length=100)
    client_phone = models.CharField(max_length=20)
    appointment_datetime = models.DateTimeField()

    def __str__(self):
        return f"{self.client_name} - {self.service.name} з {self.master.name} о {self.appointment_datetime.strftime('%Y-%m-%d %H:%M')}"

class GalleryImage(models.Model):
    image = models.ImageField(upload_to='gallery/')
    caption = models.CharField(max_length=255, blank=True)