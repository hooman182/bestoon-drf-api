from rest_framework.generics import ListAPIView
from .models import Income
from .serializers import IncomesSerilizer
#------------------------------------------------------------------------


class IncomeListViews(ListAPIView):
    queryset = Income.objects.all()
    serializer_class = IncomesSerilizer