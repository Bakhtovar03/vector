from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from content.models import Course, Teacher


class CourseSitemap(Sitemap):
    changefreq = "weekly"

    def items(self):
        return Course.objects.all()

    def lastmod(self, obj):
        return obj.updated_at

    def location(self, obj):
        return reverse('course_detail', args=[obj.slug])

    def priority(self, obj):
        return 0.8


class TeachersSitemap(Sitemap):
    changefreq = "monthly"

    def items(self):
        return Teacher.objects.all()

    def lastmod(self, obj):
        return obj.updated_at

    def location(self, obj):
        return reverse('teacher_list')

    def priority(self, obj):
        return 0.6



sitemaps = {
    'courses': CourseSitemap,
    'teachers': TeachersSitemap,
}