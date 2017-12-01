from extract_text import ExtractText

list_file_names = [
    'txt/size_04.txt',
    'txt/size_08.txt',
    'txt/size_16.txt',
    'txt/size_32.txt'
]

extraction1 = ExtractText()
extraction1.read_lines_into_list(file_name='txt/size_04.txt')
extraction1.print_lists()

extraction2 = ExtractText()
extraction2.read_lines_into_multiple_lists(list_of_file_names=list_file_names)
extraction2.print_full_lists()
