'''This class is a simple representation of a folder in webBloops, it contains
all the required information for displaying the folder'''
import os

class MusicFolder:
  def __init__(self, path):
    self.path = path
    self.images = []
    self.children = []
    self.files = {'music': [], 'images': []}
    self._get_files()

  def _get_files(self):
    items = os.listdir(self.path)
    children = []
    for x in items:
      if os.path.isdir(self.path + '/' + x):
        children.append(x)
      else:
        if not self._add_file(x, ['.mp3'], self.files['music']):
          self._add_file(x, ['.png', '.jpg'], self.files['images'])
    #add children to our list
    for c in children:
      print "Checking child %s" % self.path + '/' + c
      self.addChild(MusicFolder(self.path + '/' + c))

  def _add_file(self, file_name, types, file_type):
    ret = False;
    for t in types:
      try:
        file_name.index(t)
        file_type.append(file_name)
        ret = True
      except ValueError:
        pass
    return ret

  def addChild(self, child):
    self.children.append(child)

    if (child.images):
      self.images.append(child.images[0])

if __name__ == "__main__":
  a = MusicFolder('/Users/jcantrell/Downloads/webBloops')
  dir(a)
  print '%s' % a.files
