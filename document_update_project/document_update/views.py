from django.shortcuts import render, redirect
from .forms import FileUploadForm
from .models import UploadedFile

def upload_file(request):
    file_instance = UploadedFile.objects.first()
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES, instance=file_instance)
        if form.is_valid():
            form.save()
            return redirect('upload_file')
    else:
        form = FileUploadForm(instance=file_instance)
    return render(request, 'upload_file.html', {'form': form})

def delete_file(request):
    file_instance = UploadedFile.objects.first()
    if file_instance:
        file_instance.delete()
    return redirect('upload_file')
