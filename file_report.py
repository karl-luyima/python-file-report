
import os
import argparse

#CL arguments
parser=argparse.ArgumentParser(description="Scan a directory and send info about its files")

parser.add_argument("path", help = "The directory path to scan")

parser.add_argument("--limit",
                    type=int,
                    default=20,
                    help='Max number of files to display(default : 20)')

parser.add_argument('--min-size-mb',
                    type= float,
                    default=0,
                    help='Only display files larger than this size in MB')

args=parser.parse_args()


if not os.path.isdir(args.path) :
    parser.error('The supplied path doesnt exist or is not a directory')

if args.limit<1 :
    parser.error("--limit must be at least 1")

if args.min_size_mb < 0 :
    parser.error('--min-size-mb cannot be negative')


# Convert megabytes to bytes
min_size_bytes = args.min_size_mb * 1024 * 1024

files=[]


#traverse directory and subdirectories
for root,directories, filenames in os.walk(args.path):
    for filename in filenames:
        file_path=os.path.join(root,filename)

        try:
            file_size=os.path.getsize(file_path)
            if file_size > min_size_bytes:
                files.append((file_path,file_size))

        except OSError :
            print(f"Could not access : {file_path}")


files.sort(key=lambda item:item[1], reverse= True)

print('\nFile Report')
print('=' *60)

print(f"Directory scanned : {args.path}")
print(f"Matching files found :{len(files)}")
print('=' *60)


for file_path, file_size in files[:args.limit] :
    size_mb=file_size /(1024*1024)

    print(f"Path: {file_path}")
    print(f"Size: {size_mb:.2f} MB")
    print("-" * 60)


if not files :
    print("No matching files found")


print("report completed")
