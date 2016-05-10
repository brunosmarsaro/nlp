# TODO Create method to write;
# TODO Create method to verify sections, variable and values;
# TODO Create exceptions.
# TODO Add a way to make comments on the file. In the middle of lines too.
# TODO Correct the reading of variables [comparing line to '\n' doesn't work for all the cases]

class Parser:
    def __init__(self, i_section, i_end, i_value):
        self.i_section = i_section
        self.i_end = i_end
        self.i_value = i_value
        self.list_sections = []
        self.dic = {}

    def get_header(self, line):
        '''
        for c in line:
            for d in self.i_section:
                print(c, d)
                if c != d:
                    print("Invalid section indicator")
                    exit()
            break
        '''
        line = line[len(self.i_section):]
        line = line.strip().replace(self.i_end, "")
        return line

    def get_variable(self, line):
        i = line.index(self.i_value)
        line = line[:i].strip()
        return line

    def get_value(self, line):
        i = line.index(self.i_value)
        line = line[(i+1):].strip()
        return line

    def read(self, file):
        self.filename = file
        with open(self.filename, 'r') as fp:
            #if not self.i_section in fp:
            #    print("Missing section header")
            #    exit()

            for line in fp:
                if line[0] == '#':
                    continue
                if self.i_section in line:
                    header = self.get_header(line)
                    self.list_sections.append(header)
                    self.dic[header] = {}
                    for item in fp:
                        if item[0] == '#':
                            continue
                        if not line: break
                        if line == '\n':
                            break
                        try:
                            variable = self.get_variable(item)
                            value = self.get_value(item)
                            self.dic[header][variable] = value
                        except ValueError:
                            break

    def sections(self):
        print(self.list_sections)

    # TODO: Finish it:
    '''
    def write(self, file):
        with open(file, 'a+') as fp:
    '''