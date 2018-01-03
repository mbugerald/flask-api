# Imports
from app.api.route import (api, SiteViews)
from app import Application


class BlueprintSiteRunner(Application):

    def __int__(self, app, db, ma, csrf):
        super().__init__()

    # Registering site views to site blue print.
    def register_views_to_site_blueprint(self):
        # Application views register to sites
        SiteViews.register(api)

    # Launching all the site components
    def siteApplicationLauncher(self):
        self.register_views_to_site_blueprint()


# Initializing site blueprint.
BlueprintSiteRunner().siteApplicationLauncher()