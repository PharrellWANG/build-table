from extract_text import ExtractText

list_file_names = [
    'txt/sm_04.txt',
    'txt/sm_08.txt',
    'txt/sm_16.txt',
    'txt/sm_32.txt'
]

# extraction1 = ExtractText(is_ordered=False)
# extraction1.read_lines_into_list(file_name='txt/sm_04.txt')
# extraction1.print_lists()

extraction2 = ExtractText(is_ordered=False)
extraction2.read_lines_into_multiple_lists(list_of_file_names=list_file_names)
extraction2.print_full_lists()

# extraction3 = ExtractText(is_ordered=True)
# extraction3.read_lines_into_list(file_name='txt/sm_04.txt')
# extraction3.print_lists()

extraction4 = ExtractText(is_ordered=True)
extraction4.read_lines_into_multiple_lists(list_of_file_names=list_file_names)
extraction4.print_full_lists()
