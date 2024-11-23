from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class CustomUser(AbstractUser):
    """
    Foydalanuvchilarni toifaga ajratish
    """
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('waiter', 'Waiter'),
        ('user', 'User'),
    ]

    role = models.CharField(_('Foydalanuvchi toifasi'), max_length=255, choices=ROLE_CHOICES, default='user')

    groups = None
    user_permissions = None

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"


class FoodMeny(models.Model):
    name = models.CharField(_('Ovqat nomi'), max_length=255)
    description = models.TextField(_("Ovqat haqida"), blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Food"
        verbose_name_plural = "Foods"


class Order(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='orders')
    created_at = models.DateTimeField(auto_now_add=True)
    distance_to_customer = models.FloatField()

    def calculate_estimated_time(self):
        """
        Yetkazib berish vaqtini hisoblash: har 5 minutda 4 ta taom + har km uchun 3 minut.
        """

        total_foods = sum(item.quantity for item in self.items.all())  # barcha ovqatlar soni
        preparation_time = (total_foods // 4) * 5  # barcha ovqatlar uchun ketadigan vaqt
        delivery_time = self.distance_to_customer * 3  # yolda sarflanadigan vaqt
        return preparation_time + delivery_time  # mijozga yetib boradigan vaqt

    def total_foods(self):
        return sum(item.quantity for item in self.items.all())

    def delivery_time(self):
        return self.calculate_estimated_time()

    def __str__(self):
        return f"Order {self.id} - {self.user.username}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    food = models.ForeignKey(FoodMeny, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.quantity} x {self.food.name}"
