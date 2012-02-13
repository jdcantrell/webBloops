'''This file will recurse through a directory and convert all audio
files to medium quality mp3s, it will skip files that already exist in
the destination directory'''
from MusicFolder import *
from clint import  args
from clint.textui import colored, puts
from pbs import lame, ogg123, flac, mp3info, cp

import os, sys

rows, columns = os.popen('stty size', 'r').read().split()
console_width = int(columns)

def clean_path(path):
  return '"%s"' % path.replace('"','\\"')

def convert(filename, path, output_path):
  base, extension = os.path.splitext(filename)
  extension = extension.lower()
  
  infile = clean_path("%s%s" % (path, filename))
  outfile = clean_path("%s%s.mp3" % (output_path, base))

  if extension == ".mp3":
    
    #determine if we we should re-encode this mp3 to a lower bit rate
    out = mp3info("-x", "-r v",'-p "%r"', infile)
    convert = False
    if out == "Variable":
      out = mp3info("-x", "-r m",'-p "%r"', infile)
      if int(out) >= 170:
        convert = True
    else:
      if int(out) >= 128:
        convert = True
        
    if convert:
      lame("--preset fast medium", "--mp3input", infile, outfile)
    else:
      cp(infile, outfile)
  elif extension == ".flac":
    lame(flac('-c', '-d', infile), "--preset fast medium",  '-', outfile)
  elif extension == ".ogg":
    lame(ogg123('-d wav', '-f', '-', infile), "--preset fast medium", '-', outfile)

#get source and destination directories
source = args.get(0)
destination = args.get(1)

#searching for files
print "Searching for music files...",
dl = MusicFolder(source, destination)
folders = dl.load()
print "done!"

print "Converting files:"
count = 0
total_paths = len(folders)

output_str = "%s %%s %%s" % colored.blue("(%s/%s)")
output = ""
for folder in folders: 
  #create directory if needed
  if not os.path.isdir(folder['out_path']):
    os.makedirs(folder['out_path'])
  

  if folder.has_key("audio"):
    path_disp = folder['path'].replace(source, '')

    folder["audio"].sort()
    for filename in folder["audio"]: 
      #trim path if it is too long
      length = len('%s%s%s%s' % (count, dl.fileCount, path_disp, filename)) + 5
      if length > console_width:
        if length - console_width < len(path_disp):
          path_disp = '...%s' % path_disp[(length - console_width + 3):len(path_disp)]
        else:
          path_disp = ''
      #trim file name if we're still over
      length = len('%s%s%s%s' % (count, dl.fileCount, path_disp, filename)) + 5
      filename_disp = filename
      if length > console_width:
        if length - console_width < len(filename):
          filename_disp = '...%s' % filename[(length - console_width + 3):len(filename)]

      output = output_str % (count, dl.fileCount, colored.cyan(filename_disp), colored.white(path_disp))

      puts(output, False)
      puts(" " * (console_width - len(colored.clean(output))), False)
      puts("\r", False)
      sys.stdout.flush()
      try:
        convert(filename, folder['path'], folder['out_path'])
      except Exception, e:
        puts(output, False)
        puts(" " * (console_width - len(colored.clean(output))), True)
        puts(colored.red("Failed on file:"), filename)
        puts(colored.red("path:"), folder['path'])
        puts('%r' % e)
        sys.exit(0)
      count += 1

puts(output, True)
puts(colored.green("Complete!"))
