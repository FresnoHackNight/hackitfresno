from .common import *

DEBUG = TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['localhost']

DJANGO_DEBUG_TOOLBAR = True
if DJANGO_DEBUG_TOOLBAR:
    INSTALLED_APPS.append('debug_toolbar')
    MIDDLEWARE_CLASSES.insert(0, 'debug_toolbar.middleware.DebugToolbarMiddleware')

    DEBUG_TOOLBAR_CONFIG = {
        # 'SHOW_TOOLBAR_CALLBACK': lambda request: True  # request.user.is_superuser
    }

    DEBUG_TOOLBAR_PANELS = (
        'debug_toolbar.panels.versions.VersionsPanel',
        'debug_toolbar.panels.timer.TimerPanel',
        'debug_toolbar.panels.settings.SettingsPanel',
        'debug_toolbar.panels.headers.HeadersPanel',
        'debug_toolbar.panels.request.RequestPanel',
        # 'debug_toolbar.panels.sql.SQLPanel',
        'debug_toolbar.panels.staticfiles.StaticFilesPanel',
        'debug_toolbar.panels.templates.TemplatesPanel',
        'debug_toolbar.panels.cache.CachePanel',
        'debug_toolbar.panels.signals.SignalsPanel',
        'debug_toolbar.panels.logging.LoggingPanel',
        # 'debug_toolbar.panels.redirects.RedirectsPanel',
    )
