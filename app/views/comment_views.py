from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from app.forms import CommentForm
from app.models import Comment


@login_required
def comment_update(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('app:user_info')

    else:
        form = CommentForm(instance=comment)

    return render(request, 'app/page/comment/comment_update.html', context={
        'comment': comment,
        'form': form,
    })


@login_required
def comment_delete(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.user != comment.user:
        pass

    if request.method == "POST":
        comment.delete()
        return redirect('app:user_info')

    return render(request, 'app/page/comment/comment_delete.html', context={'comment': comment})