from django import forms


class CreateBookForm(forms.Form):
    title = forms.CharField(max_length=150, label='Enter book title')
    released_year = forms.IntegerField()
    description = forms.CharField(widget=forms.Textarea, label='Enter description')
    author_id = forms.IntegerField()


class CreateReviewForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea, label='Write a review')
