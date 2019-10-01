# Create your views here.

from django.shortcuts import render_to_response
from map.models import Building, Department

def Test(request):
    return render_to_response('test.html')

def Home(request):
    return render_to_response('index.html')

def All(request):
    buildings = Building.objects.all()
    departments = Department.objects.all()
    context = {'buildings': buildings,'departments':departments}
    return render_to_response('display.html',context)
    
def SpecificBuilding(request, buildingname):
    buildings = Building.objects.all()
    if buildingname.find('/') == -1:
        building = Building.objects.get(name = buildingname)
        #department = Building.objects.get(name = buildingname).department_set.all()
        context = {'building':building,'buildings': buildings}
        return render_to_response('singledisplay.html',context)
    else:
        departmentname = buildingname.split('/')
        department = Department.objects.get(name = departmentname[1])
        context = {'department':department,'buildings': buildings}
        return render_to_response('deptdisplay.html',context)