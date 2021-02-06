'''Permite "inyectar" contenido adicional a las templates'''
from django.urls import reverse

def menu(request):
    menu = {'menu': [
        {'name': 'Home', 'url': reverse('worker_list')},
        {'name': 'New Worker', 'url': reverse('worker_new')},
    ]}
    for item in menu['menu']:
        if request.path == item['url']:
            item['active'] = True
    return menu 