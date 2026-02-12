from django.db import models

# Create your models here.



class Account(models.Model):
    pochta = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    full_name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    balance = models.FloatField()

    def __str__(self):
        return self.full_name
    



from django.db import models

class Category(models.Model):
    CATEGORY_CHOICES = [
        ('car', 'Car'),
        ('job', 'Job'),
        ('house', 'House'),
        ('animal', 'Animal'),
    ]

    tip = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES,
        unique=True
    )

    def __str__(self):
        return self.get_tip_display()
    


class AD(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='ads_by_category'  # unique reverse name
    )
    tip = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='ads_by_tip'  # unique reverse name
    )
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    describe = models.TextField()
    region = models.CharField(max_length=200)
    price = models.FloatField()
    title = models.CharField(max_length=200)
    # image = models.ImageField(upload_to='ads_images/')

    def __str__(self):
        return f"{self.title} - {self.region} - {self.price}"




class Car(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    marka = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    mileage = models.FloatField()
    fuel_type = models.CharField(max_length=50)
    transmission = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    kolichestvo_xozyayev = models.IntegerField()

    def __str__(self):
        return f"{self.marka} {self.model} ({self.year})"




class Job(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    category_job = models.CharField(max_length=100)
    salary = models.FloatField()
    tipwork = models.CharField(max_length=100)
    tipzanyatosti = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} at {self.company} - {self.category} - {self.salary}"




class House(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    address = models.CharField(max_length=200)
    price = models.FloatField()
    region = models.CharField(max_length=100)
    tip = models.CharField(max_length=100)
    describe = models.TextField()
    area = models.FloatField()
    rooms = models.IntegerField()
    gotinflat = models.TextField()
    floor = models.IntegerField()

    def __str__(self):
        return f"{self.address} - {self.region} - {self.price}"




class Animal(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    tip = models.CharField(max_length=100)
    poroda = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.tip} - {self.poroda}"


    



    

