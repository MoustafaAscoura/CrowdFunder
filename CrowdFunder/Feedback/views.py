from django.shortcuts import  render, redirect
from django.urls import reverse_lazy
from .forms import ReportForm, ReviewForm
from .models import Report, Review
from projects.models import Project
from django.views import generic



def report_list(request):
    reports = Report.objects.all()
    return render(request, 'reports/reports_list.html', {'reports': reports})


class ReportProject(generic.CreateView):
    model = Report
    form_class = ReportForm
    success_url = reverse_lazy('report_list')
    template_name='reports/create.html'

    


def report_project(request, pk):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            project = Project.objects.get(id=pk)
            review.project = project
            review.user = request.user
            review.save()
            return redirect('project_detail', id=pk)
    else:
        form = ReviewForm()
    return render(request, 'feedback/create_review.html', {'form': form})

    



# def report_project(request):
#     pass

# @login_required
# def rate_project(request, id):
#     project = get_object_or_404(Project, id=id)
