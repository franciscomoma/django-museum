from setuptools import setup

setup(name='django-museum',
      version='0.1',
      description='Manage different picture sizes easily in your Django project.',
      url='https://github.com/franciscomoma/django-museum',
      author='Francisco Molina',
      author_email='franciscomoma@gmail.com',
      license='MIT',
      packages=['museum'],
      install_requires=[
          'Pillow==4.1.1'
      ],
      classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.10.7',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6'
      ],      
      zip_safe=False)