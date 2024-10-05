DEFAULT_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
PROJECT_APPS = [
    'apps.blog.apps.BlogConfig',
    'apps.portfolio.apps.PortfolioConfig',
    'apps.resume.apps.ResumeConfig',
    'apps.shared.apps.SharedConfig',
    'apps.bot.apps.BotConfig',
    'apps.users.apps.UsersConfig',
]
THIRD_PARTY_APPS = [
    "rest_framework",
]
