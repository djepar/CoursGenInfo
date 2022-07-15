import os
def parent_directory():
  # Create a relative path to the parent 
  # of the current working directory 
  path_current = os.getcwd()
  os.chdir("..")
  path_child = os.listdir(".")
  relative_parent = os.path.join(path_current, path_child)

  # Return the absolute path of the parent directory
  return relative_parent

print(os.listdir("."))