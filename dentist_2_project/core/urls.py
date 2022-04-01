from django.urls import path, include

from dentist_2_project.core.views.appointment import build_book_appointment, build_delete_appointment
from dentist_2_project.core.views.generic import build_home
from dentist_2_project.core.views.review import build_add_review, build_edit_review, build_delete_review

urlpatterns = [
    path('', build_home, name='show index'),
    path('book-appointment/', build_book_appointment, name='show book appointment'),
    path('delete-appointment/<int:pk>', build_delete_appointment, name='show delete appointment'),
    path('add-review/', build_add_review, name='show add review'),
    path('edit-review/<int:pk>', build_edit_review, name='show edit review'),
    path('delete-review/<int:pk>', build_delete_review, name='show delete review'),

]