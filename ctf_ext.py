import os;
import sys;

def get_file_perms(path, paths=None):
    try:
        if paths is None:
            paths = []
        if path in paths:
            return []
        paths += [path]
        try:
            output = os.popen("ls -l " + path).read()
        except:
            return []
        lines = output.split("\n")[1:-1]

        files = []
        readable_folders = []
        for line in lines:
            if line[0] == 'd':
                if line.split(" ")[0][-4] == "r":
                    readable_folders.append(path + "/" + line.split(" ")[-1])
            elif line[0] == "-":
                files.append(line)
            elif line[0] == "l":
                pass # links are useless

        print(files)
        
        valid_files = [(path + "/" + file.split(" ")[-1]) for file in files if int(file.split(" ")[4]) > 0]
        for readable in readable_folders:
            files_with_write += get_file_perms(readable, paths)
        return files_with_write
    except:
        return []

print("running...")

cwd = os.getcwd()
files = get_file_perms(cwd)

output_filename = sys.argv[1] if len(sys.argv) > 1 else "/home/student/output_ctf_ext.txt"

with open(output_filename, "w+") as f:
    f.write("\n".join(files))
    f.write("\n")

print("Done! Found " + str(len(files)) + " files.")
