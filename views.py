from django.shortcuts import render
from .forms import UploadPDFForm
from django.http import HttpResponse
import PyPDF2
from django.conf import settings
import requests  # Assuming you are using requests to make an API call
from django.shortcuts import redirect

def upload_pdf(request):
    if request.method == 'POST' and request.FILES.get('pdf_file'):
        uploaded_file = request.FILES['pdf_file']
        with open(f'./media/{uploaded_file.name}', 'wb') as f:
            for chunk in uploaded_file.chunks():
                f.write(chunk)
        return redirect('quiz_home')  # Redirect back to home after uploading



def quiz_home(request):
    form = UploadPDFForm()  # Initialize the form
    return render(request, 'quiz_app/quiz_home.html', {'form': form})





def some_view(request):
    api_key = settings.API_KEY  # Access the API key from settings.py
    
    # Assuming you're making a GET request to an external API
    url = "https://api.example.com/your-endpoint"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }

    # Example API request (adjust the URL, headers, or method as needed)
    response = requests.get(url, headers=headers)

    # You can handle the response here
    if response.status_code == 200:
        # Parse the response if needed
        data = response.json()
        # Do something with the data (e.g., pass to template)
        return render(request, 'result.html', {'data': data})
    else:
        return HttpResponse("API request failed!", status=response.status_code)




# View for the home page (Upload Form)
def home(request):
    return render(request, 'home.html')

def extract_pdf_text(pdf_file):
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    text = ''
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text



def quiz_result(request):
    # Your logic to process the result
    return render(request, 'quiz_app/quiz_result.html')  # Replace with your actual template




def submit_quiz(request):
    if request.method == 'POST':
        # Process the form data or quiz answers
        # For example, saving results or calculating scores
        return HttpResponse("Quiz Submitted Successfully")
    return render(request, 'quiz_app/submit_quiz.html')  # Or return a different template if needed




















