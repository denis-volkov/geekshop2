from django.shortcuts import render


def main(request):
    return render(request, 'mainapp/index.html')


def products(request):
    links_menu = [
        {'href': 'products_all', 'name': 'все'},
        {'href': 'products_premium', 'name': 'премиум'},
        {'href': 'products_speed', 'name': 'быстроходные'},
        {'href': 'products_other', 'name': 'другое'}
    ]
    content = {'links_menu': links_menu}
    return render(request, 'mainapp/products.html', content)


def products_all(request):
    return render(request, 'mainapp/products.html')


def products_speed(request):
    return render(request, 'mainapp/products.html')


def products_premium(request):
    return render(request, 'mainapp/products.html')


def products_other(request):
    return render(request, 'mainapp/products.html')


def contact(request):
    return render(request, 'mainapp/contact.html')