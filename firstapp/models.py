from django.db import models

# Create your models here.
    


class Account(models.Model):
    pochta = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    full_name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    balance = models.DecimalField( max_digits=12, decimal_places=2)

    def __str__(self):
        return self.full_name
    



from django.db import models

class Category(models.Model):
    tip  = models.CharField( max_length=50,unique=True)

    def __str__(self):
        return self.tip
    


class Region(models.Model):
    regions = models.CharField(max_length=100)

    def __str__(self):
        return self.regions



"""class Images(models.Model):
        image = models.ImageField(upload_to='ads_images/')
        
    
        def __str__(self):
            return f"Image for AD: {self.ad.title}"
        """



class AD(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='ads_by_category', )
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    describe = models.TextField()
    price = models.DecimalField(max_digits=11, decimal_places=1)
    title = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.title} - {self.region} - {self.price}"




class Car(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    reklama = models.ForeignKey(AD, on_delete=models.CASCADE)
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
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    reklama = models.ForeignKey(AD, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    category_job = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=11, decimal_places=2)
    tipwork = models.CharField(max_length=100)
    tipzanyatosti = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} at {self.company} - {self.category} - {self.salary}"




class House(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    reklama = models.ForeignKey(AD, on_delete=models.CASCADE)
    address = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=11, decimal_places=2)

    tip = models.CharField(max_length=100)
    describe = models.TextField()
    area = models.FloatField()
    rooms = models.IntegerField()
    floor = models.FloatField()

    def __str__(self):
        return f"{self.address} - {self.region} - {self.price}"




class Animal(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    reklama = models.ForeignKey(AD, on_delete=models.CASCADE)
    tip = models.CharField(max_length=100)
    poroda = models.CharField(max_length=100)
    age = models.FloatField()
    color = models.CharField(max_length=50)


    def __str__(self):
        return f"{self.tip} - {self.poroda}"


    

