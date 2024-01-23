from django import forms

CHART__CHOICES = (
    ('#1', 'Bar chart'),
    ('#2', 'Pie chart'),
    ('#3', 'Line chart')
)

DIFFIC__CHOICES = (
    ('#1', 'Easy'),
    ('#2', 'Intermediate'),
    ('#3', 'Hard')
)


class RecipeSearchForm(forms.Form):
    recipe_diff = forms.ChoiceField(choices=DIFFIC__CHOICES)
    chart_type = forms.ChoiceField(choices=CHART__CHOICES)