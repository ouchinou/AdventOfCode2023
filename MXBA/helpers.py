# -*- coding: utf-8 -*-
"""
Created on Fri Dec 15 14:47:39 2023

@author: mxba
"""


def write_to_file(file_path, content):
    try:
        # Open the file in write mode ('w')
        outfile = file_path + ".txt"
        with open(outfile, 'w') as file:
            # Write the content to the file
            for line in content:
                print("".join(line), file=file)
        print(f"Content successfully written to '{outfile}'")
    except IOError as e:
        print(f"Error writing to file: {e}")
