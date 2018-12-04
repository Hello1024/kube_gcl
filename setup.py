from setuptools import setup, find_packages 

setup(name='kube_gcl',
      version='0.1.1',
      description='Kube GCL lets you write simple easy configs to autogenerate kubernetes yaml configs.',
      url='https://https://github.com/Hello1024/kube_gcl',
      author='Oliver Mattos',
      author_email='omattos@gmail.com',
      license='MIT',
      zip_safe=False,


      entry_points = {
        'console_scripts' : [
            'kube_gcl=kube_gcl.kube_gcl:main',
        ],
	},

	# See https://pypi.python.org/pypi?%3Aaction=list_classifiers
	classifiers=[
	    # How mature is this project? Common values are
	    #   3 - Alpha
	    #   4 - Beta
	    #   5 - Production/Stable
	    'Development Status :: 3 - Alpha',

	    # Indicate who your project is intended for
	    'Intended Audience :: Developers',
	    
	    # Pick your license as you wish (should match "license" above)
	    'License :: OSI Approved :: MIT License',

	    # Specify the Python versions you support here. In particular, ensure
	    # that you indicate whether you support Python 2, Python 3 or both.
	    'Programming Language :: Python :: 2',
	    'Programming Language :: Python :: 2.6',
	    'Programming Language :: Python :: 2.7',
	    'Programming Language :: Python :: 3',
	    'Programming Language :: Python :: 3.2',
	    'Programming Language :: Python :: 3.3',
	    'Programming Language :: Python :: 3.4',
	],

	# What does your project relate to?
	keywords='configuration',

	# You can just specify the packages manually here if your project is
	# simple. Or you can use find_packages().
	packages=find_packages(exclude=['contrib', 'docs', 'tests*']),

	# List run-time dependencies here.  These will be installed by pip when your
	# project is installed. For an analysis of "install_requires" vs pip's
	# requirements files see:
	# https://packaging.python.org/en/latest/requirements.html
	install_requires=['gcl>=0.6.10'],
  )