#from django.shortcuts import render
from django.http import HttpResponse  
from datetime import date
from django.template import Template,Context
from django.template.loader import get_template
from django.shortcuts import render
def hello(request):
    return HttpResponse("Hello, world!")

def bye(request):
    return HttpResponse("Goodbye, world!")

def edad(request,anios,futuro):

    incremento = futuro - date.today().year
    cumplira = anios + incremento
    mensaje = "En el año %d cumpliras %d años" % (futuro,cumplira)

    return HttpResponse(mensaje)

def primer_plantilla(request):

   plantilla = """
   <html>
       <body>
           <h1>Hola {{nombre}}!Esta es mi primera plantilla en archivo</h1>
       </body>
   </html>
    """ 
   tpl = Template(plantilla)
   ctx = Context({
         "nombre":"Juan"
   })
    
   mensaje = tpl.render(ctx)

   return HttpResponse(mensaje)

def segunda_plantilla(request):

    tpl = get_template('segunda_plantilla.html')
    mensaje = tpl.render({
        "nombre":"Pedro",
        "fecha_actual":date.today()
    })
    return HttpResponse(mensaje)

def tercer_plantilla(request):

   return render(request,'tercer_plantilla.html',{
       "nombre":"Julio Martinez",
       "fecha_actual":date.today()
   })