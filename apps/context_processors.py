from apps.models import Post, Category, Info


def custom_categories(request):
    return {
        "custom_categories": Category.objects.all()
    }


def site_info(request):
    return {
        "info": Info.objects.first()
    }


def custom_posts(request):
    return {
        "custom_posts": Post.active.order_by('-created_at')
    }
