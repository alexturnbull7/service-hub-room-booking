from django.urls import path

from .views import RoomList, RoomDetail, CompanyList, CompanyDetail, UserTypeList, UserTypeDetail, StatusList, StatusDetail, ProfileList, ProfileDetail, UserList, UserDetail, BookingList, BookingDetail, BookingByLeadBooker, RoomSearchList  

urlpatterns = [
    path('room', RoomList.as_view()),
    path('room/<int:pk>/', RoomDetail.as_view()),
    path('company', CompanyList.as_view()),
    path('company/<int:pk>/', CompanyDetail.as_view()),
    path('user-type', UserTypeList.as_view()),
    path('user-type/<int:pk>/', UserTypeDetail.as_view()),
    path('status', StatusList.as_view()),
    path('status/<int:pk>/', StatusDetail.as_view()),
    path('profile', ProfileList.as_view()),
    path('profile/<int:pk>/', ProfileDetail.as_view()),
    path('user', UserList.as_view()),
    path('user/<int:pk>/', UserDetail.as_view()),
    path('booking', BookingList.as_view()),
    path('booking/<int:pk>/', BookingDetail.as_view()),
    path('search/room/', RoomSearchList.as_view()),
    path('booking/leadbooker/', BookingByLeadBooker.as_view()),
]

