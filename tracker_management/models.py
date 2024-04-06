from django.db import models
from user_management.models import User
import uuid


class GlucoseLabel(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        db_table = 'glucose_label'


class Glucose(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # image = models.ImageField()
    value = models.IntegerField(null=True, blank=True)
    label = models.ManyToManyField(GlucoseLabel,blank=True)
    note = models.TextField()
    time = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.value}'

    class Meta:
        db_table = 'glucose_tracker'


class MedicineLabel(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        db_table = 'medicine_label'



class Medicine(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # image = models.ImageField()
    pills = models.IntegerField(null=True, blank=True)
    description = models.TextField()
    note = models.TextField()
    label = models.ManyToManyField(MedicineLabel,blank=True)
    time = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.pills}'

    class Meta:
        db_table = 'medicine_tracker'


class InsulineLabel(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        db_table = 'insuline_label'



class Insulin(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # image = models.ImageField()
    value = models.IntegerField(null=True, blank=True)
    type = models.CharField(max_length=255, unique=True)
    label = models.ManyToManyField(InsulineLabel,blank=True)
    note = models.TextField()
    time = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.value}'

    class Meta:
        db_table = 'insulin_tracker'


class PressureLabel(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        db_table = 'pressure_label'



class Pressure(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # image = models.ImageField()
    bp = models.IntegerField(null=True, blank=True)
    pressure = models.IntegerField(null=True, blank=True)
    label = models.ManyToManyField(PressureLabel,blank=True)
    note = models.TextField()
    time = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.bp}'

    class Meta:
        db_table = 'pressure_tracker'



class Clinic(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # image = models.ImageField()
    hospital = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    checkups = models.TextField()
    result = models.TextField()
    date = models.DateField()
    next_clinic_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.id}'

    class Meta:
        db_table = 'clinic_tracker'


class ClinicMedicine(models.Model):
    clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    # image = models.ImageField()

    def __str__(self):
        return f'{self.name}'

    class Meta:
        db_table = 'clinic_medine'



class Meal(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # image = models.ImageField()
    unit_description = models.CharField(max_length=255, unique=True)
    unit = models.IntegerField()
    weight = models.IntegerField()
    calories = models.DecimalField(max_digits=10, decimal_places=0)
    meal_type = models.CharField(max_length=255, unique=True)
    time = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.id}'

    class Meta:
        db_table = 'meal_tracker'



class Exercise(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=255)
    amount_time = models.IntegerField()
    calories_per_time = models.DecimalField(max_digits=10, decimal_places=0)
    burned_calories = models.DecimalField(max_digits=10, decimal_places=0)
    note = models.TextField()
    time = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.id}'

    class Meta:
        db_table = 'excercise_tracker'


class Step(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    number_of_steps = models.IntegerField()
    time = models.DateTimeField()
    burned_calories = models.DecimalField(max_digits=10, decimal_places=0)

    def __str__(self):
        return f'{self.id}'

    class Meta:
        db_table = 'step_tracker'


class Water(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    litre = models.IntegerField()
    time = models.DateTimeField()

    def __str__(self):
        return f'{self.id}'

    class Meta:
        db_table = 'water_tracker'


