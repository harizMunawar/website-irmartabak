from django.db import models
from django.utils.text import slugify
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

class martabak(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    image = models.FileField(upload_to="img/martabak/%y/%m/%d")
    preview = ImageSpecField(
        source='image',
        processors=[ResizeToFill(200, 200)],
        format='JPEG',
        options={'quality': 85}
    )
    lowest_price = models.PositiveIntegerField(default=0)
    highest_price = models.PositiveIntegerField(default=0)
    variant = models.CharField(max_length=50, choices=[("Manis", "Manis"), ("Asin", "Asin")], default="Manis")
    size_besar = models.BooleanField(default="True")
    size_kecil = models.BooleanField(default="True")
    deskripsi = models.TextField()
    best_seller = models.CharField(max_length=50, choices=[("True", "True"), ("False", "False")], default="True")
    slug = models.SlugField(blank=True, editable=False)
    # rating = models.OneToOneField(Rating, on_delete=models.CASCADE)

    def delete(self, *args, **kwargs):
        # self.rating.delete()
        return super(martabak, self).delete(*args, **kwargs)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        # if not self.rating:
        #     self.rating = Rating.objects.create()
        super(martabak, self).save(*args, **kwargs)

    def __str__(self):
        return "{}".format(self.name)
