from rest_framework import serializers
from .models import Course

#class CourseSerializer(serializers.ModelSerializer):
 #   class Meta:
  #      model = Course
   #     fields = ('id', 'name', 'language', 'price')
     
#2 here   
class CourseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Course
        fields = ('id', 'url', 'name', 'language', 'price')