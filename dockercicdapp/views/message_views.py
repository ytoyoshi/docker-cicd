from django.shortcuts import render, get_object_or_404, redirect
from ..models import Message
from ..forms import MessageForm

def message_list(request):
    messages = Message.objects.all()
    return render(request, 'message.html', {'messages': messages})

def message_create(request):
    if request.method == 'POST':
        print("create")
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('message')
    else:
        form = MessageForm()
    return render(request, 'message.html', {'form': form})

def message_delete(request, pk):
    message = get_object_or_404(Message, pk=pk)

    if request.method == 'POST':
        message.delete()
        return redirect('message')

    return render(request, 'message_confirm_delete.html', {'message': message})