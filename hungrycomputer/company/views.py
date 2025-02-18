from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse
from matplotlib.style import context
from company.models import Assembly_order, Employee, Problem, Product


def index(request):
    # return HttpResponse("Hello, world. DUDE .")
    registro = Problem.objects.get(id=1)
    print(registro)
    context = {"registro": registro}
    return render(request, "index.html", context)


def simple_form(request):
    if request.method == "POST":
        description = request.POST.get("description")
        inputO = request.POST.get("inputO")
        print(description, inputO)

    return render(request, "simple_form.html")


def delete_simple_form_id(request, id):
    if request.method == "POST":
        print(f"example of deleting some id: {id}")
    return redirect(simple_form)


# ALMACEN
def almacen_view(request):
    context = {"products": Product.objects.all()}
    print(context)
    return render(request, "almacen.html", context)

def add_product(request):
    if request.method == "POST":
        name = request.POST.get("NombreProd")
        price = request.POST.get("PrecioProd")
        stock = request.POST.get("StockProd")
        description = request.POST.get("exampleInputNota")
        serial_num = request.POST.get("IdProd")
        model = request.POST.get("ModeloProd")
        brand = request.POST.get("MarcaProd")
        print(name, price, stock)
        product = Product(
            name=name,
            price=price,
            stock=stock,
            description=description,
            serial_num=serial_num,
            brand=brand,
            model=model,
        )
        product.save()
    return redirect(almacen_view)


def update_product(request):
    if request.method == "POST":
        p_id = request.POST.get("IdProd")
        name = request.POST.get("NombreProd")
        price = request.POST.get("PrecioProd")
        stock = request.POST.get("StockProd")
        description = request.POST.get("exampleInputNota")
        serial_num = request.POST.get("IdProd")
        brand = request.POST.get("MarcaProd")
        model = request.POST.get("ModeloProd")
        print(name, price, stock)

        try:
            product = Product.objects.get(id=p_id)
            product.name = name
            product.price = price
            product.stock = stock
            product.description = description
            product.serial_num = serial_num
            product.brand = brand
            product.model = model
            product.save()
        except Product.DoesNotExist:
            print("El producto no existe")
    return redirect(almacen_view)


def delete_product(request, id):
    if request.method == "POST":
        product = Product.objects.get(id=id)
        product.delete()
    return redirect(almacen_view)


#Soporte Formulario
def soporte_form(request):
    print(Problem.objects.all())
    if request.method == "POST":
        id = request.POST.get("id")
        problema = request.POST.get("problema")
        descripcion = request.POST.get("descripcion")
        print(id, problema, descripcion)
        problem = Problem(employee_id= id, type= problema, description= descripcion)
    return render(request, "fromEmpleado.html")

#ENSAMBLE
def ensamble_view(request):
    context = {"assembly_orders": Assembly_order.objects.all()}
    print(context)
    return render(request, "ensamblaje.html", context)

def add_assembly_order(request):
    if request.method == "POST":
        id = request.POST.get("exampleInputFolio")
        attendant_id = request.POST.get("exampleInputTitular")
        finish_date = request.POST.get("exampleInputFecha")
        description = request.POST.get("exampleFormDescripcionTextarea1")
        attendant=Employee.objects.get(id="attendant_id")
        notes = request.POST.get("exampleFormNotasTextarea1")
        print(id, attendant_id, finish_date, description, notes)
        assembly_order = Assembly_order(
            id=id,
            attendant=attendant,
            finish_date=finish_date,
            description=description,
            notes=notes,
        )
        assembly_order.save()
    return render(request, ensamble_view)

def update_assembly_order(request):
    if request.method == "POST":
        id = request.POST.get("exampleInputFolio")
        attendant = request.POST.get("exampleInputTitular")
        finish_date = request.POST.get("exampleInputFecha")
        description = request.POST.get("exampleFormDescripcionTextarea1")
        notes = request.POST.get("exampleFormNotasTextarea1")

        try:
            assembly_order = Product.objects.get(id=id)
            assembly_order.attendant = attendant
            assembly_order.finish_date = finish_date
            assembly_order.description = description
            assembly_order.description = description
            assembly_order.notes = notes
            assembly_order.save()
        except Product.DoesNotExist:
            print("El pedido no existe")
    return redirect(ensamble_view)

def delete_assembly_order(request, id):
    if request.method == "POST":
        assembly_order = Assembly_order.objects.get(id=id)
        assembly_order.delete()
    return redirect(ensamble_view)
