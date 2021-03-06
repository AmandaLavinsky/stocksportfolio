from django import forms
from .models import Stock,UpperLimit,LowerLimit	

class StockForm(forms.ModelForm):
	class Meta:
		model = Stock
		fields = ["ticker"]

class UpperLimitForm(forms.ModelForm):
	class Meta:
		model = UpperLimit
		fields = ["highprice"]

class LowerLimitForm(forms.ModelForm):
	class Meta:
		model = LowerLimit
		fields = ["lowprice"]

