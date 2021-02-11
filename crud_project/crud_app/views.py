from django.shortcuts import render, redirect, get_object_or_404
from .forms import StudentForm
from . models import StudentModel
# Create your views here.

def create_view(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = StudentForm()
    context = {
        'form':form
    }
    return render(request, 'create.html', context)


def Retrieve_ListView(request):
    dataset = StudentModel.objects.all()
    return render(request, 'listview.html', {'dataset': dataset})


def Retrieve_DetailView(request, _id):
    try:
        data = StudentModel.objects.get(id=_id)
    except StudentModel.DoesNotExist:
        raise Http404('Data does not exist')

    return render(request, 'detailview.html', {'data': data})
    
def DeleteView(request, _id):
    try:
        data = get_object_or_404(StudentModel, id = _id)
    except Exception:
        raise Http404('Data does not exist')
    if request.method == 'POST':
        data.delete()
        return redirect('/data')
    else:
        return render(request, 'delete.html')



def UpdateView(request, _id):
    try:
        old_data = get_object_or_404(StudentModel, id=_id)
    except Exception:
        raise Http404('Does Not Exist')

    if request.method == 'POST':
        form = StudentForm(request.POST, instance=old_data)

        if form.is_valid():
            form.save()
            return redirect(f'/data/{_id}')

    else:

        form = StudentForm(instance=old_data)
        context = {
            'form': form
        }
        return render(request, 'update.html', context)