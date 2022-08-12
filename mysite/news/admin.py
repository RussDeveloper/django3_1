from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import News, Category

# Register your models here.


class NewsAdmin(admin.ModelAdmin):    #Класс-редактор
    list_display = ('id',
                    'title',
                    'category',
                    'created_at',
                    'updated_at',
                    'is_published',
                   # 'photo',
                    'get_photo',
                    )
    list_display_links = ('id', 'title')   #Поля, которые должны быть ссылками
    search_fields = ('title', 'content')   #Поля, по которым осуществляется поиск
    list_editable = ('is_published',)      #Список редактируемости полей из общего списка
    list_filter = ('is_published', 'category',)
    fields = ('title',
              'category',
              'content',
              'photo',
              'get_photo',
              'is_published',
              #'views',
              'created_at',
              'updated_at'
              )
    readonly_fields = ('get_photo',
                       #'views',
                       'created_at',
                       'updated_at'
                       )

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}", width="75">')
        else:
            return 'Фото не загружено'

    get_photo.short_description = 'Миниатюра'

class CategoryAdmin(admin.ModelAdmin):    #Класс-редактор
    list_display = ('id',
                    'title',
                    )
    list_display_links = ('id', 'title')   #Поля, которые должны быть ссылками
    search_fields = ('title', )   #Поля, по которым осуществляется поиск


admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)

admin.site.site_title = 'Управление новостями'
admin.site.site_header = 'Управление новостями'

