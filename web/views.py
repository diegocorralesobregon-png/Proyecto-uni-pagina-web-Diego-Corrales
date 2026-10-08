from django.shortcuts import render

def home(request):
    """Vista de página de inicio"""
    context = {
        'titulo': '¡Bienvenido a tu sitio web!',
        'mensaje': 'Esta es tu primera página creada con Django y Docker',
    }
    return render(request, 'home.html', context)

def plantilla1(request):
    """Vista de plantilla 1"""
    context = {
        'titulo': 'Plantilla 1',
        'descripcion': 'Primera página de ejemplo',
        'contenido': 'Aquí puedes agregar tu contenido...',
    }
    return render(request, 'plantilla1.html', context)

def plantilla2(request):
    """Vista de plantilla 2"""
    context = {
        'titulo': 'Plantilla 2',
        'descripcion': 'Segunda página de ejemplo',
        'contenido': 'Aquí puedes agregar tu contenido...',
    }
    return render(request, 'plantilla2.html', context)

def plantilla3(request):
    """Vista de plantilla 3"""
    context = {
        'titulo': 'Plantilla 3',
        'descripcion': 'Tercera página de ejemplo',
        'contenido': 'Aquí puedes agregar tu contenido...',
    }
    return render(request, 'plantilla3.html', context)

def plantilla4(request):
    """Vista de plantilla 4"""
    context = {
        'titulo': 'Plantilla 4',
        'descripcion': 'Cuarta página de ejemplo',
        'contenido': 'Aquí puedes agregar tu contenido...',
    }
    return render(request, 'plantilla4.html', context)