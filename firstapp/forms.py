from django import forms

class NameForm(forms.Form):
  your_name = forms.CharField(
    label='Your name', max_length=5)

from .models import Curriculum
class CurriculumForm(forms.ModelForm):
  class Meta:
    model = Curriculum
    fields = ['name'] # id 속성은 PK 이므로 사용하지 않음
    
    labels = { # fields에 명시된 속성만 사용
    'name': '과목'
    }