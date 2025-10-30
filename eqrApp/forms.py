from django import forms
from eqrApp import models


class SaveEmployee(forms.ModelForm):
    employee_code = forms.CharField(max_length=250, label="Company ID")
    first_name = forms.CharField(max_length=250, label="First Name")
    middle_name = forms.CharField(max_length=250, label="Middle Name", required=False)
    last_name = forms.CharField(max_length=250, label="Last Name")
    dob = forms.DateField(label="Birthday", widget=forms.DateInput(attrs={"type": "date"}))
    gender = forms.ChoiceField(choices=[("Male", "Male"), ("Female", "Female")], label="Gender")
    contact = forms.CharField(max_length=250, label="Contact #")
    email = forms.EmailField(max_length=250, label="Email")
    address = forms.CharField(widget=forms.Textarea, label="Address")
    department = forms.CharField(max_length=250, label="Department")
    position = forms.CharField(max_length=250, label="Position")
    avatar = forms.ImageField(label="Avatar", required=False)

    class Meta:
        model = models.Employee
        fields = (
            "employee_code",
            "first_name",
            "middle_name",
            "last_name",
            "dob",
            "gender",
            "contact",
            "email",
            "address",
            "department",
            "position",
            "avatar",
        )

    def clean_employee_code(self):
        id = self.data.get("id")
        employee_code = self.cleaned_data["employee_code"]

        try:
            if id and id.isdigit() and int(id) > 0:
                employee = models.Employee.objects.exclude(id=id).get(employee_code=employee_code)
            else:
                employee = models.Employee.objects.get(employee_code=employee_code)
        except models.Employee.DoesNotExist:
            return employee_code

        raise forms.ValidationError(f"{employee_code} already exists.")
