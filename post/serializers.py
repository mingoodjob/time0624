from rest_framework import serializers
from post.models import SkillSet, JobPostSkillSet, JobType, JobPost, Company, CompanyBusinessArea, BusinessArea

class JobTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobType
        fields = ('job_type',)

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('company_name',)

class JobPostSerializer(serializers.ModelSerializer):
    job_types = JobTypeSerializer(read_only=True)
    company_set = CompanySerializer(read_only=True)

    class Meta:
        model = JobPost
        fields = ('job_types', 'company_set','job_description', 'salary', 'created_at')

    def create(self, validated_data):
        # print(validated_data.get('job_type'))
        job_type = JobType.objects.get(id=validated_data.get('job_type'))
        company = Company.objects.get(name=validated_data.get('company'))   
        job_post = JobPost.objects.create(job_type=job_type, company=company, job_description=validated_data.get('job_description'), salary=validated_data.get('salary'))

        return job_post

class JobPostSkillSetSerializer(serializers.ModelSerializer):

    class Meta:
        model = JobPostSkillSet
        fields = ('skill_set',)

    
        

