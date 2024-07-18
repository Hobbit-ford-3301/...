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


def recipes_views(request, data, dish_name):
    quantity_per_person = dict()

    number_of_person = int(request.GET.get("servings", 1))

    for name, quantity in data[dish_name].items():
        quantity_per_person.setdefault(name, quantity * number_of_person)

    context = {
        'data': quantity_per_person,
        'dish_name': dish_name,
        'persons': number_of_person
        }

    return render(request, 'index.html', context)