"""
This scripts helps to create new project from djangostrap files
"""
from os import listdir, mkdir, rename
from os.path import dirname, abspath, join, isdir
import shutil, sys


def replace_in_dir(dirpath, old_string, new_string):
  for fname in listdir(dirpath):
    fpath = join(dirpath, fname)
    if isdir(fpath):
      replace_in_dir(fpath, old_string, new_string)
    else:
      replace(fpath, old_string, new_string)

def replace(filepath, old_string, new_string):
  content = open(filepath).read()
  if old_string in content:
    content = content.replace(old_string, new_string)
    f = open(filepath, 'w')
    f.write(content)
    f.flush()
    f.close()


def genereate_new_secret_key():
  import random
  return ''.join([random.SystemRandom().choice('abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)') for i in range(50)])

if __name__ == "__main__":
  args = sys.argv
  if len(args) != 2: print("\n\tUsage: ./djangostrap.py <name_of_your_project>"); exit()

  new_project_name = args[1]
  ds_dir = abspath("..")
  new_project_dir = join(ds_dir, new_project_name)
  if isdir(new_project_dir):
    raise Exception("%s already exists! please select another name or delete this folder!" %(new_project_dir))
  shutil.copytree(".", new_project_dir, ignore = shutil.ignore_patterns("*.pyc", ".git"))
  rename(join(new_project_dir, "djangostrap"), join(new_project_dir, new_project_name))
  replace_in_dir(new_project_dir, "djangostrap", new_project_name)
  with open(join(new_project_dir, "secret_key.txt"), "w") as f:
    f.write(genereate_new_secret_key())
    f.close()

  print("\n\tNew project was created in " + new_project_dir)