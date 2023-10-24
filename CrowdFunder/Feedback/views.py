from django.shortcuts import  render
from django.urls import reverse_lazy
from .forms import ReportForm
from .models import Report
from django.views import generic



def report_list(request):
    reports = Report.objects.all()
    return render(request, 'reports/reports_list.html', {'reports': reports})


class ReportProject(generic.CreateView):
    model = Report
    form_class = ReportForm
    success_url = reverse_lazy('report_list')
    template_name='reports/create.html'

    




def report_project(request):
    pass



# @login_required
# def rate_project(request, id):
#     project = get_object_or_404(Project, id=id)
