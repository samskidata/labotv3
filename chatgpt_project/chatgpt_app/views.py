from django.shortcuts import render
from chatgpt_app import views

# Create your views here.


from django.http import JsonResponse
import openai
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

openai.api_key = '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' # replace with your OpenAI API key
chat_model = "gpt-4.0-turbo"

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("login")
    else:
        form = UserCreationForm()
    return render(request, "register.html", {"form": form})


def chat_with_gpt(message):
    response = openai.ChatCompletion.create(
      model=chat_model,
      messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": message}
        ]
    )
    return response['choices'][0]['message']['content']

def chat_view(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        response = chat_with_gpt(message)
        return JsonResponse({'message': response})

    return render(request, 'chatgpt_app/chat.html')

