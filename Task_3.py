with open('1.txt', encoding = 'utf') as f1:
  first = f1.readlines()
  len_lines_1 = len(first)
  file_name_1 = '1.txt'
  name_txt1 = {file_name_1 : first}


with open('2.txt', encoding = 'utf') as f2:
  second = f2.readlines()
  len_lines_2 = len(second)
  file_name_2 = '2.txt'
  name_txt2 = {file_name_2 : second}


with open('3.txt', encoding = 'utf') as f3:
  third = f3.readlines()
  len_lines_3 = len(third)
  file_name_3 = '3.txt'
  name_txt3 = {file_name_3 : third}


lines = [len_lines_1, len_lines_2, len_lines_3]
all_dicts = {}
all_dicts[len_lines_1] = name_txt1
all_dicts[len_lines_2] = name_txt2
all_dicts[len_lines_3] = name_txt3


with open('result.txt', 'a', encoding = 'utf') as r:
    for i in sorted(lines):
      for j in all_dicts[i]:
          r.write(j)
          r.write('\n')
          r.write(str(i))
          r.write('\n')
          for l in all_dicts[i][j]:
            r.write(l)
          r.write('\n')
