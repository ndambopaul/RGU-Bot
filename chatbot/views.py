# Create your views here.
# from django.shortcuts import render
# from .utils.vector_utils import load_vector_store, find_similar
# from .utils.openai_utils import generate_answer_gpt4

# def chatbot_view(request):
#     user_message = None
#     bot_response = None
#     error_message = None

#     if request.method == 'POST':
#         user_message = request.POST.get('message')
#         vector_store_path = './vector_store.json'
        
#         try:
#             vector_store = load_vector_store(vector_store_path)
#             similar_docs = find_similar(user_message, vector_store)
            
#             if similar_docs:
#                 bot_response = generate_answer_gpt4(similar_docs, user_message)
#             else:
#                 bot_response = "I'm sorry, I couldn't find relevant information."
#         except FileNotFoundError:
#             error_message = "Our service is temporarily unavailable. Please try again later."
#             bot_response = None 

#     return render(request, 'chatbot/chat.html', {
#         'user_message': user_message,
#         'bot_response': bot_response,
#         'error_message': error_message  # Pass the error message to the template
#     })


# Create your views here.
import os
from django.shortcuts import render
from .utils.vector_utils import load_vector_store, find_similar
from .utils.openai_utils import generate_answer_gpt4

def chatbot_view(request):
    user_message = None
    bot_response = None

    if request.method == 'POST':
        user_message = request.POST.get('message')
        vector_store_path = 'data/vector_store.json'
        vector_store = load_vector_store(vector_store_path)
        
        similar_docs = find_similar(user_message, vector_store)
        
        if similar_docs:
            bot_response = generate_answer_gpt4(similar_docs, user_message)
        else:
            bot_response = "I'm sorry, I couldn't find relevant information."

    return render(request, 'chatbot/chat.html', {
        'user_message': user_message,
        'bot_response': bot_response
    })