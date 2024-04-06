from django.urls import path
from .views import *
app_name = 'tracker_management'

urlpatterns = [
    path('insert-get-glucose', GlucoseView.as_view()),
    path('delete-update-glucose', DeleteUpdateGlucose.as_view()),

    path('insert-get-insulin', InsulinView.as_view()),
    path('delete-update-insulin', DeleteUpdateInsulin.as_view()),

    path('insert-get-medicine', MedicineView.as_view()),
    path('delete-update-medicine', DeleteUpdateMedicine.as_view()),

    path('insert-get-pressure', PressureView.as_view()),
    path('delete-update-pressure', DeleteUpdatePressure.as_view()),

    path('insert-get-water', WaterView.as_view()),
    path('delete-update-water', DeleteUpdateWater.as_view()),

    path('insert-get-step', StepView.as_view()),
    path('delete-update-step', DeleteUpdateStep.as_view()),

    path('insert-get-exercise', ExerciseView.as_view()),
    path('delete-update-exercise', DeleteUpdateExercise.as_view()),

    path('insert-get-meal', MealView.as_view()),
    path('delete-update-meal', DeleteUpdateMeal.as_view()),

    path('insert-get-clinic', ClinicView.as_view()),
    path('delete-update-clinic', DeleteUpdateClinic.as_view()),
]
