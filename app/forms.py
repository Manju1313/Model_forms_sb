from django import forms
g=[['MALE','male'],('FEMALE','female')]
c=[['PYTHON','python'],['DJANGO','django'],['JAVA','java'],['HTML','html'],['SQL','sql'],['CSS','css'],['PHP','php']]
class NameForm(forms.Form):
    name         =forms.CharField(max_length=100)
    age          =forms.IntegerField()
    password     = forms.CharField(widget = forms.PasswordInput())
    roll_number  = forms.IntegerField(
                     help_text = "Enter 6 digit roll number"
                     )
    #password=forms.CharField(max_length=100,widget=forms.PasswordInput)
    #gender=forms.ChoiceField(choices=g)
    gender       = forms.ChoiceField(choices=g,widget=forms.RadioSelect)
    #course      =forms.MultipleChoiceField(choices=c)
    course     = forms.MultipleChoiceField(choices=c,widget=forms.CheckboxSelectMultiple)
    #first_name  = forms.CharField(max_length = 200)
    #last_name   = forms.CharField(max_length = 200)
    


class TopicForm(forms.Form):
    topic=forms.CharField(max_length=100)
    date=forms.DateField()
    duration=forms.CharField(max_length=122)

