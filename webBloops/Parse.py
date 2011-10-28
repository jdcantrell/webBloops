'''This is the collection of functions needed to generate the site'''
from jinja2 import Template, Environment, FileSystemLoader
import MusicFolder
import Config
import os
import shutil

config = Config.Config()

env = Environment(loader=FileSystemLoader(config.TEMPLATE_PATH))

def create_file_pages(path, musicFolder):
  web_folder = path.replace(config.BASE_FOLDER, config.WEB_ROOT)

  if web_folder[len(web_folder) - 1] != '/':
    web_folder += '/'

  try:
    os.makedirs(web_folder)
  except OSError:
    pass

  #create navigation html
  template = env.get_template('album_view.html')
  file_name = web_folder + 'nav.html'
  f = open(file_name, 'w')
  print "Creating %s" % file_name
  html = template.render(files=musicFolder.children)
  f.write(html)


  #this assumes that all files are in leaf folders
  #I'm okay with this for now
  if len(musicFolder.children) == 0:
    #copy images
    for f in musicFolder.files['images']:
      shutil.copy(config.BASE_FOLDER + f, config.WEB_ROOT + f)

    #copy music
    for f in musicFolder.files['music']:
      shutil.copy(config.BASE_FOLDER + f, config.WEB_ROOT + f)
  
  #create children folders
  for i in musicFolder.children:
    create_file_pages(i.path, i)
      
if __name__ == "__main__":
  musicFolder = MusicFolder.MusicFolder(config.BASE_FOLDER, config.WEB_PATH)
  create_file_pages(config.BASE_FOLDER, musicFolder)

