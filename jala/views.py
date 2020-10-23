from django.http import HttpResponse
from django.template import Template, Context
import datetime
from django.template import loader

class Persona (object):
    def __init__(self, nombre,edad):
        self.nombre=nombre
        self.edad=edad
#esta es la version 2 

def saludo(request):
    p1= Persona("ALEJANDRO", 18)
    fecha = datetime.datetime.now()
    
    temasDelCurso= ["Formularios","Aprendiendo", "python"]
    #docExterno= open("C:/Users/Alejandro Pizano/Desktop/cmder/jala/jala/plantilla/miplantilla.html")
    #plt = Template(docExterno.read())
    #docExterno.close()
    doc_externo = loader.get_template('miplantilla.html')
    #ctx= Context({"nombre_persona":p1.nombre,"Hora":fecha, "edad":p1.edad, "temas":temasDelCurso})

    documento =doc_externo.render({"nombre_persona":p1.nombre,"Hora":fecha, "edad":p1.edad, "temas":temasDelCurso})

    return HttpResponse(documento)

def closing(request):
    return HttpResponse("Bye, I'm out!!!!")


def dameFecha(request):
    fecha = datetime.datetime.now()
    cortecia= ("La fecha y hora actual es %s" %fecha)
 
    return HttpResponse(cortecia)

def edad(request, anio):
    edadActual= 21
    periodo=anio-2020
    edadFutura= edadActual+periodo
    if(edadFutura<100):
        documento="En el año %s tendras %s años"%(anio, edadFutura)
    else:
        documento= "Ya vas a estar muerto papi"
    return HttpResponse(documento)

def conoci (request):

    return HttpResponse("he declarado que ya aprendiste un 1% mas!")
