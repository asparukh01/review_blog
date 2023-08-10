from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .forms import ReviewForm, UpdateForm
from .models import Review
from django.core.paginator import Paginator
# Create your views here.

class ReviewListView(View):
    template_name = 'review/review_list.html'

    def get(self, request, *args, **kwargs):
        review = Review.objects.filter(status='Принят').order_by('-created_at')
        paginator = Paginator(review, 12)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, self.template_name, {'page_obj': page_obj})
    

class RejectedListView(View):
    template_name = 'review/rejected.html'

    def get(self, request, *args, **kwargs):
        review = Review.objects.filter(status='Отклонен').order_by('-created_at')
        paginator = Paginator(review, 12)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, self.template_name, {'page_obj': page_obj})
    

class ReviewCreateView(LoginRequiredMixin, View):
    template_name = 'review/review_list.html'

    def get(self, request, *args, **kwargs):
        form = ReviewForm()
        statuses = Review.STATUSES
        return render(request, self.template_name, {'form': form, 'statuses': statuses})

    def post(self, request, *args, **kwargs):
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            review = form.save(commit=False)
            review.author = self.request.user
            review.save()
            return redirect('review_list')
        return render(request, self.template_name, {'form': form})
    

class ReviewUpdateView(LoginRequiredMixin, View):
    template_name = 'review/review_update.html'

    def get(self, request, *args, **kwargs):
        review = get_object_or_404(Review, pk=kwargs.get('pk'))
        statuses = Review.STATUSES
        form = UpdateForm(
            initial={
                'name': review.name,
                'email': review.email,
                'status': review.status,
                'text': review.text,

            }
        )
        return render(request, self.template_name, {'review': review, 'form': form, 'statuses': statuses})

    def post(self, request, *args, **kwargs):
        form = UpdateForm(request.POST)
        review = get_object_or_404(Review, pk=kwargs.get('pk'))
        statuses = Review.STATUSES
        if form.is_valid():
            review.name = request.POST.get('name')
            review.email = request.POST.get('email')
            review.status = request.POST.get('status')
            review.text = request.POST.get('text')
            review.save(update_fields=['name', 'text', 'status', 'email'])
            return redirect('review_list')
        return render(request, self.template_name, {
            'form': ReviewForm(
                initial={
                    'name': review.name,
                    'email': review.email,
                    'status': review.status,
                    'text': review.text,
                }),
            'review': review, 'statuses': statuses})
    

class ReviewDetailView(View):
    template_name = 'review/review_detail.html'

    def get(self, request, *args, **kwargs):
        review = get_object_or_404(Review, pk=self.kwargs.get('pk'))
        return render(request, self.template_name, {'review': review})
    


class ReviewDeleteView(LoginRequiredMixin, View):
    template_name = 'review/review_delete.html'

    def post(self, request, *args, **kwargs):
        review = get_object_or_404(Review, pk=kwargs.get('pk'))
        review.delete()
        return redirect('review_list')