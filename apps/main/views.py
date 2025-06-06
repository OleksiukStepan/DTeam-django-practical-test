import tempfile
from datetime import datetime

from django.contrib import messages
from django.http import FileResponse
from django.shortcuts import get_object_or_404, redirect
from django.utils.text import slugify
from django.views.decorators.http import require_POST
from django.views.generic import ListView, DetailView
from openai import OpenAIError
from rest_framework.viewsets import ModelViewSet

from apps.main.models import CV
from apps.main.serializers import CVSerializer
from apps.main.send_pdf_email_task import send_cv_pdf_email_task
from utils.html_to_pdf import generate_pdf
from utils.languages import TRANSLATION_LANGUAGES
from utils.text_from_cv import serialize_cv_for_translation
from utils.translate import translate_text


def export_cv_pdf(request, pk):
    cv = get_object_or_404(CV, pk=pk)
    context = {"cv": cv}
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M")

    filename = f"{timestamp}_{slugify(cv.firstname)}_{slugify(cv.lastname)}.pdf"

    with tempfile.NamedTemporaryFile(suffix=".pdf", delete=False) as tmpfile:
        generate_pdf("main/cv_detail.html", context, tmpfile.name)

        response = FileResponse(
            open(tmpfile.name, "rb"),
            content_type="application/pdf"
        )
        response["Content-Disposition"] = f'attachment; filename="{filename}"'
        return response


def send_cv_pdf_view(request, pk):
    if request.method == "POST":
        email = request.POST.get("email")
        if email:
            send_cv_pdf_email_task.delay(pk, email)
            messages.success(
                request,
                "CV PDF was successfully sent to your email"
            )
    return redirect("main:cv_detail", pk=pk)


@require_POST
def translate_cv_view(request, pk):
    cv = get_object_or_404(CV, pk=pk)
    lang = request.POST.get("language")

    if lang:
        try:
            full_text = serialize_cv_for_translation(cv)
            translated_text = translate_text(full_text, lang)
            request.session["translated_cv"] = translated_text
            messages.success(request, f"Translated into {lang}!")
        except OpenAIError:
            messages.error(request, f"Translation failed")
    else:
        messages.error(request, "No language selected.")

    return redirect("main:cv_detail", pk=pk)


class CVListView(ListView):
    model = CV
    template_name = "main/cv_list.html"
    context_object_name = "cv_list"
    queryset = CV.objects.select_related("contacts").prefetch_related(
        "skills", "projects"
    )


class CVDetailView(DetailView):
    model = CV
    template_name = "main/cv_detail.html"
    context_object_name = "cv"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        translated = self.request.session.pop("translated_cv", None)
        context["translated_cv"] = translated
        context["languages"] = TRANSLATION_LANGUAGES
        return context


class CVViewSet(ModelViewSet):
    queryset = CV.objects.all()
    serializer_class = CVSerializer

