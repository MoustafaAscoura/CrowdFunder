from django.shortcuts import  render, redirect
from django.urls import reverse_lazy
from .forms import ReportForm, ReviewForm, CommentForm
from .models import Report, Review, Comment
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



def report_comment(request, comment_id):
    if request.method == 'POST':
        form = ReportForm(request.POST)
        if form.is_valid():
            comment = Comment.objects.get(pk=comment_id)
            report = form.save(commit=False)
            report.comment = comment
            report.user = request.user
            report.save()
            return redirect('project_detail', pk=comment.project.id)
    else:
        form = ReportForm()
    return render(request, 'feedback/report_comment.html', {'form': form})



def create_review(request, pk):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            project = Project.objects.get(id=pk)
            review.project = project
            review.user = request.user
            review.save()
            return redirect('project_detail', pk=pk)
    else:
        form = ReviewForm()
    return render(request, 'feedback/create_review.html', {'form': form})

    
def create_comment( request , pk ):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
                comment = form.save(commit=False)
                project = Project.objects.get(id=pk)
                comment.project = project
                comment.user = request.user
                comment.save()
                return redirect('project_detail', pk=pk )
    else:
           form = CommentForm()
    return render(request, 'feedback/create_comment' , { 'form' : form } )


# @login_required
# def rate_project(request, id):
#     project = get_object_or_404(Project, id=id)

# def create_report(request, comment_pk):
#       if request.method == 'POST':
#         form = ReportForm(request.POST)
#         if form.is_valid():
#                 reason = form.save(commit=False)
#                 comment = Comment.objects.get(pk=comment_pk)
#                 reason.comment = comment
#                 reason.user = request.user
#                 reason.project = comment.project
#                 reason.save()
#                 return redirect('project_detail', pk=comment.project.pk )
#       else:
#            form = CommentForm()
#       return render(request, 'reports/create.html' , { 'form' : form } )



 