from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .forms import ReservationForm

# Create your views here.


def hello_func(response):
      return HttpResponse("Hello from func")

#classbased 
class heloClass(View):
      def get(self, response):
            return HttpResponse("Hello from class")

def home(request):
      form = ReservationForm

      if request.method == 'POST':
            form = ReservationForm(request.POST)
            if form.is_valid():
                  form.save()
                  return HttpResponse("Successful submission!")
            
      
      return render(request, 'index.html', {'form' : form })