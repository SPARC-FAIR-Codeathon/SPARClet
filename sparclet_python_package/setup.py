from distutils.core import setup
setup(
  name = 'sparclet',         # How you named your package folder (MyLib)
  packages = ['sparclet'],   # Chose the same as "name"
  version = '0.31',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Leaflet Interactions with Flatmaps from SPARC',   # Give a short description about your library
  author = 'Archit Bhatnagar',                   # Type in your name
  author_email = 'archibhatnagar27@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/SPARC-FAIR-Codeathon/2022-project-4',   # Provide either the link to your github or to your website
  install_requires=[            # I get to this in a second
          'ipyleaflet',
          'bs4',
          'requests',
          'shapely'
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      
    'License :: OSI Approved :: MIT License',   
    'Programming Language :: Python :: 3',      
  ],
  include_package_data=True
)