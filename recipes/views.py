from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Recipe
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import RecipeSearchForm
import pandas as pd
from .utils import get_chart, get_recipename_from_id

def welcome(request):
    return render(request, 'recipes/welcome.html')

class RecipeListView(LoginRequiredMixin, ListView):
    model = Recipe
    template_name = 'recipes/list.html'

class RecipeDetailView(LoginRequiredMixin, DetailView):
    model = Recipe
    template_name = 'recipes/detail.html'

def records(request):
    form = RecipeSearchForm(request.POST or None)
    recipe_df = None
    recipe_diff = None
    chart = None
    qs = None

    if request.method == 'POST':
        recipe_diff = request.POST.get('recipe_diff')
        chart_type = request.POST.get('chart_type')

        print(f"Received difficulty: {recipe_diff}")

        if recipe_diff == '#1':
            recipe_diff = 'Easy'
        elif recipe_diff == '#2':
            recipe_diff = 'Intermediate'
        elif recipe_diff == '#3':
            recipe_diff = 'Hard'

        qs = Recipe.objects.all()
        id_searched = []
        for obj in qs:
            diff = obj.calculate_difficulty()
            if diff == recipe_diff:
                id_searched.append(obj.id)

        qs = qs.filter(id__in=id_searched)

        if qs:
            recipe_df = pd.DataFrame(qs.values())
            chart = get_chart(chart_type, recipe_df, labels=recipe_df['name'].values)
            recipe_df = recipe_df.to_html()

    context = {
        'form': form,
        'recipe_df': recipe_df,
        'recipe_diff': recipe_diff,
        'chart': chart,
        'qs': qs,
    }

    return render(request, 'recipes/search.html', context)
