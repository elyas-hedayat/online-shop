from rest_framework import generics

from .models import Apply, Job
from .serializers import ApplySerializer, JobSerializer


class JobListApiView(generics.ListAPIView):
    queryset = Job.objects.filter(active=True)
    serializer_class = JobSerializer


class ApplyCreateApiView(generics.CreateAPIView):
    queryset = Apply.objects.all()
    serializer_class = ApplySerializer
