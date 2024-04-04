from rest_framework import serializers
from .models import *


class WaterPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Water
        fields = [
            'user',
            'litre',
            'time'
        ]

class WaterGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Water
        fields = "__all__"
        depth = 1


class StepPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Step
        fields = [
            'user',
            'number_of_steps',
            'time',
            'burned_calories'
        ]


class StepGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Step
        fields = "__all__"
        depth = 1


class ExercisePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = [
            'user',
            'type',
            'amount_time',
            'calories_per_time',
            'burned_calories',
            'note',
            'time'
        ]


class ExerciseGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = "__all__"
        depth = 1


class MealPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meal
        fields = [
            'user',
            'unit_description',
            'unit',
            'weight',
            'calories',
            'meal_type',
            'time'
        ]


class MealGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meal
        fields = "__all__"
        depth = 1


class ClinicMedicinePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClinicMedicine
        fields = [
            'clinic',
            'name',
        ]


class ClinicPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clinic
        fields = [
            'user',
            ' hospital',
            'description',
            'checkups',
            'result',
            'date',
            'next_clinic_date'
        ]


class ClinicGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clinic
        fields = "__all__"
        depth = 1


