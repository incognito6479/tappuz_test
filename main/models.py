from django.db import models
from django.contrib.auth.models import AbstractUser


DEPARTMENT_STATUS = (
    ('active', 'Активный'),
    ('inactive', 'Неактивный'),
)


class CustomUser(AbstractUser):
    department = models.ForeignKey('Department', on_delete=models.PROTECT, verbose_name="Отдел",
                                   blank=True, null=True, related_name='department')
    first_name = models.CharField(max_length=255, verbose_name="Имя")
    last_name = models.CharField(max_length=255, verbose_name="Фамилия")
    middle_name = models.CharField(max_length=255, verbose_name="Отчество")
    phone_number = models.CharField(max_length=11, unique=True, verbose_name="Телефон")

    # REQUIRED_FIELDS = ['first_name', 'last_name', 'middle_name', 'phone_number']

    def __str__(self):
        return f"{self.username}"

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


class Department(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    department_name = models.CharField(max_length=255, verbose_name="Названия отдела")
    department_status = models.CharField(max_length=255, choices=DEPARTMENT_STATUS, default='active',
                                         verbose_name="Статус")
    employee_number = models.IntegerField(verbose_name="Кол.во сотрудников", default=0)

    def __str__(self):
        return f"{self.department_name}"

    class Meta:
        verbose_name = "Отдел"
        verbose_name_plural = "Отделы"
