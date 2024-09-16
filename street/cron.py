from .models import Home
from media.scripts import users_data


def update_item_data():
    items = Home.objects.all()
    
    for item in items:
        street = item.street_for
        home = item.home
        script = users_data(street, home)

        item.file = script[0]        
        item.active = script[1]        
        item.deactive = script[2]        

        item.save()
        
        print(f'{street} {home}')