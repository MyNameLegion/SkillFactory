from django_filters import FilterSet, DateFilter
from django.forms import DateInput
from .models import Post


class PostFilter(FilterSet):
    added_after = DateFilter(
        field_name='date_time',
        label='Дата',
        lookup_expr='lt',
        widget=DateInput(
            format='%m-%d-%Y',
            attrs={'type': 'date'},
        ),
    )

    class Meta:
        model = Post
        fields = {
            'title': ['icontains'],
            'category': ['exact'],
        }

