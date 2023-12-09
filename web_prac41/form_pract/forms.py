from django import forms

genders = [
    ('', 'Please select'),
    ('male', 'Male'),
    ('female', 'Female')
]

hobbies = [
    ('gardening', 'Gardening'),
    ('coin_collection', 'Coin Collection'),
    ('waku', 'Waku')
]


class PracticeForm(forms.Form):
    char = forms.CharField(max_length=5)
    email = forms.EmailField()
    choice = forms.ChoiceField(
        choices=genders,
        show_hidden_initial=True,
        initial=''
    )
    choiceRadio = forms.ChoiceField(
        choices=genders,
        show_hidden_initial=True,
        initial='',
        widget=forms.RadioSelect()
    )
    multiChoiceCheck = forms.MultipleChoiceField(label='Hobbies Check box',choices=hobbies,widget=forms.CheckboxSelectMultiple())
    multiChoice = forms.MultipleChoiceField(label='Hobbies',choices=hobbies)
    dateF = forms.DateField(label='Birth Date',widget=forms.SelectDateWidget())
    boolField = forms.BooleanField(label='Ami amar sob jomi tomake diye dilam')
    decimal = forms.DecimalField()
    integer = forms.IntegerField(label='Age')
