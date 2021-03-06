from django.shortcuts import render,redirect
from .models import Stock,UpperLimit,LowerLimit
from .forms import StockForm,UpperLimitForm,LowerLimitForm
from django.contrib import messages
#from django.core.mail import send_mail
#from stocks.settings import EMAIL_HOST_USER

# Create your views here.

def home(request):
	import requests
	import json

	if request.method == 'POST':
		ticker = request.POST['ticker']
		api_request = requests.get("https://cloud.iexapis.com/stable/stock/" + ticker + "/quote?token=pk_bc93d0a28f8e457a8d2218081561c802")

		try:
			#Converte JSON em um dicionário Python
			api = json.loads(api_request.content)
		except Exception:
			api = "Error"
		return render(request, 'home.html', {'api': api,'error':"Not access the api"})
	
	else:	
		return render(request, 'home.html', {'ticker': "Type a Ticker Above to get quote information..."})


	#pk_bc93d0a28f8e457a8d2218081561c802


def news(request):
	import requests
	import json
	
	api_request = requests.get('http://newsapi.org/v2/top-headlines?q=stocks&apiKey=5c12a9b1ef6c4339a30e94b17c773a7c')	
	api = json.loads(api_request.content)
	return render(request, 'news.html', {'api': api}) 
	messages.success(request, ("Stock Has Been Deleted from the Portfolio"))
	return redirect(add_stock)

def search_news(request):
	import requests
	import json

	if request.method == 'POST':
		ticker = request.POST['ticker']
		api_request = requests.get("http://newsapi.org/v2/everything?q="+ticker+"&apiKey=5c12a9b1ef6c4339a30e94b17c773a7c")

		try:
			api = json.loads(api_request.content)
		except Exception:
			api = "Error"
		return render(request, 'search_news.html', {'api': api,'error':"Could not access the api"})
	
	else:	
		return render(request, 'search_news.html', {'ticker': "Search news by ticker..."})


def add_stock(request):
	import requests
	import json

	if request.method == 'POST':
		form = StockForm(request.POST or None)

		if form.is_valid():
			form.save()
			messages.success(request,("A New Stock Has Been Added to Amanda's Portfolio"))
			return redirect('add_stock')

	else:
		ticker = Stock.objects.all()
		ticker_list = []

		for ticker_item in ticker:
			api_request = requests.get("https://cloud.iexapis.com/stable/stock/" + str(ticker_item) + "/quote?token=pk_bc93d0a28f8e457a8d2218081561c802")

			try:
				api = json.loads(api_request.content)
				ticker_list.append(api)


			except Exception:
				api = "Error..."

		return render(request,'add_stock.html',{'ticker': ticker, 'ticker_list':ticker_list})

def delete(request,stock_id):
	item = Stock.objects.get(pk=stock_id)
	item.delete()
	messages.success(request, ("Stock Has Been Deleted!"))
	return redirect(delete_stock)

def delete_stock(request):
	ticker = Stock.objects.all()
	return render(request,'delete_stock.html',{'ticker': ticker})

#def email():
	#send_mail(subject, message, EMAIL_HOST_USER, [recepient], fail_silently = False)


def add_upperlimit(request):
	import requests
	ticker = Stock.objects.all()
	if request.method == 'POST':
		highprice = UpperLimitForm(request.POST or None)

		if highprice.is_valid():
			highprice.save()
			messages.success(request,("The upper price limit has been set"))
			return redirect('add_upperlimit')
	else:
		highprice = UpperLimit.objects.all()
	return render(request,'add_upperlimit.html',{'highprice': highprice,'ticker': ticker})

def add_lowerlimit(request):
	import requests
	ticker = Stock.objects.all()
	if request.method == 'POST':
		lowprice = LowerLimitForm(request.POST or None)

		if lowprice.is_valid():
			lowprice.save()
			messages.success(request,("The lower price limit has been set"))
			return redirect('add_lowerlimit')
	else:
		lowprice = LowerLimit.objects.all()
	return render(request,'add_lowerlimit.html',{'lowprice': lowprice,'ticker': ticker})



