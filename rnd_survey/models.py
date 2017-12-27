from django.db import models
import pandas as pd
# Create your models here.


class Dataset(models.Model):
    name = models.CharField(max_length=30)

    excel_slot = models.FileField(upload_to='uploads/')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        orgs_data = pd.read_excel(self.excel_slot)

        print(orgs_data)

        for index, row in orgs_data.iterrows():
            organization, created = Organization.objects.get_or_create(
                name=row['기관명'],
                researchers_female=row['여성연구원'],
                researchers_male=row['남성연구원'],
            )

        super(Dataset, self).save(*args, **kwargs)


class Organization(models.Model):
    name = models.CharField(max_length=30)
    researchers = models.IntegerField(default=0)
    researchers_male = models.IntegerField(default=0)
    researchers_female = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return '/rnd_survey/{}/'.format(self.id)

    def save(self, *args, **kwargs):
        self.researchers = self.researchers_female + self.researchers_male
        super(Organization, self).save(*args, **kwargs)
