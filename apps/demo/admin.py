from django.contrib import admin


from .models import Table, Customer, WalkIn, Reservation

class TableAdmin(admin.ModelAdmin):
    list_display = ('table_size', 'seat_num')
    search_fields = ('table_size',)
    list_filter = ('table_size', 'seat_num')

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone')
    search_fields = ('name', 'phone')
    list_filter = ('name', 'phone')

class WalkInAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'people_num', 'table', 'date', 'time')
    search_fields = ('name', 'phone', 'people_num', 'table', 'date', 'time')
    list_filter = ('name', 'phone', 'people_num', 'table', 'date', 'time')

class ReservationAdmin(admin.ModelAdmin):
    list_display = ('name', 'people_num', 'table', 'date', 'time')
    search_fields = ('name', 'people_num', 'table', 'date', 'time')
    list_filter = ('name', 'people_num', 'table', 'date', 'time')

admin.site.register(Table, TableAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(WalkIn, WalkInAdmin)
admin.site.register(Reservation, ReservationAdmin)






