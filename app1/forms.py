from django import forms
from .models import LateCheckInPolicy
from django.core.exceptions import ValidationError

class LateCheckInPolicyForm(forms.ModelForm):
    class Meta:
        model = LateCheckInPolicy
        fields = ['student', 'start_time', 'description']
        widgets = {
            'start_time': forms.TimeInput(format='%H:%M', attrs={'type': 'time'}),
            'description': forms.Textarea(attrs={'rows': 3}),
        }

    def clean(self):
        cleaned_data = super().clean()
        student = cleaned_data.get('student')
        policy_id = self.instance.id  # Get the current instance's ID

        # Check if a LateCheckInPolicy already exists for this student, excluding the current instance
        if student and LateCheckInPolicy.objects.filter(student=student).exclude(id=policy_id).exists():
            raise ValidationError(f"A late check-in policy already exists for {student.name}.")
        
        return cleaned_data


from django import forms
from .models import Student

class StudentEditForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = [
            'name',
            'email',
            'student_class',
            'image',
            'joining_date',
        ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter full name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter email address'}),
            'student_class': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter class'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'joining_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }
