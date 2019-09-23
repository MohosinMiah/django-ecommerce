from django import forms



class SuggesstionForm(forms.Form):
    
    name = forms.CharField()
    email = forms.EmailField()
    suggestion = forms.CharField(widget=forms.Textarea)
    honeypot = forms.CharField(required=False,widget=forms.HiddenInput,label="Leave Empty")


    def clean_honeypot(self):
        data = self.cleaned_data["honeypot"]
        if len(data):
            raise forms.ValidationError("Leave It Empty")
        return data
       
