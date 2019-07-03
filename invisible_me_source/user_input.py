# Imports
file = open("/home/ubuntu/InvisibleMe/python/system_info.csv","r+")
for a_line in file:
    a_line = a_line.split(',')
    column_list_str = a_line[4:]
    column_list = []
    for a_string in column_list_str:
        column_list.append(int(a_string))
    file_path = str(a_line[0])
    write_path = str(a_line[1])
    en_or_de = str(a_line[2])
    delimiter_list = ["period", "comma", "line", "tab", "newline"]
    delimiter_charaters = [".",",","|","\t","\n"]
    delimiter = delimiter_charaters[delimiter_list.index(str(a_line[3]))]
file.close()
