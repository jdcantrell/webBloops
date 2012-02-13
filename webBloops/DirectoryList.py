'''This class is a simple recursive directory loader. It's meant to be
subclassed to only allow specific files and folders into the final file
list'''
import os

class DirectoryList(object):
  def __init__(self, path):
    self.path = path
    self.fileCount = 0

    if not self.path.endswith('/'):
      self.path = self.path + '/'

  def load(self):
    self.fileCount = 0
    return self._get_files(self.path);

  def _get_files(self, path):
    folders = [] 
    if self.checkDirectory(path):
      #current folder dictionary
      folder = {"path": path}
      file_count = 0

      #check the current directory for files and sub-folders
      items = os.listdir(path)
      children = []
      for x in items:
        file_path = path + x + '/'
        if os.path.isdir(file_path):
          if self.checkDirectory(file_path):
            children.append(file_path)
        else:
          if self.checkFile(x, path):
            file_count += 1
            self.addFile(folder, x, path)

      #check child folders
      child_folders = []
      for c in children:
        child_folders.extend(self._get_files(c))

      #if we have anything worthwhile to return lets do that
      if len(child_folders) or file_count:
        self.fileCount += file_count
        self.addFolder(folder)

        folders.append(folder)
        folders.extend(child_folders)

    return folders

  def checkFile(self, file_name, path):
    return file_name.endswith(('.mp3', '.ogg', '.flac', '.png', '.jpg'))

  def checkDirectory(self, folder):
    return True

  def addFolder(self, folder):
    #add custom folder keys here
    pass

  def addFile(self, folder, filename, file_path):
    if folder.has_key('files'):
      folder["files"].append(filename)
    else:
      folder["files"] = [filename]

if __name__ == "__main__":
  import sys
  dl = DirectoryList(sys.argv[1])
  dirs = dl.load()
  print dirs
  print "Found %d files" % dl.fileCount
  print "Found %d folders" % len(dirs)


