from django.shortcuts import render
from form.models import Feedback

# Create your views here.
def feedback(request):
    return render(request,'feedback.html')
def submit_feedback(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        details = request.POST['feedback']
        feedb = Feedback(customer_name=name,email=email,details=details)
        feedb.save()
    res = render(request,'thanks.html')
    return res
def about(request):
    return render(request,'about.html')


