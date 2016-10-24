from django.shortcuts import render

# Create your views here.
def dashboard(request):
    title_from_view = "Dashboard"
    return render(request, 'PP_Dashboard/dashboard.html', {"title_from_view": title_from_view})

