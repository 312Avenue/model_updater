import os
from django.db import models
from django.core.files import File

from media.scripts import users_data


class Street(models.Model):
    street = models.CharField(verbose_name='Название улицы', max_length=50, primary_key=True, unique=True)

    class Meta:
        verbose_name = 'Улица'
        verbose_name_plural = 'Улицы'

    def __str__(self):
        return self.street
    

class Home(models.Model):
    street_for = models.ForeignKey(Street, verbose_name='Улица', on_delete=models.CASCADE, related_name='homes')
    home = models.CharField(verbose_name='Дом', max_length=10, primary_key=True, unique=True)
    ent = models.CharField(verbose_name='Количество подъездов', max_length=10)
    apps = models.CharField(verbose_name='Количество квартир', max_length=10)
    file = models.FileField(verbose_name='Файл с данными', upload_to='xlsx', blank=True, null=True)
    active = models.CharField(verbose_name='Активный', max_length=10, blank=True, null=True)
    deactive = models.CharField(verbose_name='Неактивный', max_length=10, blank=True, null=True)
    # internet = models.CharField(verbose_name='Абоненты с интернетом', max_length=10, blank=True, null=True)
    # domofon = models.CharField(verbose_name='Абоненты домофонии', max_length=10, blank=True, null=True)

    class Meta:
        verbose_name = 'Дом'
        verbose_name_plural = 'Дома'

    def __str__(self) -> str:
        return f'{self.street_for} {self.home}'
    
    def save(self, *args, **kwargs):
        if not self.file:
            file_path = users_data(self.street_for.street, self.home)

            with open(file_path[0], 'rb') as f:
                self.file.save(os.path.basename(file_path[0]), File(f), save=False)
        
        if not self.active:
            self.active = file_path[1]
        
        if not self.deactive:
            self.deactive = file_path[2]

        # if not self.internet:
        #     self.internet = file_path[3]

        # if not self.domofon:
        #     self.domofon = file_path[4]
        
        super().save(*args, **kwargs)
    