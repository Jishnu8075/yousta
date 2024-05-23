from django.urls import path

from yousta.views import SignUpView,SignInView,CategoryCreateView,remove_category\
,ClothCreateView,ClothListView,ClothUpdateView,remove_clothview,ClothVarientCreateView,\
    ClothDetailView,ClothVarientUpdateView,remove_varient,OfferCreateView,offer_delete_view,sign_out_view,IndexView,cart_view



urlpatterns=[

    path("register/",SignUpView.as_view(),name="signup"),
    path("categories/add",CategoryCreateView.as_view(),name="add-category"),
    path("",SignInView.as_view(),name="signin"),
    path("categories/<int:pk>/remove",remove_category,name="remove-category"),
    path("cloths/add",ClothCreateView.as_view(),name="cloth-add"),
    path("cloths/all",ClothListView.as_view(),name="cloth-list"),
    path("cloths/<int:pk>/change",ClothUpdateView.as_view(),name="cloth-change"),
    path("cloths/<int:pk>/remove",remove_clothview,name="cloth-remove"),
    path("cloths/<int:pk>/varients/add",ClothVarientCreateView.as_view(),name="add-varient"),
    path("cloths/<int:pk>/",ClothDetailView.as_view(),name="cloth-detail"),
    path("varients/<int:pk>/change/",ClothVarientUpdateView.as_view(),name="update-varient"),
    path("varients/<int:pk>/remove",remove_varient,name="remove-varient"),
    path("varients/<int:pk>/offers/add",OfferCreateView.as_view(),name="offers-add"),
    path('offers/<int:pk>/remove',offer_delete_view,name='delete-offer'),
    path('logout/',sign_out_view,name='signout'),
    path('index/',IndexView.as_view(),name='index'),
    path("cloths/<int:pk>/cart/add",cart_view,name="cart-add")






]