from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions, status
from yaml import serialize
from .models import (
    JobPostSkillSet,
    JobType,
    JobPost,
    Company
)
from django.db.models.query_utils import Q
from .serializers import (
    JobPostSkillSetSerializer,
    JobPostSerializer,
    CompanySerializer
)


class SkillView(APIView):

    permission_classes = [permissions.AllowAny]

    def get(self, request):
        skills = self.request.query_params.getlist('skills', '')
        serializer = JobPostSkillSetSerializer(JobPostSkillSet.objects.filter(skill_set__in=skills), many=True)
        # print("skills = ", end=""), print(skills)

        return Response(serializer.data, status=status.HTTP_200_OK)


class JobView(APIView):

    def post(self, request):
        # job_type = int( request.data.get("job_type", None) )
        # company = request.data.get("company", None)
        # job_type = JobType.objects.get(id=job_type)
        # company = Company.objects.get(company_name=company)

        serializer = JobPostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
