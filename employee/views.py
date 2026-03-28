from rest_framework.decorators import api_view
from .models import Employee
from.serializers import EmployeeSerializer
from rest_framework.response import Response

@api_view(['POST'])
def add_employee(request):

        serializer = EmployeeSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Successfully added employee"})
        else:
            return Response({"message": "Failed to add employee"}, status=400)
        


@api_view(['GET'])  # Decorator to specifiy that view only accepts GET requests
def get_employees(request):
    employees = Employee.objects.all()  #Employee -> Model .objets -> model Manager .all() -> Get All
    serializer = EmployeeSerializer(employees, many=True)  # converts model to JSON, employees -> queryset , Many = True sends multiple JSON objects
    return Response(serializer.data)



@api_view(['PUT'])
def update_employee(request,id):
    try:
        employee = Employee.objects.get(id=id)
    except Employee.DoesNotExist:
        return Response({"message": "Employee not found"}, status=404)

    serializer = EmployeeSerializer(employee, data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Employee updated successfully"})
    else:
        return Response({"message": "Failed to update employee"}, status=400)



@api_view(['DELETE'])
def delete_employee(request, id):
    try:
        employee = Employee.objects.get(id=id)
    except Employee.DoesNotExist:
        return Response({"message": "Employee not found"}, status=404)

    employee.delete()
    return Response({"message": "Employee deleted successfully"})