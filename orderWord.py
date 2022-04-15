"""

order words 

simple input:

qwe:213
kawqead:798
mojsad:786
kilar:895

output:

qwe:213
kilar:895
mojsad:786
kawqead:798

"""


# This Code Developed By Mohammad Al Jadallah

with open("<testFileName>.txt", "r") as read_file:
    all_rows_inside_the_file = read_file.readlines()
    number_of_rows = len(all_rows_inside_the_file)

    rows = []
    for n in range(number_of_rows - 1):
        row = all_rows_inside_the_file[n]
        rows.append((len(row[:row.index(":")]), row))

    data = rows
    after_sort_rows = sorted(data)
    with open("<outputFileName>.txt", "w") as file:
        for key, value in after_sort_rows:
            file.write(value + "\n")

    file.close()

read_file.close()


