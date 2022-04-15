# CSV Combiner - command line program that takes several CSV files as arguments
# Leonie Nutz
# 04/14/2022

import os.path
import sys
import pandas as pd


# function to return the basename of the file
def get_file_name(path):
    file_name = os.path.basename(path)
    return file_name


# function to return the directory name of the file
def get_dir_name(path):
    dir_name = os.path.dirname(path)
    return dir_name


# main function
def main():
    csv_files = []
    all_df = []
    file_num = len(sys.argv)
    # loop through command line arguments
    for i in range(file_num):
        # if command line argument is a file then continue in the loop
        # for more complex program we could use argparse instead of sys.argv
        if os.path.isfile(sys.argv[i]):
            # if file type is csv then append to csv_files list
            if sys.argv[i].endswith('.csv'):
                # create full path
                name = get_file_name(sys.argv[i])
                path = get_dir_name(sys.argv[i])
                full = path + '/' + name
                csv_files.append(full)

    # add filename column containing corresponding file name
    for file in csv_files:
        df = pd.read_csv(file, sep=',')
        df['filename'] = file.split('/')[-1]
        all_df.append(df)
    # merge all dataframes and convert to csv file
    combined_csv = pd.concat(all_df, ignore_index=True)
    combined_csv = combined_csv.to_csv(index=False)
    print(combined_csv)


if __name__ == "__main__":
    main()
