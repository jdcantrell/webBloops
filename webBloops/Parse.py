'''This is the collection of functions needed to generate the site'''
from jinja2 import Template, Environment, FileSystemLoader
import MusicFolder
import os

WEB_PATH = '/'
WEB_ROOT = '/Users/john/Projects/output'
BASE_FOLDER = '/Users/john/webBloops'
TEMPLATE_PATH = '/Users/john/Projects/webBloops/templates'

env = Environment(loader=FileSystemLoader(TEMPLATE_PATH))

def create_file_pages(path, musicFolder):
  web_folder = path.replace(BASE_FOLDER, WEB_ROOT)

  try:
    os.makedirs(web_folder)
  except OSError:
    pass

  #create navigation html
  template = env.get_template('album_view.html')
  file_name = web_folder + '/nav.html'
  f = open(file_name, 'w')
  print "Creating %s" % file_name
  html = template.render(files=musicFolder.children)
  f.write(html)

  #copy images

  #copy music
  
  #create children folders
  for i in musicFolder.children:
    create_file_pages(i.path + '/', i)
      
if __name__ == "__main__":
  musicFolder = MusicFolder.MusicFolder(BASE_FOLDER, WEB_PATH)
  create_file_pages(BASE_FOLDER, musicFolder)

