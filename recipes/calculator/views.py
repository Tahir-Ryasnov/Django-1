from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
}

def home_view(request):
    recipes = list(DATA.keys())
    return render(request, 'home.html', context={'recipes': recipes})

def show_recipe(request, recipe_name):
    ingr = DATA[recipe_name]
    count = int(request.GET.get("count", 1))
    result = dict()
    for key, value in ingr.items():
        new_value = value * count
        result[key] = new_value
    context = {
        'recipe_name': recipe_name,
        'recipe': result
    }
    return render(request, template_name='calculator/index.html', context=context)
