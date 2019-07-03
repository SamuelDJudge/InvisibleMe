file = open("system_info.csv","r+")
line = file.readline()
file.close()
line = line.split(',')
column_list_str = line[4:]
column_list = []
for a_string in column_list_str:
    column_list.append(int(a_string))
file_path = str(line[0])
write_path = str(line[1])
en_or_de = str(line[2])
delimiter_list = ["period", "comma", "line", "tab", "newline"]
delimiter_charaters = [".",",","|","\t","\n"]
delimiter = delimiter_charaters[delimiter_list.index(str(line[3]))]

keys_write_path = "s3a://rijndaelkeys/keys"
