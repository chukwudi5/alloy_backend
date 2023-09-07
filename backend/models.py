from django.db import models

class Application(models.Model):
    name_first = models.CharField(max_length=200)
    name_last = models.CharField(max_length=200)
    email_address = models.EmailField(max_length=200)
    address_line_1 = models.CharField(max_length=200)
    address_city = models.CharField(max_length=200)
    address_state = models.CharField(max_length=2)
    address_country_code = models.CharField(max_length=2)
    address_postal_code = models.CharField(max_length=5)
    phone_number = models.CharField(max_length=10)
    birth_date = models.DateField()
    document_ssn = models.CharField(max_length=9)

    def __str__(self):
        return self.name_first