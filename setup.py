from setuptools import setup

setup(
    name='MyApp',
    version='1.0.0',
    packages=['MyApp'],
    url='http://www.example.com/MyApp/',
    license='MIT',
    author='John Doe',
    author_email='john.doe@example.com',
    description='My App is an awesome app',
    install_requires=[
        'pywin32'
    ],
    entry_points={
        'console_scripts': [
            'myapp = MyApp.__main__:main'
        ]
    },
    options={
        'build_exe': {
            'include_files':
            [
                'MyApp/',
                'MyApp/__main__.py',
                'MyApp/myapp.py'
            ],
            'include_msvcr': True,
            'excludes': [
                'tkinter',
            ],
            'packages': [
                'MyApp',
            ],
            'include_msvcr': True,
            'compressed': True,
            'optimize': 2,
            'create_shared_zip': False,
            'append_script_to_exe': True,
            'append_script_to_library': True,
            'icon': 'MyApp/myapp.ico',
            'target_name': 'MyApp'
        }
    }
)