from django.urls import path
from django_rest_passwordreset.views import reset_password_request_token, reset_password_confirm

from backend.views import ShopView, CategoryView, ProductsView, ProductInfoView, ContactView, RegisterAccount, \
    ConfirmAccount, LoginAccount, AccountDetails, PartnerUpdate, PartnerState, PartnerOrders, OrderView, BasketView

urlpatterns = [
    path('partner/update', PartnerUpdate.as_view(), name='partner-update'),
    path('partner/state', PartnerState.as_view(), name='partner-state'),
    path('partner/orders', PartnerOrders.as_view(), name='partner-orders'),


    path('shops/', ShopView.as_view(), name='shops'),
    path('category/', CategoryView.as_view(), name='categories'),
    path('products/', ProductsView.as_view(), name='products'),
    path('products/<id>/', ProductInfoView.as_view(), name='product_info'),
    path('order/', OrderView.as_view(), name='order'),
    path('basket', BasketView.as_view(), name='basket'),

    path('user/register', RegisterAccount.as_view(), name='user-register'),
    path('user/register/confirm', ConfirmAccount.as_view(), name='user-register-confirm'),
    path('user/details', AccountDetails.as_view(), name='user-details'),
    path('user/contact', ContactView.as_view(), name='user-contact'),
    path('user/login', LoginAccount.as_view(), name='user-login'),
    path('user/password_reset', reset_password_request_token, name='password-reset'),
    path('user/password_reset/confirm', reset_password_confirm, name='password-reset-confirm'),
]

