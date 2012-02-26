from DirectoryList import *
import os

class MusicFolder(DirectoryList):
  def __init__(self, path, out_path):
    self.audioCount = 0
    super(MusicFolder, self).__init__(path)
    if out_path.endswith('/'):
      self.out_path = out_path
    else:
      self.out_path = "%s%s" % (out_path, '/')

  def checkFile(self, file_name, path):
    if file_name.endswith(('.mp3', '.ogg', '.flac', '.png', '.jpg', '.gif')):
      out_path = path.replace(self.path, self.out_path)
      base, extension = os.path.splitext(file_name)

      if not os.path.isfile("%s%s.mp3" % (out_path, base)):
        return True
    return False

  def addFolder(self, folder):
    path = folder["path"]
    folder["out_path"] = path.replace(self.path, self.out_path)

  def addFile(self, folder, filename, file_path):
    if filename.endswith(('.mp3', '.ogg', '.flac')):
      self.audioCount += 1
      if folder.has_key('audio'):
        folder["audio"].append(filename)
      else:
        folder["audio"] = [filename]

    else:
      if filename.endswith(('.gif', '.png', '.jpg')):
        if folder.has_key('images'):
          folder["images"].append(filename)
        else:
          folder["images"] = [filename]


if __name__ == "__main__":
  import sys
  dl = MusicFolder(sys.argv[1], sys.argv[2])
  dirs = dl.load()
  print dirs
  print "Found %d files" % dl.fileCount
  print "Found %d folders" % len(dirs)
