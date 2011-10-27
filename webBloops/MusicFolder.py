'''MusicFolder will recurse through the given directory and collect information
about each level. It collects the images and available music files in a simple
object for parsing'''
import os

class MusicFolder:
  def __init__(self, path, web_path):
    self.web_path = web_path
    self.path = path

    #clean up file paths
    if web_path[len(web_path) - 1] != '/':
      self.web_path += '/'
    
    if path[len(path) - 1] != '/':
      self.path += '/'
    self.name = path.split('/').pop()
    self.children = []
    self.files = {'music': [], 'images': []}
    self._get_files()

  def _get_files(self):
    items = os.listdir(self.path)
    children = []
    for x in items:
      if os.path.isdir(self.path + x):
        children.append(x)
      else:
        if not self._add_file(x.replace(self.path, self.web_path), ['.mp3'], 'music'):
          self._add_file(x.replace(self.path, self.web_path), ['.png', '.jpg', '.gif'], 'images')
    #add children to our list
    for c in children:
      print 'Children %s' % self.path + c
      self._add_child(MusicFolder(self.path + c, self.web_path + c))

  def _add_file(self, file_name, types, file_type):
    ret = False;
    for t in types:
      try:
        file_name.index(t)
        self.files[file_type].append(self.web_path  + file_name)
        ret = True
      except ValueError:
        pass
    return ret

  def _add_child(self, child):
    self.children.append(child)

    if len(child.files['images']):
      self.files['images'].append(child.files['images'][0])
