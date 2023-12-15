import time
import numpy as np


def day11(file_path):
    with open(file_path, 'r') as file:
        lines = file.read().splitlines()
        num_lines = len(lines)
        len_image_line = len(lines[0])
        result = 0

        # part 1
        # expansion_speed = 1
        # part 2
        expansion_speed = 1000000-1
        image_text_only = np.array([])
        image = np.array([('',0,0)])
        index_line = 0
        index_col = 0
        for line in lines:
            index_col = 0
            for c in line:
                image_text_only = np.concatenate((image_text_only, np.array([c])))
                image = np.concatenate((image, np.array([(c, index_line, index_col)])))
                index_col+=1
            index_line +=1
        image = image[1:]
        image_text_only = np.reshape(image_text_only, (num_lines, len_image_line))

        # Let's expand our image:
        # columns:
        empty_line = np.array(['.' for i in range(num_lines)])
        nb_expansion = 0
        for j in range(len_image_line):
            for i in range(num_lines):
                image[i*len_image_line + j][2] = str(int(image[i*len_image_line + j][2]) + expansion_speed * nb_expansion)
            if np.array_equal(image_text_only[:, j], empty_line):
                nb_expansion += 1

        # lines:
        empty_line = np.array(['.' for i in range(len_image_line)])
        nb_expansion = 0
        for i in range(num_lines):
            for j in range(len_image_line):
                image[i * len_image_line + j][1] = str(int(image[i * len_image_line + j][1]) + expansion_speed * nb_expansion)
            if np.array_equal(image_text_only[i, :], empty_line):
                nb_expansion += 1


        # Build a list of galaxy indexes:
        galaxy_indexes = []
        for i in range(num_lines):
            for j in range(len_image_line):
                if image[i * len_image_line + j][0] == '#':
                    galaxy_indexes += [[int(image[i * len_image_line + j][1]),int(image[i * len_image_line + j][2])]]

        sum_short_path = 0
        for i in range(len(galaxy_indexes)):
            for j in range(i+1, len(galaxy_indexes)):
                sum_short_path += abs(galaxy_indexes[i][0] - galaxy_indexes[j][0]) + abs(galaxy_indexes[i][1] - galaxy_indexes[j][1])
        print("Result : " + str(sum_short_path))


start_time = time.time()
file_path = 'input'
day11(file_path)
end_time = time.time()
print("--- %s seconds ---" % (end_time - start_time))
