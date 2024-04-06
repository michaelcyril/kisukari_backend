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



class GlucoseView(APIView):
    @staticmethod
    def post(request):
        try:
            data = request.data
            serialized = GlucosePostSerializer(data=data)
            isvalid = serialized.is_valid()
            if isvalid:
                serialized.save()
                return Response({"save": True})
            return Response({"save": False, "errors": serialized.errors})
        except:
            return Response({"save": False})


    @staticmethod
    def get(request):
        userId = request.GET.get("userId")
        try:
            user = User.objects.get(id=userId)
            glucose = Glucose.objects.filter(user=user)
            serialized = GlucoseGetSerializer(instance=glucose, many=True)
            return Response(serialized.data)
        except:
            return Response([])



# {
#   "user": "75c03b21-a226-477b-9f98-02e01975b57c",
#   "value": 100,
#   "label": [
#     {"name": "Normal"},
#     {"name": "Postprandial"},
#     {"name": "Fasting"}
#   ],
#   "note": "This is a test note.",
#   "time": "2024-04-01T08:00:00"
# }

class DeleteUpdateGlucose(APIView):
    @staticmethod
    def post(request):
        # try:
        #     data = request.data
        #     glucose = Glucose.objects.get(id=data['id'])
        #     serialized = GlucosePostSerializer(glucose, data=request.data)
        #     isvalid = serialized.is_valid()
        #     if isvalid:
        #         return Response({"update": True})
        #     return Response({"update": False, "errors": serialized.errors})
        # except:
        #     return Response({"update": False})
        pass

    @staticmethod
    def get(request):
        try:
            glucoseId = request.GET.get("glucoseId")
            glucose = Glucose.objects.get(id=glucoseId)
            glucose.delete()
            return Response({"delete": True})
        except:
            return Response({"delete": False})



# {
#     "id": "ef80f19b-072b-4f8e-9ac8-bafb023fa377",
#     "user": "75c03b21-a226-477b-9f98-02e01975b57c",
#     "value": 100,
#     "label": [
#         {
#             "name": "Good"
#         },
#         {
#             "name": "Fasting"
#         }
#     ],
#     "note": "This is a test note.",
#     "time": "2024-04-01T08:00:00+03:00"
# }



class MedicineView(APIView):
    @staticmethod
    def post(request):
        try:
            data = request.data
            serialized = MedicinePostSerializer(data=data)
            isvalid = serialized.is_valid()
            if isvalid:
                serialized.save()
                return Response({"save": True})
            return Response({"save": False, "errors": serialized.errors})
        except:
            return Response({"save": False})

    @staticmethod
    def get(request):
        userId = request.GET.get("userId")
        try:
            user = User.objects.get(id=userId)
            medicine = Medicine.objects.filter(user=user)
            serialized = MedicineGetSerializer(instance=glucose, many=True)
            return Response(serialized.data)
        except:
            return Response([])



class DeleteUpdateMedicine(APIView):
    @staticmethod
    def post(request):
        pass

    @staticmethod
    def get(request):
        try:
            medicineId = request.GET.get("medicineId")
            medicine = Medicine.objects.get(id=medicineId)
            medicine.delete()
            return Response({"delete": True})
        except:
            return Response({"delete": False})



class InsulinView(APIView):
    @staticmethod
    def post(request):
        try:
            data = request.data
            serialized = InsulinePostSerializer(data=data)
            isvalid = serialized.is_valid()
            if isvalid:
                serialized.save()
                return Response({"save": True})
            return Response({"save": False, "errors": serialized.errors})
        except:
            return Response({"save": False})

    @staticmethod
    def get(request):
        userId = request.GET.get("userId")
        try:
            user = User.objects.get(id=userId)
            insulin = Insulin.objects.filter(user=user)
            serialized = InsulineGetSerializer(instance=insulin, many=True)
            return Response(serialized.data)
        except:
            return Response([])



class DeleteUpdateInsulin(APIView):
    @staticmethod
    def post(request):
        pass

    @staticmethod
    def get(request):
        try:
            insulinId = request.GET.get("insulinId")
            insulin = Insulin.objects.get(id=insulinId)
            insulin.delete()
            return Response({"delete": True})
        except:
            return Response({"delete": False})



class PressureView(APIView):
    @staticmethod
    def post(request):
        try:
            data = request.data
            serialized = PressurePostSerializer(data=data)
            isvalid = serialized.is_valid()
            if isvalid:
                serialized.save()
                return Response({"save": True})
            return Response({"save": False, "errors": serialized.errors})
        except:
            return Response({"save": False})

    @staticmethod
    def get(request):
        userId = request.GET.get("userId")
        try:
            user = User.objects.get(id=userId)
            pressure = Pressure.objects.filter(user=user)
            serialized = PressureGetSerializer(instance=pressure, many=True)
            return Response(serialized.data)
        except:
            return Response([])



class DeleteUpdatePressure(APIView):
    @staticmethod
    def post(request):
        pass

    @staticmethod
    def get(request):
        try:
            pressureId = request.GET.get("pressureId")
            pressure = Pressure.objects.get(id=pressureId)
            pressure.delete()
            return Response({"delete": True})
        except:
            return Response({"delete": False})


