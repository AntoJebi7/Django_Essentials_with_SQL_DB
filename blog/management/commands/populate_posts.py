# demo data,  to generate , we need important library for post's data - pip install faker

from typing import Any
from blog.models import Post,Category
import random
from django.core.management.base import BaseCommand
    # to run with command




class Command(BaseCommand):
    help = "This command inserts post data"

    def handle(self, *args: Any, **options: Any) :
        #delete existing data
        Post.objects.all().delete()

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
    "In today’s fast-paced world, mastering the art of scheduling is essential for maximizing productivity and achieving personal and professional goals. To optimize your daily schedule, start by assessing how you currently spend your time. Conduct a time audit by tracking your activities for a week to identify patterns and time drains. Categorize your tasks into urgent, important, and less critical activities to prioritize tasks that align with your long-term objectives. Techniques like the Pomodoro Technique, which involves working in focused intervals of 25 minutes followed by short breaks, can help maintain concentration and prevent burnout. Time blocking, where you allocate specific periods for different activities throughout the day, is another effective method. Utilize digital tools like calendar apps and task management software to organize and monitor your schedule efficiently. Setting clear, achievable goals for each day and regularly reviewing your progress enhances productivity. Incorporating habits such as planning your day the night before and starting your morning with a routine that energizes you can set a positive tone for the day. Remember, optimizing your schedule is not just about working harder but working smarter and making the most of your time.",
    
    "The technological landscape is evolving rapidly, with several emerging technologies significantly reshaping various industries. Artificial Intelligence (AI) is at the forefront of this transformation, driving innovations across fields such as healthcare and finance. AI algorithms analyze vast amounts of data, leading to more accurate medical diagnoses and personalized treatments. In finance, AI tools enhance fraud detection and automate trading processes, making financial systems more efficient. Blockchain technology, known for its decentralized and transparent nature, is improving supply chain management by enhancing traceability and reducing fraud. The Internet of Things (IoT) is revolutionizing manufacturing with real-time monitoring and predictive maintenance, resulting in more efficient operations. Quantum computing promises breakthroughs in solving complex problems beyond classical computers’ reach, impacting cryptography and material science. As these technologies continue to advance, they create new opportunities while challenging existing business models and industry practices.",
    
    "Staying productive in a world filled with distractions requires strategic planning and effective tools. Start by setting clear, actionable goals and breaking them down into manageable tasks. Creating a detailed plan and establishing a daily routine can provide structure and focus. Productivity techniques like the Eisenhower Matrix help prioritize tasks based on urgency and importance. Utilize productivity tools such as to-do lists, project management software, and time-tracking apps to stay organized and on track. Minimize distractions by identifying and mitigating common interruptions. For example, schedule specific times for checking emails and social media rather than allowing these activities to disrupt your workflow. Incorporate regular breaks into your routine using methods like the Pomodoro Technique to maintain high levels of productivity. Regularly reviewing your goals and progress can help adjust your strategies and stay aligned with your objectives. By implementing these tips and tools, you can enhance your productivity and make the most of your time.",
    
    "The realm of health and wellness is continually evolving with new trends that are transforming our approach to self-care. Emerging health trends include advancements in personalized medicine, which tailors treatments based on individual genetic profiles, leading to more effective and targeted interventions. Wearable technology, such as fitness trackers and smartwatches, provides real-time health monitoring, enabling individuals to track their physical activity, sleep patterns, and vital signs. Additionally, the rise of mental health awareness has led to a greater focus on holistic approaches, including mindfulness and stress management techniques. Integrative medicine combines conventional treatments with alternative therapies, promoting a more comprehensive approach to health. The growing interest in plant-based diets and sustainable nutrition reflects a shift towards healthier eating habits that benefit both personal health and the environment. Moreover, telemedicine is revolutionizing healthcare delivery by providing remote consultations and reducing barriers to access. Staying informed about these emerging trends allows individuals to adopt proactive and innovative approaches to wellness and self-care.",
    
    "Artificial Intelligence (AI) is rapidly advancing, presenting both exciting possibilities and complex ethical considerations. The potential of AI spans numerous applications, including autonomous vehicles, intelligent virtual assistants, and advanced data analytics. These innovations promise to enhance efficiency, safety, and convenience in various aspects of daily life. For instance, AI-driven systems in autonomous vehicles aim to reduce traffic accidents and improve transportation efficiency. However, the advancement of AI also raises significant ethical concerns. Issues such as data privacy, algorithmic bias, and the potential for job displacement need to be addressed. Ensuring that AI systems are transparent and unbiased is crucial to prevent discrimination and unfair practices. Additionally, the development of AI must be accompanied by robust data protection measures to safeguard personal information. As AI technology continues to evolve, it is essential for policymakers, technologists, and ethicists to collaborate in creating guidelines and regulations that balance innovation with ethical considerations, ensuring that AI contributes positively to society while mitigating potential risks.",
    
    "Mindfulness practices have gained recognition for their ability to cultivate a deeper sense of peace and clarity in everyday life. Mindfulness involves focusing on the present moment with an attitude of non-judgment and acceptance. Techniques such as mindful breathing, meditation, and body scans help individuals develop greater awareness of their thoughts, emotions, and physical sensations. Regular mindfulness practice can reduce stress, enhance emotional regulation, and improve overall well-being. To incorporate mindfulness into daily life, start with simple practices like setting aside a few minutes each day for meditation or mindful breathing exercises. Engaging in mindful activities, such as eating or walking, with full attention to the experience can also enhance mindfulness. Mindfulness-based stress reduction (MBSR) and mindfulness-based cognitive therapy (MBCT) are structured programs that offer comprehensive approaches to integrating mindfulness into daily routines. By embracing mindfulness, individuals can cultivate a greater sense of inner calm and clarity, contributing to improved mental and emotional health.",
    
    "For those seeking thrill and adventure, there are numerous travel destinations that offer unparalleled experiences. From the rugged landscapes of Patagonia to the vibrant streets of Tokyo, these destinations cater to a wide range of adventurous pursuits. Patagonia, located in the southern regions of Chile and Argentina, is renowned for its dramatic scenery, including glaciers, mountains, and pristine lakes. Activities such as trekking, glacier hiking, and wildlife spotting provide thrilling experiences for outdoor enthusiasts. Tokyo, Japan’s bustling capital, offers a mix of modern excitement and traditional culture. Visitors can explore futuristic technology, enjoy world-class cuisine, and immerse themselves in the city's vibrant nightlife. For a more extreme adventure, consider bungee jumping in New Zealand or exploring the depths of the Great Barrier Reef in Australia. Each destination provides unique challenges and unforgettable memories for those with a taste for adventure. Whether you’re seeking natural wonders, cultural experiences, or adrenaline-pumping activities, these travel destinations offer exceptional opportunities for thrill-seekers.",
    
    "Creating and growing a profitable online business involves several key steps, from idea generation to marketing strategies. Begin by identifying a niche or market need that aligns with your interests and expertise. Conduct thorough market research to validate your idea and understand your target audience. Once you have a clear concept, create a business plan outlining your objectives, target market, value proposition, and revenue model. Developing a strong online presence is crucial, so build a professional website and establish a presence on relevant social media platforms. Utilize search engine optimization (SEO) techniques to enhance your website’s visibility and attract organic traffic. Implement digital marketing strategies such as content marketing, email campaigns, and pay-per-click (PPC) advertising to reach potential customers. Monitor your performance through analytics tools and adjust your strategies based on data-driven insights. Additionally, focus on providing excellent customer service and continuously improving your products or services. By following these steps and staying adaptable to market changes, you can build a successful and profitable online business.",
    
    "The relationship between social media usage and mental health is complex and multifaceted. On one hand, social media platforms can provide valuable connections, support networks, and access to information. They allow individuals to stay in touch with friends and family, share experiences, and find communities with similar interests. However, excessive or negative use of social media can have detrimental effects on mental health. Studies have shown that frequent social media use is associated with increased feelings of anxiety, depression, and loneliness. The constant exposure to curated and idealized portrayals of others' lives can lead to social comparison and diminished self-esteem. Additionally, cyberbullying and online harassment are significant concerns that impact mental well-being. To navigate social media mindfully, set boundaries for usage, curate your feed to include positive and uplifting content, and take regular breaks from screens. Engaging in offline activities and seeking professional support when needed can also help maintain a healthy balance between social media and mental health.",
    
    "Living a greener life in the city involves adopting sustainable practices that minimize environmental impact while maintaining convenience and comfort. Start by making eco-friendly choices in your daily routines, such as reducing energy consumption by using energy-efficient appliances and lighting. Opt for public transportation, biking, or walking instead of driving to reduce your carbon footprint. Implementing waste reduction strategies, such as recycling and composting, helps manage waste effectively and minimize landfill contributions. Choose sustainable products and support local businesses that prioritize environmentally friendly practices. Urban gardening is another way to contribute to sustainability; growing herbs and vegetables in small spaces or community gardens can reduce food miles and enhance your connection to nature. Additionally, consider participating in community initiatives and advocacy for green policies that promote sustainability in your city. By integrating these practices into your daily life, you can contribute to a more sustainable urban environment without sacrificing convenience or comfort."
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


        categories = Category.objects.all()
        for title, content , img_url in zip(titles,contents,img_urls):
            category = random.choice(categories)
            Post.objects.create(title=title,content = content,img_url=img_url, category=category)


        self.stdout.write(self.style.SUCCESS("Completed Inserting Data"))