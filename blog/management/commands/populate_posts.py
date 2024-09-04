# demo data,  to generate , we need important library for post's data

from typing import Any
from blog.models import Post
from django.core.management.base import BaseCommand


    # to run with command




class Command(BaseCommand):
    help = "This command inserts post data"

    def handle(self, *args: Any, **options: Any) :
        titles = [
    "The Ultimate Guide to Mastering Time Management",
    "10 Hidden Gems in Modern Technology",
    "How to Boost Your Productivity in 2024",
    "Top 5 Health Trends You Need to Know About",
    "Exploring the Future of Artificial Intelligence",
    "The Art of Mindful Living: A Beginner's Guide",
    "10 Must-Visit Travel Destinations for Adventure Seekers",
    "How to Start a Successful Online Business from Scratch",
    "The Impact of Social Media on Mental Health",
    "Essential Tips for Sustainable Living in Urban Areas"
]

        contents = [
    "Learn proven techniques and strategies to optimize your daily schedule, improve focus, and achieve more with less effort.",
    "Discover lesser-known yet powerful technologies that are reshaping industries and changing the way we live.",
    "Explore actionable tips and tools to help you stay productive and make the most out of your time in the upcoming year.",
    "Stay ahead of the curve with these emerging health trends that are transforming the way we approach wellness and self-care.",
    "Delve into the exciting possibilities and ethical considerations surrounding the advancements in AI technology.",
    "An introduction to mindfulness practices that can help you cultivate a deeper sense of peace and clarity in everyday life.",
    "For those seeking thrill and adventure, these travel destinations offer unparalleled experiences that will leave you breathless.",
    "Step-by-step guidance on how to create and grow a profitable online business, from idea generation to marketing strategies.",
    "Examine the complex relationship between social media usage and mental health, and learn how to navigate the digital world mindfully.",
    "Practical advice and sustainable practices for living a greener life in the city, without sacrificing convenience or comfort.",
    "test content"
]

        img_urls = [
    "https://picsum.photos/id/237/800/400",
    "https://picsum.photos/id/238/800/400",
    "https://picsum.photos/id/239/800/400",
    "https://picsum.photos/id/240/800/400",
    "https://picsum.photos/id/241/800/400",
    "https://picsum.photos/id/242/800/400",
    "https://picsum.photos/id/243/800/400",
    "https://picsum.photos/id/244/800/400",
    "https://picsum.photos/id/245/800/400",
    "https://picsum.photos/id/246/800/400"
]

        for title, content , img_url in zip(titles,contents,img_urls):
            Post.objects.create(title=title,content = content,img_url=img_url)


        self.stdout.write(self.style.SUCCESS("Completed Inserting Data"))