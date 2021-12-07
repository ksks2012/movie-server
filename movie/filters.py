class MovieFilter:
    def filter_queryset(self, request, queryset):
        year = request.query_params.get('year')
        genres = request.query_params.get('genres')
        title = request.query_params.get('title')
        filter_options = dict()
        if year is not None:
            filter_options['year'] = year
        if genres is not None:
            filter_options['genres__icontains'] = genres
        if title is not None:
            filter_options['title__icontains'] = title
        filtered_queryset = queryset.filter(**filter_options)
        return filtered_queryset
