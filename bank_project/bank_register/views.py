from django.shortcuts import render,redirect
from .forms import BankForm
from .models import Bank

# Create your views here.

def bank_list(request):
    context = {'bank_list':Bank.objects.all()}
    return render(request,'bank_register/bank_list.html',context)

def bank_form(request,id=0):
    if request.method == 'GET':
        if id==0:
            form = BankForm()
        else:
            bank = Bank.objects.get(pk=id)
            form = BankForm(instance=bank)    
        return render(request,'bank_register/bank_form.html',{'form':form})
    else:
        if id ==0:
            form = BankForm(request.POST)
        else:
            bank = Bank.objects.get(pk=id)
            form = BankForm(request.POST,instance= bank)
        if form.is_valid():
            form.save()
        return redirect('/bank/list')

def bank_delete(request,id):
    bank = Bank.objects.get(pk=id)
    bank.delete()
    return redirect('/bank/list')