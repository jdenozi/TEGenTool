from setuptools import setup
setup(name = 'TEGenTool',
      version = '0.0.1',
      description = 'Outil de visualisation de la dynamique des éléments transposables sur plusieurs générations',
      author = 'Julien DENOZI, ISEM',
      author_email = 'denozi.j@gmail.com',
      maintainer = 'Julien DENOZI',
      maintainer_email = ' denozi.j@gmail.com',
      url = 'https://github.com/jdenozi/TEGenTool',
      download_url = 'https://github.com/jdenozi/TEGenTool',
      packages = {'' : 'src'},
      plateformes = 'LINUX', 
      install_requires = ['pandas<=0.24.2', 'numpy<=1.16.2'])
