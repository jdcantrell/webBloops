'''This is the collection of functions needed to generate the site'''
from jinja2 import Template, Environment, FileSystemLoader
import MusicFolder
BASE_FOLDER = '/Users/jcantrell/Downloads/webBloops'
TEMPLATE_PATH = '/Users/jcantrell/Projects/webBloops/templates'

env = Environment(loader=FileSystemLoader(TEMPLATE_PATH))

def create_file_pages(path):
  folder = MusicFolder.MusicFolder(path)
  template = env.get_template('album_view.html')
  html = template.render(files=folder.children)
  print html
  
  for i in folder.children:
    print "Creating page for %s" % i.path
    create_file_pages(i.path)

      
if __name__ == "__main__":
  create_file_pages(BASE_FOLDER)

