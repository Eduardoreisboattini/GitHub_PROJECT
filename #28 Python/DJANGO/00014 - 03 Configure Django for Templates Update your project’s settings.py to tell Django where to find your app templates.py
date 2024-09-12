# settings
#. Set Up a Django Project:
# First, create a new Django project and app
#
# 2 Install Bootstrap:
# Option 1: Add Bootstrap via CDN (Content Delivery Network).
# Option 2: Download Bootstrap and link it in your templates.
# Option 1: Using Bootstrap via CDN
# In this case, you can simply link to the Bootstrap CDN in your Django HTML templates.
#
# 3. Configure Django for Templates:
# Update your project’s settings.py to tell Django where to find your app templates.

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # Custom templates directory
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

