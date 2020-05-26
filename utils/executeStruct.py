from structure import make_struct, make_dir
import os
import sys

if __name__ == '__main__':
    src_path = sys.argv[1]       # src path
    dest_path = sys.argv[2]      # Destination path
    file_format = sys.argv[3]    # conversion format

    # Prepare data structure for Clara
    clara_path = make_dir(dest_path, 'Clara_Structure')
    os.chdir(clara_path)

    studies = [x[0] for x in os.walk(src_path)][1:]
    for study in studies:
        id = os.path.basename(study)
        struct_dir = make_dir(clara_path, id)
        make_struct(study, struct_dir, file_format)
