from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from .models import Book
from .forms import BookForm


class BookCreate(CreateView):
    model = Book
    form_class = BookForm
    template_name = 'create.html'
    success_url = reverse_lazy('read')

class BookList(ListView):
    model = Book
    template_name = 'read.html'
    ordering = ['-created_at']


class BookUpdate(UpdateView):
    model = Book
    form_class = BookForm
    template_name = 'create.html'
    success_url = reverse_lazy('read')

class BookDelete(DeleteView):
    model = Book
    template_name = 'delete.html'
    success_url = reverse_lazy('read')

class BookDetail(DetailView):
    model = Book
    template_name = 'detail.html'