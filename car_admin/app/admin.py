from django.contrib import admin

from .models import Car, Review
from .forms import ReviewAdminForm


class CarAdmin(admin.ModelAdmin):
	list_display = ('list_brand', 'list_model', 'list_review_count')
	list_filter = ['brand']
	search_fields = ['model']
	ordering = ['id']

	def list_brand(self, obj):
		return obj.brand
	list_brand.short_description = 'Бренд'

	def list_model(self, obj):
		return obj.model
	list_model.short_description = 'Модель'

	def list_review_count(self, obj):
		return obj.review_count()
	list_review_count.short_description = 'Количество просмотров'



class ReviewAdmin(admin.ModelAdmin):
	form = ReviewAdminForm
	list_display = ('list_car', 'list_title')
	search_fields = ['title']
	list_filter = ['title']
	ordering = ['id']

	def list_car(self, obj):
		return obj.car
	list_car.short_description = 'Машина'

	def list_title(self, obj):
		return obj.title
	list_title.short_description = 'Название'


admin.site.register(Car, CarAdmin)
admin.site.register(Review, ReviewAdmin)
