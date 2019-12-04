from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse

from .models import Product, Review
from .forms import ReviewForm

from django.http import HttpResponseRedirect
from django.shortcuts import render


def product_list_view(request):
    template = 'app/product_list.html'

    products = Product.objects.all()

    context = {
        'product_list': products,
    }

    return render(request, template, context)


def product_view(request, pk):
    template = 'app/product_detail.html'

    is_review_exist = False

    print(request.session['reviewed_products'])
    session_set = set(request.session['reviewed_products'])
    tm_arr = request.session['reviewed_products']

    product = get_object_or_404(Product, id=pk)
    form = ReviewForm(request.POST)

    if request.method == 'POST':

        if form.is_valid():
            text = form.cleaned_data['text']

            if pk not in session_set:
                review = Review(text = text, product = Product.objects.get(id=pk))
                review.save()
                tm_arr.append(pk)
                request.session['reviewed_products'] = tm_arr
            else:
                is_review_exist = True

            # return HttpResponseRedirect('/success/')

    print(request.session['reviewed_products'])

    context = {
        'form': form,
        'product': product,
        'is_review_exist': is_review_exist,
        'reviews': Review.objects.all().filter(product = product).order_by('-id')
    }

    return render(request, template, context)


