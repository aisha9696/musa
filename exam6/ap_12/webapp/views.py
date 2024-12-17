from django.shortcuts import render, get_object_or_404, redirect
from webapp.models import Record
from webapp.forms import RecordForm


def index_view(request):
    context = {'record': Record.objects.filter(status='active').order_by('-created_at')}
    return render(request, 'index.html', context)


def record_create_view(request):
    if request.method == 'GET':
        form = RecordForm()
        return render(request, 'record/create.html', context={'form': form})
    elif request.method == 'POST':
        print(request.POST)
        form = RecordForm(data=request.POST)

        if form.is_valid():
            Record.objects.create(
                author=request.POST.get('author'),
                text=request.POST.get('text'),
                status='active',
                email=request.POST.get('email'),
            )

            return redirect('index')

        else:
            return render(
               request, 'record/create.html',
               context={'form': form},
            )


def record_update_view(request, id):
    record = get_object_or_404(Record, id=id)

    if request.method == 'GET':
        form = RecordForm(initial={
            'author': record.author,
            'text': record.text,
            'email': record.email,
        })

        return render(
            request, 'record/update.html',
            context={'record': record, 'form': form},
        )

    elif request.method == 'POST':
        form = RecordForm(data=request.POST)

        if form.is_valid():
            record.author = form.cleaned_data.get('author')
            record.text = form.cleaned_data.get('text')
            record.email = form.cleaned_data.get('email')

            record.save()

            return redirect('index')
        else:
            return render(request, 'record/update.html', context={'form': form, 'record': record})


def record_delete_view(request, id):
    get_object_or_404(Record, id=id).delete()
    return redirect('index')
