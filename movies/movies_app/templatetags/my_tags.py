from django import template
from movies_app.models import Genre, Movie

register = template.Library()

@register.inclusion_tag('movies_app/sidebar.html')
def show_sidebar():
    genres = Genre.objects.all()
    years = [movie.year for movie in Movie.objects.all()]
    years_distinkt = [i for i in set(years)]
    
    

     
    return {'genres':genres, 'years':years_distinkt}
