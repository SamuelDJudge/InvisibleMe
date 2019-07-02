# Imports
file = open("/home/ubuntu/InvisibleMe/python/system_info.csv","r+")
for a_line in file:
    a_line = a_line[:-2]
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
print("##################", column_list,file_path,write_path,delimiter,"#################")










#column_list = [7,11]
#file_path = "s3a://fecpoliticaldata/small_data.tex"
#write_path = "s3a://fecdatakeys/encrypted"
read_path = "s3://fecdatakeys/encrypted/part-00000-8def0398-3961-4a1d-9f0b-2e830ac84039-c000.csv"
#delimiter = '|'
#en_or_de = "encryption"
id_num = "part-00000-ab4cde60-93c1-4bdb-89d9-835cc498047f-c000"
keys_write_path = "s3a://fecdatakeys/keys"
keys_read_path = "s3://fecdatakeys/keys/part-00000-f4922dc0-b219-4ffe-9833-e63f9ccc0316-c000.csv"
