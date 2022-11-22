from django.urls import path
from billing import views


urlpatterns = [
    path("uploads/", views.BillingView.as_view()),
    path("filter/month/<int:month>/", views.BillingByDateView.as_view()),
    path("filter/client/<int:client>/", views.BillingByClientView.as_view()),
    path("filter/category/<str:category>/", views.BillingByCategoryView.as_view()),
    path("filter/product/<str:product>/", views.BillingByProductView.as_view()),
    path("list/", views.BillingAllVIew.as_view()),
    path("quarterly/<int:quarter>/", views.BillingByQuarterlyView.as_view())
]
