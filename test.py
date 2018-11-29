import os
root_path =os.getcwd()
offset = len(root_path.split("\\"))
for root,dirs,files in os.walk(root_path):
	#current_dir = root
	#path_list = current_dir.split("\\")
	#indent_level = len(path_list) - offset
	#print("\t"*indent_level,path_list[-1])
	#print(dirs)
	for f in files:
		print(f)




	#print(files)
	#os.path.splitext()


    
  