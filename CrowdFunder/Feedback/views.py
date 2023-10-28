from django.shortcuts import  render, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q

from .forms import *
from .models import Report, Review, Comment
from projects.models import Project

class Reports(generic.ListView):
    model = Report
    context_object_name = 'reports'
    template_name = 'reports/reports_list.html'

class ReportProject(LoginRequiredMixin, generic.CreateView):
    model = Report
    form_class = ReportForm
    success_url = reverse_lazy('report_list')
    template_name='reports/create.html'

def report_comment(request, comment_id, pk):
    if request.method == 'POST':
        form = ReportForm(request.POST)
        if form.is_valid():
            comment = Comment.objects.get(id=comment_id)
            project = Project.objects.get(id=pk)
            report = form.save(commit=False)
            report.comment = comment
            report.project = project
            report.user = request.user
            report.save()
            return redirect('project_detail', pk=pk )
    else:
        form = ReportForm()
    return render(request, 'reports/report_comment.html', {'form': form})

@login_required
def create_review(request, pk):
    project = Project.objects.get(id=pk)
    if request.method == "POST":
        #Check if user has already review project
        old_review = Review.objects.filter(Q(user=request.user) & Q(project=project))
        if old_review.exists():
            form = ReviewForm(request.POST, instance=old_review.first())
        else:
            form = ReviewForm(request.POST)

        if form.is_valid():
            review = form.save(commit=False)
            review.project = project
            review.user = request.user
            review.save()

    return redirect(reverse_lazy('project_detail', kwargs={'pk': pk}))

@login_required
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
    
    return redirect(reverse_lazy('project_detail', kwargs={'pk': pk}))

@login_required
def create_reply( request , comment_id):
    comment = Comment.objects.get(id=comment_id)
    print(comment,'aaaa')
    if request.method == 'POST':
        form = ReplyForm(request.POST)
        print(form,'ccccc')
        if form.is_valid():
            reply = form.save(commit=False)
            reply.comment = comment
            reply.user = request.user
            reply.save()
            print(reply,'bbb')
    
    return redirect(reverse_lazy('project_detail', kwargs={'pk': comment.project.id}))

