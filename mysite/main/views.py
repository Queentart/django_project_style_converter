from django.shortcuts import render, redirect


# Create your views here.

def index(request):
    Board = Board.objects.order_by('name')
    
    