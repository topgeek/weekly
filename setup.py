import os
from setuptools import setup
from setuptools import find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()
CHANGES = open(os.path.join(here, 'CHANGES.rst')).read()
version = '1.0'


requires = [
        'pyramid',
        'pyramid_jinja2',
        'pyramid_assetviews',
        'waitress',
        'mailsnake'
        ]

setup(name='weekly',
      version=version,
      description='weekly',
      long_description=README + '\n\n' + CHANGES,
      author='Eric Lo',
      author_email='lxneng@gmail.com',
      url='http://lxneng.com',
      packages=find_packages('src'),
      package_dir={'': 'src'},
      namespace_packages=["weekly"],
      include_package_data=True,
      zip_safe=False,
      install_requires=requires,
      tests_require=requires,
      test_suite="weekly",
      entry_points="""\
      [paste.app_factory]
      main = weekly:main
      """,
      )
