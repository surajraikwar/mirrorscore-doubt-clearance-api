from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Question
from .forms import QuestionForm
#from rest_framework import generics
from rest_framework import viewsets
from .serializers import QuestionSerializer


def index(request):
    context = {}
    if request.POST:
        form = QuestionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your doubt has been sent.')
            return redirect('doubts:index')

        else:
            context['question_form'] = form

    else:
        form = QuestionForm()
        context['question_form'] = form

    return render(request, 'doubts/index.html', context)

class ListQuestionsView(viewsets.ModelViewSet):#(generics.ListAPIView):

    queryset = Question.objects.all().order_by('-id')
    serializer_class = QuestionSerializer
