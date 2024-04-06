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


class GlucoseLabelSerializer(serializers.ModelSerializer):
    class Meta:
        model = GlucoseLabel
        fields = '__all__'

class GlucosePostSerializer(serializers.ModelSerializer):
    label = GlucoseLabelSerializer(many=True, required=False)

    class Meta:
        model = Glucose
        fields = [
            'id',
            'user',
            'value',
            'label',
            'note',
            'time',
            'created_at'
        ]

    def create(self, validated_data):
        label_data = validated_data.pop('label', None)
        glucose = Glucose.objects.create(**validated_data)
        if label_data:
            for label_item in label_data:
                label, _ = GlucoseLabel.objects.get_or_create(**label_item)
                glucose.label.add(label)
        return glucose

    # def update(self, instance, validated_data):
    #     label_data = validated_data.pop('label', None)
    #     instance.label.clear()
    #     print("HERE")
    #     print(validated_data['value'])
    #     # glucose = super().update(instance, validated_data)
    #     if label_data:
    #         # glucose.label.clear()  # Remove existing labels
    #         for label_item in label_data:
    #             label, _ = GlucoseLabel.objects.get_or_create(**label_item)
    #             glucose.label.add(label)
    #
    #     return glucose


class GlucoseGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Glucose
        fields = [
            'id',
            'value',
            'label',
            'note',
            'time',
            'created_at'
        ]
        depth = 2


class MedicineLabelSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicineLabel
        fields = '__all__'

class MedicinePostSerializer(serializers.ModelSerializer):
    label = MedicineLabelSerializer(many=True, required=False)

    class Meta:
        model = Medicine
        fields = [
            'id',
            'user',
            'pills',
            'description',
            'note',
            'label',
            'time',
            'created_at'
        ]

    def create(self, validated_data):
        label_data = validated_data.pop('label', None)
        medicine = Medicine.objects.create(**validated_data)
        if label_data:
            for label_item in label_data:
                label, _ = MedicineLabel.objects.get_or_create(**label_item)
                medicine.label.add(label)
        return medicine


class MedicineGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicine
        fields = [
            'id',
            'user',
            'pills',
            'description',
            'note',
            'label',
            'time',
            'created_at'
        ]
        depth = 2


class InsulineLabelSerializer(serializers.ModelSerializer):
    class Meta:
        model = InsulineLabel
        fields = '__all__'

class InsulinePostSerializer(serializers.ModelSerializer):
    label = InsulineLabelSerializer(many=True, required=False)

    class Meta:
        model = Insulin
        fields = [
            'id',
            'user',
            'value',
            'type',
            'label',
            'note',
            'time',
            'created_at'
        ]

    def create(self, validated_data):
        label_data = validated_data.pop('label', None)
        insuline = Insulin.objects.create(**validated_data)
        if label_data:
            for label_item in label_data:
                label, _ = InsulineLabel.objects.get_or_create(**label_item)
                insuline.label.add(label)
        return insuline


class InsulineGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Insulin
        fields = [
            'id',
            'user',
            'value',
            'type',
            'label',
            'note',
            'time',
            'created_at'
        ]
        depth = 2


class PressureLabelSerializer(serializers.ModelSerializer):
    class Meta:
        model = PressureLabel
        fields = '__all__'

class PressurePostSerializer(serializers.ModelSerializer):
    label = PressureLabelSerializer(many=True, required=False)

    class Meta:
        model = Pressure
        fields = [
            'id',
            'user',
            'bp',
            'pressure',
            'label',
            'note',
            'time',
            'created_at'
        ]

    def create(self, validated_data):
        label_data = validated_data.pop('label', None)
        pressure = Pressure.objects.create(**validated_data)
        if label_data:
            for label_item in label_data:
                label, _ = PressureLabel.objects.get_or_create(**label_item)
                pressure.label.add(label)
        return pressure


class PressureGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pressure
        fields = [
            'id',
            'user',
            'bp',
            'pressure',
            'label',
            'note',
            'time',
            'created_at'
        ]
        depth = 2




