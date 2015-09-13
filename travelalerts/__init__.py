"""
Plugin definition for the travelalerts OPAL plugin
"""
from opal.core import plugins

from travelalerts.urls import urlpatterns

class TravelalertsPlugin(plugins.OpalPlugin):
    """
    Main entrypoint to expose this plugin to our OPAL application.
    """
    urls = urlpatterns
    javascripts = {
        'opal.controllers': [
            'js/travelalerts/controllers/travel_alerts.js'            
        ],
        # Add your javascripts here!
        'opal.travelalerts': [
            # 'js/travelalerts/app.js',
            # 'js/travelalerts/controllers/larry.js',
            # 'js/travelalerts/services/larry.js',
        ]
    }

    def restricted_teams(self, user):
        """
        Return any restricted teams for particualr users that our
        plugin may define.
        """
        return []

    def list_schemas(self):
        """
        Return any patient list schemas that our plugin may define.
        """
        return {}

    def flows(self):
        """
        Return any custom flows that our plugin may define
        """
        return {}

    def roles(self, user):
        """
        Given a (Django) USER object, return any extra roles defined
        by our plugin.
        """
        return {}


plugins.register(TravelalertsPlugin)
