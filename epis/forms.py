from django import forms
from .models import EPI  # remova EntregaEPI se não existir
# from .models import Colaborador  # descomente se precisar deste form


class EPIForm(forms.ModelForm):
    class Meta:
        model = EPI
        fields = ['nome', 'ca']  # ajuste de acordo com seus campos
