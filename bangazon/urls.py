from django.conf.urls import url, include
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from BangazonAPI import views

router = routers.DefaultRouter()
router.register(r'customer', views.CustomerViewSet)
router.register(r'product', views.ProductViewSet)
router.register(r'paymenttypes', views.PaymentTypeViewSet)
router.register(r'producttype', views.ProductTypeViewSet)
router.register(r'order', views.OrderViewSet)
router.register(r'orderproduct', views.OrderProductViewSet)
router.register(r'trainingcourse', views.TrainingCourseViewSet)
router.register(r'department', views.DepartmentViewSet)
router.register(r'employee', views.EmployeeViewSet)
router.register(r'employeetraining', views.EmployeeTrainingViewSet)
router.register(r'computer', views.ComputerViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-token-auth/', obtain_auth_token),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
