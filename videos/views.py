
from django.shortcuts import render, redirect
from urllib.parse import quote_plus, urlparse
from .models import Video
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

def home(request):
    videos = Video.objects.all().order_by("-id")

    site_id = request.GET.get("site", "").strip()
    query = request.GET.get("q", "").strip()

    if site_id and query:
        site = Video.objects.filter(id=site_id).first()

        if site and site.website_url:
            domain = urlparse(site.website_url).netloc.lower()
            q = quote_plus(query)

            search_patterns = {
                "youtube.com": f"https://www.youtube.com/results?search_query={q}",
                "google.com": f"https://www.google.com/search?q={q}",
                "bing.com": f"https://www.bing.com/search?q={q}",
            }

            search_url = None

            for key, url in search_patterns.items():
                if key in domain:
                    search_url = url
                    break

            if search_url:
                return redirect(search_url)

            return redirect(site.website_url)

    return render(request, "videos/home.html", {
        "videos": videos,
    })


def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
    else:
        form = UserCreationForm()

    return render(request, "registration/signup.html", {"form": form})