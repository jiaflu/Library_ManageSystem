from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Book,Reader,Record

#若想直接使用.models中的表单
#admin.site.register([Book, Reader, Record])

#此处为自定义表单
class RecordInline(admin.TabularInline):  #内联
    model = Record
    fk_name = "Reader"

class BooksAdmin(admin.ModelAdmin):
    save_as = True #设为Ture时，change页面的 "Save and add another"按钮会被"Save as"代替
    actions_on_top = True   #action的位置
    actions_on_bottom = False
    search_fields = ('Title', 'ISBN', 'id') #为该列表增加搜索栏
    list_filter = ('Pub_Time', 'Position', 'Available')
    list_display = ('id', 'Title', 'Author', 'ISBN', 'Publisher', 'Pages', 'Pub_Time', 'Position', 'Available')
    #list_display:Model的change list页面可以展示的字段,如果不设置,admin界面会自动展示Model的__unicode__()结果
    list_display_links = ('Title',)

    def make_available(modeladmin, request, queryset):
        queryset.update(Available=True)
    make_available.short_description = "Mark selected Books as Available"
    def make_unavailable(modeladmin, request, queryset):
        queryset.update(Available=True)
    make_available.short_description = "Mark selected Books as Unvailable"
    actions = [make_available, make_unavailable]

admin.site.register(Book,BooksAdmin)

class ReadersAdmin(admin.ModelAdmin):
    actions_on_top = True
    actions_on_bottom = False
    list_display = ('id', 'Name', 'Password', 'Active')
    search_fields = ('id', 'Name')
    list_filter = ('Active',)
    inlines = [      #Inline
        RecordInline,
    ]
    def make_available(modeladmin, request, queryset):
        queryset.update(Available=True)
    make_available.short_description = "Mark selected Books as Available"
    def make_unavailable(modeladmin, request, queryset):
        queryset.update(Available=True)
    make_available.short_description = "Mark selected Books as Unvailable"
    actions = [make_available, make_unavailable]

admin.site.register(Reader, ReadersAdmin)

class RecordsAdmin(admin.ModelAdmin):
    actions_on_top = True
    actions_on_bottom = False
    list_display = ('id','Reader','Book','Created_time','Modified_time','Status')
    list_display_links = ('id','Reader','Book','Status')
    search_fields = ('id', 'Reader__Name','Reader__id','Book__Title','Book__ISBN','Book__id')
    list_filter = ('Modified_time', 'Status','Book__Available')
    fields = ('Reader','Book','Status')

    def make_borrow(modeladmin, request, queryset):
        for record in queryset:
            if record.Status != 'BORROWED':
                b = record.Book
                if b.Available:
                    b.Available = False
                    b.save()
                    record.Status = 'BORROWED'
                    record.save()
                else:
                    record.Status = 'WAITFORCHECK'
                    record.save()

    make_borrow.short_description = "Mark BORROWED if book is Availible "

    def make_return(modeladmin, request, queryset):
        queryset.filter(Status = 'WAITFORCHECK').update(Status = 'TURNDOWN')