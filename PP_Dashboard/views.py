from django.shortcuts import render
from PP_Dashboard.models import Profile
# Create your views here.
def dashboard(request):
    title_from_view = "Dashboard"
    person = Profile() # Empty profile for now, getting current user will be done later
    return render(request, 'PP_Dashboard/dashboard.html', {"title_from_view": title_from_view, "person":person})
