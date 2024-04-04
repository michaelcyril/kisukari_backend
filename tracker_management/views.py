from django.shortcuts import render
from .models import *
from .serializer import *
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from user_management.models import User

# Create your views here.

class WaterView(APIView):
    @staticmethod
    def post(request):
        data = request.data
        try:
            serialized = WaterPostSerializer(data=data)
            isvalid = serialized.is_valid()
            if isvalid:
                serialized.save()
                return Response({"save": True})
            return Response({"save": False, "errors": serialized.errors})
        except:
            return Response({"save": False, "errors": "Error Occured"})

    @staticmethod
    def get(request, userId):
        try:
            user = User.objects.get(id=userId)
            water = Water.objects.filter(user=user)
            serialized = WaterGetSerializer(instance=water, many=True)
            return Response(serialized.data)
        except User.DoesNotExist:
            return Response([])


class DeleteUpdateWater(APIView):
    @staticmethod
    def post(request):
        try:
            data = request.data
            water = Water.objects.get(id=data['id'])
            water.litre = data['litre']
            water.time = data['time']
            water.save()
            return Response({"update": True})
        except:
            return Response({"update": False, "error": "Water Does Not Exists"})


    @staticmethod
    def get(request, waterId):
        try:
            water = Water.objects.get(id=waterId)
            water.delete()
            return Response({"delete": True})
        except Water.DoesNotExist:
            return Response({"delete": False, "error": "Water Does Not Exists"})


class StepView(APIView):
    @staticmethod
    def post(request):
        try:
            data = request.data
            serialized = StepPostSerializer(data=data)
            isvalid = serialized.is_valid()
            if isvalid:
                serialized.save()
                return Response({"save": True})
            return Response({"save": False, "errors": serialized.errors})
        except:
            return Response({"save": False, "errors": "Error Occured"})

    @staticmethod
    def get(request, userId):
        try:
            user = User.objects.get(id=userId)
            step = Step.objects.filter(user=user)
            serialized = StepGetSerializer(instance=step, many=True)
            return Response(serialized.data)
        except User.DoesNotExist:
            return Response([])


class DeleteUpdateStep(APIView):
    @staticmethod
    def post(request):
        data = request.data
        try:
            step = Step.objects.get(id=data['id'])
            step.number_of_steps = data['number_of_steps']
            step.time = data['time']
            step.burned_calories = data['burned_calories']
            step.save()
            return Response({"update": True})
        except:
            return Response({"upsate": False, "errors": "Error Occured"})

    @staticmethod
    def get(request, stepId):
        try:
            step = Step.objects.get(id=stepId)
            step.delete()
            return Response({"delete": True})
        except:
            return Response({"delete": False, "errors": "Error Occured"})


class ExerciseView(APIView):
    @staticmethod
    def post(request):
        try:
            data = request.data
            serialized = ExercisePostSerializer(data=data)
            isvalid = serialized.is_valid()
            if isvalid:
                serialized.save()
                return Response({"save": True})
            return Response({"save": False, "errors": serialized.errors})
        except:
            return Response({"save": False, "errors": "Error Occured"})

    @staticmethod
    def get(request, userId):
        try:
            user = User.objects.get(id=userId)
            exercise = Exercise.objects.filter(user=user)
            serialized = ExerciseGetSerializer(instance=exercise, many=True)
            return Response(serialized.data)
        except User.DoesNotExist:
            return Response([])


class DeleteUpdateExercise(APIView):
    @staticmethod
    def post(request):
        data = request.data
        try:
            exercise = Exercise.objects.get(id=data['id'])
            exercise.type = data['type']
            exercise.amount_time = data['amount_time']
            exercise.calories_per_time = data['calories_per_time']
            exercise.burned_calories = data['burned_calories']
            exercise.note = data['note']
            exercise.time = data['time']
            exercise.save()
            return Response({"update": True})
        except:
            return Response({"upsate": False, "errors": "Error Occured"})

    @staticmethod
    def get(request, exerciseId):
        try:
            exercise = Exercise.objects.get(id=exerciseId)
            exercise.delete()
            return Response({"delete": True})
        except:
            return Response({"delete": False, "errors": "Error Occured"})


class MealView(APIView):
    @staticmethod
    def post(request):
        try:
            data = request.data
            serialized = MealPostSerializer(data=data)
            isvalid = serialized.is_valid()
            if isvalid:
                serialized.save()
                return Response({"save": True})
            return Response({"save": False, "errors": serialized.errors})
        except:
            return Response({"save": False, "errors": "Error Occured"})

    @staticmethod
    def get(request, userId):
        try:
            user = User.objects.get(id=userId)
            meal = Meal.objects.filter(user=user)
            serialized = MealGetSerializer(instance=meal, many=True)
            return Response(serialized.data)
        except User.DoesNotExist:
            return Response([])


class DeleteUpdateMeal(APIView):
    @staticmethod
    def post(request):
        data = request.data
        try:
            meal = Meal.objects.get(id=data['id'])
            meal.unit_description = data['unit_description']
            meal.unit = data['unit']
            meal.weight = data['weight']
            meal.calories = data['calories']
            meal.meal_type = data['meal_type']
            meal.time = data['time']
            meal.save()
            return Response({"update": True})
        except:
            return Response({"upsate": False, "errors": "Error Occured"})

    @staticmethod
    def get(request, mealId):
        try:
            meal = Meal.objects.get(id=mealId)
            meal.delete()
            return Response({"delete": True})
        except:
            return Response({"delete": False, "errors": "Error Occured"})


class ClinicView(APIView):
    @staticmethod
    def post(request):
        try:
            data = request.data
            clinic_data = {
                "user": data['user'],
                "hospital": data['hospital'],
                "description": data['description'],
                "checkups": data['checkups'],
                "result": data['result'],
                "date": data['date'],
                "next_clinic_date": data['next_clinic_date']
            }
            serialized = ClinicPostSerializer(data=clinic_data)
            isvalid = serialized.is_valid()
            if isvalid:
                clinic = serialized.save()
                for medicine in data['medicines']:
                    serialized2 = ClinicMedicinePostSerializer(data=medicine)
                    if serialized2.is_valid():
                        serialized2.save()
                    #some
                return Response({"save": True})
            return Response({"save": False})
        except:
            return Response({"save": False})

    @staticmethod
    def get(request, userId):
        try:
            user = User.objects.get(id=userId)
            clinic = Clinic.objects.filter(user=user)
            serialized = ClinicGetSerializer(instance=clinic, many=True)
            return Response(serialized.data)
        except User.DoesNotExist:
            return Response([])


class DeleteUpdateClinic(APIView):
    @staticmethod
    def post(request):
        data = request.data
        try:
            clinic = Clinic.objects.get(id=data['id'])
            clinic.hospital = data['hospital']
            clinic.description = data['description']
            clinic.checkups = data['checkups']
            clinic.result = data['result']
            clinic.date = data['date']
            clinic.next_clinic_date = data['next_clinic_date']
            clinic.save()
            return Response({"update": True})
        except:
            return Response({"upsate": False, "errors": "Error Occured"})

    @staticmethod
    def get(request, clinicId):
        try:
            clinic = Clinic.objects.get(id=clinicId)
            clinic.delete()
            return Response({"delete": True})
        except:
            return Response({"delete": False, "errors": "Error Occured"})

