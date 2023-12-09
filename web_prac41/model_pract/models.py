from django.db import models

from web_prac41.settings import BASE_DIR

# Create your models here.

class PracticeModel(models.Model):
    roll = models.BigAutoField(primary_key=True)
    ageInSeconds = models.BigIntegerField()
    dataField = models.BinaryField()
    boolean = models.BooleanField()
    char = models.CharField(max_length=30)
    date = models.DateField()
    dateTime = models.DateTimeField()
    deci = models.DecimalField(decimal_places=6,max_digits=15)
    duration = models.DurationField()
    email = models.EmailField()
    fileField = models.FileField()
    filePath = models.FilePathField(path=BASE_DIR.as_posix())
    floating = models.FloatField()
    img = models.ImageField()
    integer = models.IntegerField()
    json = models.JSONField()
    positiveBigInt = models.PositiveBigIntegerField()
    slug = models.SlugField()
    article = models.TextField()
    url = models.URLField()
    uuid = models.UUIDField()

    def __str__(self):
        return str(self.roll)
    


class OnnoModel(models.Model):
    practice = models.ForeignKey(PracticeModel,on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    ip = models.GenericIPAddressField()

    def __str__(self) -> str:
        return self.name