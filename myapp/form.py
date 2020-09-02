from django import forms  
from myapp.models import Employee  
  
class EmpForm(forms.ModelForm):  
    class Meta:  
        model = Student  
        fields = "__all__"  