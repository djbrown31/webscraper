from django.shortcuts import render, get_object_or_404
from .models import Landmark

def landmark_list(request):
    landmarks = Landmark.objects.all()
    return render(request, 'map/landmark_list.html', {'landmarks': landmarks})

def landmark_detail(request, landmark_id):
    landmark = get_object_or_404(Landmark, id=landmark_id)
    return render(request, 'map/landmark_detail.html', {'landmark': landmark, 'address': generate_google_address(landmark.address)})


def generate_google_address(address):
    modified_address = address.replace(' ', '%20')
    return f"https://www.google.com/maps/embed/v1/place?q={modified_address}&key=AIzaSyCMgH8cUUYkgteoRzgNPFlv4L1_Gkhk_6U"
