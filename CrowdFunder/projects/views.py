from django.http import HttpResponse
from django.shortcuts import render ,get_object_or_404,redirect
from . models import Project , Category
from . forms import ProjectForm , CategoryForm
from django.contrib.auth.decorators import login_required


def project_list(request):
    projects = Project.objects.all()
    return render(request, 'projects/project_list.html', {'projects': projects})

def project_detail(request, id):
    project = get_object_or_404(Project, id=id)
    return render(request, 'projects/project_detail.html', {'project': project})


@login_required
def delete(request, id):
    project = get_object_or_404(Project, id=id)
    
    if project.user != request.user:
        return HttpResponse("You are not authorized to delete this project.")
    if project:
        project.delete()
        # print(request.user,'I am delete function in views.py')
        return redirect('project_list')
    else:
        return HttpResponse("Sorry, project not found")   

@login_required
def create_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            if Project.objects.filter(title=form.cleaned_data['title']).exists():
                form.add_error('title', 'A project with this name already exists.')
            else:
            # Save the form data to create a new Project object
                project = Project(
                    title=form.cleaned_data['title'],
                    details=form.cleaned_data['details'],
                    total_target=form.cleaned_data['total_target'],
                    start_time=form.cleaned_data['start_time'],
                    end_time=form.cleaned_data['end_time'],
                    category=form.cleaned_data['category'],
                    user=request.user
                )
                project.save()
                return redirect('project_list')
    else:
        form = ProjectForm()

    context = {
        'form': form
    }
    return render(request, 'projects/create/create.html', context)

@login_required
def edit_project(request, id):
    project = get_object_or_404(Project, id=id)
    
    # Check if the current user is the owner of the gun
    if project.user != request.user:
        return HttpResponse("You are not authorized to edit this project.")

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project.title = form.cleaned_data['title']
            project.details = form.cleaned_data['details']
            project.total_target = form.cleaned_data['total_target']
            project.start_time = form.cleaned_data['start_time']
            project.end_time = form.cleaned_data['end_time']
            project.category = form.cleaned_data['category']

            # Check if a new image is provided
            # if 'image' in request.FILES:
            #     project.image = form.cleaned_data['image']
            project.save()
            return redirect('project_list')
    else:
        form = ProjectForm({
            'title': project.title,
            'details': project.details,
            'total_target': project.total_target,
            'start_time': project.start_time,
            'end_time': project.end_time,
            'category': project.category,
            }
        )

    context = {
        'form': form
    }
    return render(request, 'projects/create/edit.html', context)




def category_list(request):
    categories = Category.objects.all()
    return render(request, 'categories/category_list.html', {'categories': categories})

def category_detail(request, category):
    projects = Project.objects.filter(category__name=category)
    context = {
        'projects': projects,
        'category': category
    }
    return render(request, 'categories/category_detail.html', context)
    

@login_required
def create_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES)
        if form.is_valid():
            if Category.objects.filter(name=form.cleaned_data['name']).exists():
                form.add_error('name', 'A category with this name already exists.')
            else:
            # Save the form data to create a new Category object
                category = Category(
                    name=form.cleaned_data['name'],
                )
                category.save()
                return redirect('category.list')
    else:
        form = CategoryForm()

    context = {
        'form': form
    }
    return render(request, 'categories/create/create.html', context)
