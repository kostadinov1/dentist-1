from django.shortcuts import render, redirect

from dentist_2_project.core.forms import ReviewForm, EditReviewForm, DeleteReviewForm
from dentist_2_project.core.models import Review


def build_add_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.save()
            return redirect('show profile view')

    else:
        form = ReviewForm()

    context = {
        'form': form
    }

    return render(request, 'core/review-add.html', context)


def build_edit_review(request, pk):
    rev = Review.objects.get(pk=pk)
    if request.method == 'POST':
        form = EditReviewForm(request.POST, instance=rev)
        if form.is_valid():
            form.save()
            return redirect('show profile view')

    else:
        form = EditReviewForm(instance=rev)

    context = {
        'form': form,
        'rev': rev
    }

    return render(request, 'core/review-edit.html', context)


def build_delete_review(request, pk):
    rev = Review.objects.get(pk=pk)
    if request.method == 'POST':
        form = DeleteReviewForm(request.POST, instance=rev)
        if form.is_valid():
            form.save()
            return redirect('show profile view')

    else:
        form = DeleteReviewForm(instance=rev)

    context = {
        'form': form,
        'rev': rev
    }

    return render(request, 'core/review-delete.html', context)