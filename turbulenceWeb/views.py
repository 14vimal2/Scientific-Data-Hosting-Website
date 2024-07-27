from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.apps import apps
from django.template import loader
# from wsgiref.util import FileWrapper
# from django.conf import settings

from . import models
import inspect
import os, zipfile





def home_page(request):
    template = loader.get_template('main.html')
    context = {
        'selected_page': 'home_page',
    }
    return HttpResponse(template.render(context) )

def data_page(request):
    template = loader.get_template('data_page.html')
    model_names = [name for name, obj in inspect.getmembers(models, inspect.isclass)]

    context = {
        'model_names': ['Choose your model'] + model_names,
        'selected_page': 'data_page',
        'dataset_kind': 'Choose your model',
    }
    return HttpResponse(template.render(context, request))

def get_dataset(request: HttpRequest):

    if request.GET.get('dataset-kind') == None:
        return data_page(request)

    template = loader.get_template('data_page.html')

    ## get the model_names
    model_names = [name for name, obj in inspect.getmembers(models, inspect.isclass)]

    # print(request)
    mydata = apps.get_model(app_label='turbulenceWeb', model_name=request.GET['dataset-kind']).objects.all()
    
    

    
    fields_tmp = apps.get_model(app_label='turbulenceWeb', model_name=request.GET['dataset-kind']).__doc__.split("(")[1][:-1].split(",")
    fields = [s.strip() for s in fields_tmp if s != 'id']

    number_fields = [] # fields that are numbers

    # Get the fields that are numbers and append them to number_fields

    for field in fields:
        # type(myVariable) == int or type(myVariable) == float
        if len(mydata) > 0 and  (type(getattr(mydata[0], field)) == int or type(getattr(mydata[0], field)) == float):
            number_fields.append(field)


    # now write filter logic here

    # if any field is in number_fields, then it's key will be like field_from and field_to else it will be field
    # if field_from is not empty, then filter the data with field >= field_from
    # if field_to is not empty, then filter the data with field <= field_to
    # if field is not empty, then filter the data with field contains field

    for field in fields:
        if field in number_fields:
            # ignore the field if it is not in request.GET
            if field == 'dimension' and request.GET.get(field) and request.GET[field] != '0':
                mydata = [i for i in mydata if getattr(i, field) == int(request.GET[field])]
            if request.GET.get(field + '_from'):
                mydata = [i for i in mydata if getattr(i, field) >= float(request.GET[field + '_from'])]
            if request.GET.get(field + '_to'):
                mydata = [i for i in mydata if getattr(i, field) <= float(request.GET[field + '_to'])]
        else:
            if request.GET.get(field):
                mydata = [i for i in mydata if request.GET[field] in getattr(i, field)]

    data_list = []

    for i in mydata:
        data_list.append([getattr(i, field) if field != 'path' else '<a href="/download?pathname=' + getattr(i, field) + '" download><img src="/static/images/download_icon.png" alt="" width="20" height="20"></a>' for field in fields])



    context = {
      'results': data_list,
      'number_fields': number_fields,
      'fields' : fields,
      'model_names': model_names,
      'dataset_kind': request.GET['dataset-kind'],
      'selected_page': 'data_page',
    }

    return HttpResponse(template.render(context, request))
    


def send_file(request):
    pathname = request.GET['pathname']
    # print(request)
    # Create a zipfile from the pathname and send it back to the user for download
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type='application/zip')
    response['Content-Disposition'] = 'attachment; filename="download.zip"'
    
    # Create a zip file on disk
    zip_file = zipfile.ZipFile(response, 'w')

    # Add the file to the zip file with all the files in folder at the pathname
    for dirs, subdirs, files in os.walk(pathname):
        for file in files:
            zip_file.write(os.path.join(dirs, file), os.path.relpath(os.path.join(dirs, file), pathname))
    
    # Close the zip file
    zip_file.close()

    # Return the response

    return response

def docs_page(request):
    template = loader.get_template('docs_page.html')
    context = {
        'selected_page': 'docs_page',
    }
    return HttpResponse(template.render(context, request))