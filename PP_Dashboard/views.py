from django.shortcuts import render
from PP_Dashboard.models import Profile
# Create your views here.
def dashboard(request):
    title_from_view = "Dashboard"
    person = Profile.objects.get(number_of_picks=1)
    return render(request, 'PP_Dashboard/dashboard.html', {"title_from_view": title_from_view, "person":person})

