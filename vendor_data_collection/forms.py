from django import forms


VENDOR_TYPE_CHOICES=(
    ('ice-cream','Ice Cream Vendor'),
    ('vegetables','Vegetable/Fruits Vendor'),
    ('street-food','Street Food Vendor'),
    ('drinks','Drinks')
)

AVAILABILITY_CHOICES=(
    ('year','Yearly'),
    ('season','Seasonally')
)

HOUR_CHOICES=(
    ('1','1'),
    ('2','2'),
    ('3','3'),
    ('4','4'),
    ('5','5'),
    ('6','6'),
    ('7','7'),
    ('8','8'),
    ('9','9'),
    ('10','10'),
    ('11','11'),
    ('12','12'),
)
MINUTE_CHOICES=(
    ('00','00'),
    ('15','15'),
    ('30','30'),
    ('45','45'),
)

TIME_TYPE_CHOICES=(
    ('am','AM'),
    ('pm','PM')
)

RATING_CHOICES=(
    ('1','1'),
    ('2','2'),
    ('3','3'),
    ('4','4'),
    ('5','5')
)

USER_CHOICES=(
    ('1','1'),
    ('2','2'),
    ('3','3'),
    ('4','4'),
    ('5','5')
)

class user_form(forms.Form):
    user = forms.ChoiceField( choices=USER_CHOICES,widget=forms.Select(attrs={'class':'form-control', 'style': 'margin-bottom:15px;'}))




class add_vendor_form_p1(forms.Form):
    name = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class':'form-control', 'style': 'margin-bottom:15px;'}),required=False)
    phone = forms.CharField(max_length=10,widget=forms.TextInput(attrs={'class':'form-control', 'style': 'margin-bottom:15px;'}),required=False)
    availability = forms.ChoiceField( choices=AVAILABILITY_CHOICES,widget=forms.Select(attrs={'class':'form-control', 'style': 'margin-bottom:15px;'}))
    paytm_available = forms.BooleanField(widget=forms.CheckboxInput(),required=False)
    vendor_type = forms.ChoiceField(choices=VENDOR_TYPE_CHOICES,widget=forms.Select(attrs={'class':'form-control', 'style': 'margin-bottom:15px;'}))


class add_vendor_form_p2(forms.Form):


    def __init__(self, *args, **kwargs):
        super(add_vendor_form_p2, self).__init__(*args, **kwargs)
        for i in range(10):
            self.fields['Latitude' + str(i)] = forms.CharField(max_length=20, required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Latitude'}))
            self.fields['Longitude' + str(i)] = forms.CharField(max_length=20, required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Longitude'}))
            self.fields['Pin' + str(i)] = forms.CharField(max_length=10, required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'PIN'}))
            self.fields['StartHour' + str(i)] = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control'}),choices=HOUR_CHOICES, required=False)
            self.fields['StartMinute' + str(i)] = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control'}), choices=MINUTE_CHOICES, required=False)
            self.fields['StartType' + str(i)] = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control'}),choices=TIME_TYPE_CHOICES, required=False)
            self.fields['EndHour' + str(i)] = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control'}),choices=HOUR_CHOICES, required=False)
            self.fields['EndMinute' + str(i)] = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control'}),choices=MINUTE_CHOICES, required=False)
            self.fields['EndType' + str(i)] = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control'}),choices=TIME_TYPE_CHOICES, required=False)

class add_vendor_form_p3(forms.Form):

    hygeine_rating=forms.ChoiceField(choices=RATING_CHOICES,widget=forms.Select(attrs={'class':'form-control', 'style': 'margin-bottom:15px;'}))
    taste_rating=forms.ChoiceField(choices=RATING_CHOICES,widget=forms.Select(attrs={'class':'form-control', 'style': 'margin-bottom:15px;'}))
