from setuptools import setup


def readme(text=''):
    with open('README.rst', 'r') as f:
        for line in f:
            if '---' in line or '~~~' in line:
                line = line.replace('-', '=')
                line = line.replace('~', '=')
            text += line
        return text


setup(
    name='usajobs',
    packages=['usajobs'],
    version='0.1.0',
    description='Lightweight wrapper for the usajobs.gov api.',
    long_description=readme(),
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    author='brennv',
    author_email='brennan@beta.build',
    license='MIT',
    url='https://github.com/brennv/usajobs',
    download_url='https://github.com/brennv/usajobs/tarball/0.1.0',
    keywords='usajobs usajobs.gov api',
    install_requires=[
        'nametupled',
        'requests',
    ],
    include_package_data=True,
    zip_safe=False)
