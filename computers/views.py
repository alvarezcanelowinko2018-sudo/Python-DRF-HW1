from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Computer

class ComputerListView(ListView):
    model = Computer
    template_name = 'computers/computer_list.html'

class ComputerDetailView(DetailView):
    model = Computer
    template_name = 'computers/computer_detail.html'

class ComputerCreateView(CreateView):
    model = Computer
    template_name = 'computers/computer_form.html'
    fields = '__all__'
    success_url = reverse_lazy('computer_list')

class ComputerUpdateView(UpdateView):
    model = Computer
    template_name = 'computers/computer_form.html'
    fields = '__all__'
    success_url = reverse_lazy('computer_list')

class ComputerDeleteView(DeleteView):
    model = Computer
    template_name = 'computers/computer_confirm_delete.html'
    success_url = reverse_lazy('computer_list')