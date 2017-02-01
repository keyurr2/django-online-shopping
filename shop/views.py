from django.shortcuts import render
from .models import ProductDetails, Tag


# Create your views here.
def index(request):

	products = ProductDetails.objects.all().order_by('-published_on')

	# if user need to filter products otherwise list all products
	
	if request.method == "POST":
		
		# Filter criteria
		search_query = request.POST.get("search_query", None)
		min_price = request.POST.get("min_price", None)
		max_price = request.POST.get("max_price", None)
		rating = request.POST.get("rating", None)
		tag = request.POST.get("tag", None)
	
		if search_query:
			products = ProductDetails.objects.filter(name__contains = search_query)
		if min_price:
			products = products.filter(price__gte = min_price)
		if max_price:
			products = products.filter(price__lte = max_price)
		if rating and rating != "-":
			products = products.filter(ratings = rating)
		if tag and tag != "-":
			products = products.filter(Tags__in = [tag])

	context = {
		'title':'list of products', 
		'products' : products,
		'rating' : ProductDetails.RATING_CHOICE,
		'tags' : Tag.objects.all()
	}
	return render(request, 'shop/list.html', context)
