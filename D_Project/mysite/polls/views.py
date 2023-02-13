from django.shortcuts import get_object_or_404, render
from .models import Choice, Question
from django.template import loader
from django.http import Http404
# Create your views here.
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.utils import timezone
from polls.models import Question, Choice
from polls.serializers import QuestionSerializer, ChoiceSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
class IndexView(generics.ListCreateAPIView):
    queryset = Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]
    serializer_class = QuestionSerializer

class DetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.filter(pub_date__lte=timezone.now())
    serializer_class = QuestionSerializer
    
class ResultsView(generics.ListCreateAPIView):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer

def vote(request, question_id, choice_id):
    selected_choice = Choice.objects.get(pk=choice_id)
    selected_choice.votes += 1
    selected_choice.save()
    