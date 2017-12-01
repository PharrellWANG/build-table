class ExtractText:
    """The class for read .txt file(s) and extract text.

    Note: see generate_table.py for examples.
    """

    def __init__(self):
        self.LINE_IDX = 4
        self.START_POS_ONE = 12
        self.START_POS_TWO = 72
        self.lineList1 = []
        self.lineList2 = []
        self.lineList3 = []
        self.lineList4 = []

    def read_lines_into_list(self, file_name):

        file = open(file_name, 'r')
        cnt = 0
        for line in file:
            cnt += 1
            if 4 < cnt < 42:
                self.lineList1.append(line)

    def print_lists(self):

        item_idx = -1
        for item in self.lineList1:
            item_idx += 1
            num_of_samples = int(item[self.START_POS_ONE:self.START_POS_ONE+9])
            percentage = float(item[self.START_POS_TWO:self.START_POS_TWO+8])
            print('%3d  %9d  %8s' % (item_idx, num_of_samples, '{0:.2f}'.format(round(percentage*100, 2))))

        print('The length of list is: %d' % len(self.lineList1))
        print('========================== end of lineList1')


    def read_lines_into_multiple_lists(self, list_of_file_names):

        file = open(list_of_file_names[0], 'r')
        cnt = 0
        for line in file:
            cnt += 1
            if 4 < cnt < 42:
                self.lineList1.append(line)

        file = open(list_of_file_names[1], 'r')
        cnt = 0
        for line in file:
            cnt += 1
            if 4 < cnt < 42:
                self.lineList2.append(line)

        file = open(list_of_file_names[2], 'r')
        cnt = 0
        for line in file:
            cnt += 1
            if 4 < cnt < 42:
                self.lineList3.append(line)

        file = open(list_of_file_names[3], 'r')
        cnt = 0
        for line in file:
            cnt += 1
            if 4 < cnt < 42:
                self.lineList4.append(line)


    def print_full_lists(self):

        item_idx = -1
        for item in self.lineList1:

            with open('output/latex_table_body.txt', 'a') as the_file:
                # the_file.write('Hello\n')

                item_idx += 1
                num_of_samples = int(item[self.START_POS_ONE:self.START_POS_ONE+9])
                percentage = float(item[self.START_POS_TWO:self.START_POS_TWO+8])

                num_of_samples1 = int(self.lineList2[item_idx][self.START_POS_ONE:self.START_POS_ONE+9])
                percentage1 = float(self.lineList2[item_idx][self.START_POS_TWO:self.START_POS_TWO+8])

                num_of_samples2 = int(self.lineList3[item_idx][self.START_POS_ONE:self.START_POS_ONE+9])
                percentage2 = float(self.lineList3[item_idx][self.START_POS_TWO:self.START_POS_TWO+8])

                num_of_samples3 = int(self.lineList4[item_idx][self.START_POS_ONE:self.START_POS_ONE+9])
                percentage3 = float(self.lineList4[item_idx][self.START_POS_TWO:self.START_POS_TWO+8])

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
