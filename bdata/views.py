from django.shortcuts import render
from django.http import HttpResponse
from bdata.models import Route, Bus, BPoint
import requests
import folium
# Create your views here.

def find(request):
    if request.method=="POST":
        route = request.POST.get("route")
        bpoint_selected = request.POST.get("bpoint")
        buses = Bus.objects.filter(route=route)
                
        context = {
            "routes" : Route.objects.all(),
            "buses" : buses,
            "bpoint_selected" : BPoint.objects.get(id=bpoint_selected)
        }
        return render(request, 'bdata/search.html', context=context)
    context = {
        "routes" : Route.objects.all(),
        "buses" : Bus.objects.all(),
        "bpoints" : BPoint.objects.all()
    }
    return render(request, 'bdata/find.html', context=context)

def home(request):
    context = {
        "routes" : Route.objects.all(),
        "buses" : Bus.objects.all()
    }
    return render(request, 'bdata/home.html', context=context)

# def bus(request, bus_id, bpoint):
#     bus = Bus.objects.get(id=bus_id)
#     bus_lat = bus.busloc.lat
#     bus_long = bus.busloc.long
#     print(bus_lat,bus_long)
#     bpoint_selected = BPoint.objects.get(id=bpoint)
#     bpoint_lat = bpoint_selected.lat
#     bpoint_long = bpoint_selected.long
#     key = "Ajb5cBYG4DdffO9dIl4wRR3RVQSEhOQ4zOXIGWxURNl24Ro6E9qOgcwGBHwsuW6v"
#     dist_mat = requests.get(f"https://dev.virtualearth.net/REST/v1/Routes/DistanceMatrix?origins={bus_lat},{bus_long}&destinations={bpoint_lat},{bpoint_long}&travelMode=driving&key={key}")
#     response = dist_mat.json()
#     travelDuration = round(float(response["resourceSets"][0]["resources"][0]["results"][0]["travelDuration"]),1)
#     travelDistance = int(response["resourceSets"][0]["resources"][0]["results"][0]["travelDistance"])

#     context = {
#         "response" : {"travelDuration":travelDuration, "travelDistance":travelDistance},
#         "buses" : Bus.objects.filter(id=bus_id),
#         "bpoint" : {"bp": bpoint_selected} 
#     }
#     return render(request, 'bdata/bus.html', context=context)

def login(request):
    return render(request,'bdata/login.html')

def loc(request):
    if request.method == "POST":
        bus_lat = request.POST.get("lat")
        bus_long = request.POST.get("long")

    return render(request, 'bdata/loc.html')


def ot(request):
    return render(request,"bdata/ourteam.html")


def bus(request, bus_id, bpoint):
    bus = Bus.objects.get(id=bus_id)
    bus_lat = bus.busloc.lat
    bus_long = bus.busloc.long
    name1=Bus.objects.get(id=bus_id)
    # print(bus_lat,bus_long)
    bpoint_selected = BPoint.objects.get(id=bpoint)
    bpoint_lat = bpoint_selected.lat
    bpoint_long = bpoint_selected.long
    # name2= BPoint.objects.get(id=bpoint)
    tooltip='Click Me!'
    map=folium.Map(location=[bus_lat,bus_long],zoom_start=12)
    folium.Marker([bus_lat,bus_long],
              popup = name1,tooltip=tooltip).add_to(map)
    
    map = map._repr_html_()
    context={'map':map}
    return render(request,'bdata/map.html',context=context)

