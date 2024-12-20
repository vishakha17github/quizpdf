from django.db import models

# Model for storing uploaded PDFs
class UploadedPDF(models.Model):
    file = models.FileField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.file)

# Model for questions in the quiz
class Question(models.Model):
    text = models.CharField(max_length=200)  # The text for the question
    options = models.JSONField()  # Stores options as a JSON object (e.g., ['Option1', 'Option2', 'Option3'])
    correct_answer = models.CharField(max_length=100)  # The correct answer for this question

    def __str__(self):
        return self.text

    class Meta:
        app_label = 'quiz'  # Specifies that this model belongs to the 'quiz' app





        
   



