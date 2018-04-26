def replace_underscore(entry):
    tmp = list(entry)
    if tmp[0] == '_':
        tmp[0] = ''
        entry = ''.join(tmp)
        return entry
    return entry

class ExtractText:
    """The class for read .txt file(s) and extract text.

    Note: see generate_table.py for examples.
    """

    def __init__(self, is_ordered):
        self.is_ordered = is_ordered
        if not self.is_ordered:
            self.OUT_FILE = 'output/latex_unordered_body.txt'
            self.LINE_IDX = 4
            self.START_POS_ONE = 12
            self.START_POS_TWO = 72
            self.lineList1 = []
            self.lineList3 = []
            self.lineList2 = []
            self.lineList4 = []
        else:
            self.OUT_FILE = 'output/latex_ordered_body.txt'
            self.LINE_IDX = 45
            self.START_POS_ZERO = 5
            self.START_POS_ONE = 12
            self.START_POS_TWO = 66
            self.lineList1 = []
            self.lineList3 = []
            self.lineList2 = []
            self.lineList4 = []

    def read_lines_into_list(self, file_name):
        """
            Read all lines into a list
        """
        with open(file_name, 'r') as f:
            for cnt, line in enumerate(f):
                if self.LINE_IDX < cnt + 1 < self.LINE_IDX + 38:
                    self.lineList1.append(line)

    def print_lists(self):
        """
            Print list
        """
        for item_idx, item in enumerate(self.lineList1):
            num_of_samples = int(item[self.START_POS_ONE:self.START_POS_ONE+9])
            percentage = float(item[self.START_POS_TWO:self.START_POS_TWO+8])
            print('%3d  %9d  %8s' % (item_idx, num_of_samples, '{0:.2f}'.format(round(percentage*100, 2))))

        print('The length of list is: %d' % len(self.lineList1))
        print('========================== end of lineList1')

    def read_lines_into_multiple_lists(self, list_of_file_names):
        """
            Read lines into multiple lines
        """
        line_list = [
            self.lineList1,
            self.lineList2,
            self.lineList3,
            self.lineList4
        ]
        for line, filename in zip(line_list, list_of_file_names):
            with open(filename, 'r') as f:
                for cnt, f_line in enumerate(f):
                    if self.LINE_IDX < cnt + 1 < self.LINE_IDX+38:
                        line.append(f_line)

    def print_full_lists(self):

        item_idx = -1
        for item in self.lineList1:

            with open(self.OUT_FILE, 'a') as the_file:
                # the_file.write('Hello\n')

                item_idx += 1
                num_of_samples = int(item[self.START_POS_ONE:self.START_POS_ONE+8])
                percentage = float(item[self.START_POS_TWO:self.START_POS_TWO+8])

                num_of_samples1 = int(self.lineList2[item_idx][self.START_POS_ONE:self.START_POS_ONE+8])
                percentage1 = float(self.lineList2[item_idx][self.START_POS_TWO:self.START_POS_TWO+8])

                num_of_samples2 = int(self.lineList3[item_idx][self.START_POS_ONE:self.START_POS_ONE+8])
                percentage2 = float(self.lineList3[item_idx][self.START_POS_TWO:self.START_POS_TWO+8])

                num_of_samples3 = int(self.lineList4[item_idx][self.START_POS_ONE:self.START_POS_ONE+8])
                percentage3 = float(self.lineList4[item_idx][self.START_POS_TWO:self.START_POS_TWO+8])

                if self.is_ordered:
                    unordered_idx0 = str(
                        item[self.START_POS_ZERO:self.START_POS_ZERO + 3])

                    unordered_idx1 = str(self.lineList2[item_idx][
                                          self.START_POS_ZERO:self.START_POS_ZERO + 3])

                    unordered_idx2 = str(self.lineList3[item_idx][
                                          self.START_POS_ZERO:self.START_POS_ZERO + 3])

                    unordered_idx3 = str(self.lineList4[item_idx][
                                          self.START_POS_ZERO:self.START_POS_ZERO + 3])

                    # text = 'abcdefg'
                    # new = list(text)
                    # new[6] = 'W'
                    # ''.join(new)
                    unordered_idx0 = replace_underscore(entry=unordered_idx0)
                    unordered_idx1 = replace_underscore(entry=unordered_idx1)
                    unordered_idx2 = replace_underscore(entry=unordered_idx2)
                    unordered_idx3 = replace_underscore(entry=unordered_idx3)

                    print(
                        '%3d & %s & %s & %5s & %s & %s & %5s & %s & %s & %5s & %s & %s & %5s \\\\' %
                        (item_idx,
                         unordered_idx0,
                         '{:,}'.format(num_of_samples),
                         '{0:.2f}'.format(round(percentage * 100, 2)),
                         unordered_idx1,
                         '{:,}'.format(num_of_samples1),
                         '{0:.2f}'.format(round(percentage1 * 100, 2)),
                         unordered_idx2,
                         '{:,}'.format(num_of_samples2),
                         '{0:.2f}'.format(round(percentage2 * 100, 2)),
                         unordered_idx3,
                         '{:,}'.format(num_of_samples3),
                         '{0:.2f}'.format(round(percentage3 * 100, 2)),
                         ))
                    the_file.write(
                        '%3d & %s & %s & %5s & %s & %s & %5s & %s & %s & %5s & %s & %s & %5s \\\\ \n' %
                        (item_idx,
                         unordered_idx0,
                         '{:,}'.format(num_of_samples),
                         '{0:.2f}'.format(round(percentage * 100, 2)),
                         unordered_idx1,
                         '{:,}'.format(num_of_samples1),
                         '{0:.2f}'.format(round(percentage1 * 100, 2)),
                         unordered_idx2,
                         '{:,}'.format(num_of_samples2),
                         '{0:.2f}'.format(round(percentage2 * 100, 2)),
                         unordered_idx3,
                         '{:,}'.format(num_of_samples3),
                         '{0:.2f}'.format(round(percentage3 * 100, 2)),
                         ))
                else:
                    print(
                        '%3d & %s & %5s & %s & %5s & %s & %5s & %s & %5s \\\\' %
                        (item_idx,
                         '{:,}'.format(num_of_samples),
                         '{0:.2f}'.format(round(percentage * 100, 2)),
                         '{:,}'.format(num_of_samples1),
                         '{0:.2f}'.format(round(percentage1 * 100, 2)),
                         '{:,}'.format(num_of_samples2),
                         '{0:.2f}'.format(round(percentage2 * 100, 2)),
                         '{:,}'.format(num_of_samples3),
                         '{0:.2f}'.format(round(percentage3 * 100, 2)),
                         ))
                    the_file.write(
                        '%3d & %s & %5s & %s & %5s & %s & %5s & %s & %5s \\\\ \n' %
                        (item_idx,
                         '{:,}'.format(num_of_samples),
                         '{0:.2f}'.format(round(percentage * 100, 2)),
                         '{:,}'.format(num_of_samples1),
                         '{0:.2f}'.format(round(percentage1 * 100, 2)),
                         '{:,}'.format(num_of_samples2),
                         '{0:.2f}'.format(round(percentage2 * 100, 2)),
                         '{:,}'.format(num_of_samples3),
                         '{0:.2f}'.format(round(percentage3 * 100, 2)),
                         ))

        print('The length of list is: %d' % len(self.lineList1))
        print('========================== end')
