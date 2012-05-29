__import__('pkg_resources').declare_namespace(__name__)


class ApplicationFactory(object):
    def create_configuration(self, settings):
        from pyramid.config import Configurator
        config = Configurator(settings=settings)
        return config

    def setup_jinja2(self, config):
        from pyramid_jinja2 import renderer_factory
        config.add_renderer('.html', renderer_factory)

    def setup_routes(self, config, settings):
        config.add_static_view('static', 'weekly:static', cache_max_age=3600)
        config.add_route('index', '/')
        config.add_route('subscribe', '/subscribe')
        config.add_route('thankyou', '/thankyou')

    def setup_assetviews(self, config):
        config.include('pyramid_assetviews')
        config.add_asset_views('weekly:static', filenames=['robots.txt',
            'favicon.ico'], http_cache=5000)

    def setup_mailchimp(self, config, settings):
        from mailsnake import MailSnake
        config.registry['mc'] = MailSnake(settings.get('mailchimp_key'))

    def configure(self, settings):
        config = self.create_configuration(settings)
        self.setup_jinja2(config)
        self.setup_routes(config, settings)
        self.setup_mailchimp(config, settings)
        self.setup_assetviews(config)
        config.scan()
        return config

    def __call__(self, global_config, **settings):
        config = self.configure(settings)
        app = config.make_wsgi_app()
        return app


app_factory = ApplicationFactory()


def main(global_config, **settings):
    return app_factory(global_config, **settings)
