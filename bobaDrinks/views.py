from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.shortcuts import redirect



from .models import Drink, Customer
from .forms import DrinkForm, CustomerForm

def index(request):
    #template = loader.get_template('bobaDrinks/index.html')
    context = {
        'name': 'jennifer',
    }
    #return HttpResponse(template.render(context, request))
    return render(request, 'bobaDrinks/index.html', context)  

def orderForm(request):
    #template = loader.get_template('bobaDrinks/base.html')
    if request.POST:
        dForm = DrinkForm(request.POST, prefix="drin")
        cForm = CustomerForm(request.POST, prefix="cust")
        if dForm.is_valid() and cForm.is_valid():
           # post = cform.save(commit=False)
            #cform.time = request.time
            #post.save()
            #dform.save()

            #a = dform.save()
            #b = cform.save(commit=False)
            #b.foreignkeytoA = a
            #b.save()

           # order = dForm.save(commit=False)
            # order.customer = cForm.save()
            dForm.save()
            cForm.save()

            return redirect('orderHistory/')#, pk=post.pk)
    else:
       dForm = DrinkForm(instance=Drink())
       cForm = CustomerForm()
    return render(request, 'bobaDrinks/orderForm.html', {'dForm': dForm, 'cForm': cForm,})

    
def orderHistory(request, order_id):
   # template = loader.get_template('bobaDrinks/orderHistory.html')
    context = {
        'name': 'jennifer',
    }
    #return HttpResponse(template.render(context, request))
    return render(request, 'bobaDrinks/orderHistory.html', context)  


    #hey testinig