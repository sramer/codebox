from django.shortcuts import render
from rest_framework import generics
from .models import Snippet
from .serializers import SnippetSerializer
from .forms import CodeForm

class SnippetList(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer



class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer


def form_data(request):
    if request.method == "POST":
        form = CodeForm(request.POST)
        if form.is_valid():
            form.save()