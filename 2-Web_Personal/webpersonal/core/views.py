from django.shortcuts import render, HttpResponse

html_base = """
    <!-- Titulo -->
    <h1>
        Mi web personal
    </h1>
    <!-- Menú -->
    <nav>
        <ul>
            <li> <a href="/">Home</a> </li>
            <li> <a href="/portfolio/">Portafolio</a> </li>
            <li> <a href="/contact/">Contacto</a> </li>
            <li> <a href="/about-me/">About Me</a> </li>
        </ul>
    </nav>
"""

# Create your views here.
def home(request):
    return HttpResponse(html_base + "<h2>Portada</h2>")

def portfolio(request):
    return HttpResponse(html_base + "<h2>Portafolio</h2>")

def contact(request):
    return HttpResponse(html_base + "<h2>Contacto</h2>")

def aboutMe(request):
    return HttpResponse(html_base + "<h2>About Me</h2>")