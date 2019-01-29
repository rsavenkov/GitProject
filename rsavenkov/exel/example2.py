# see https://xlsxwriter.readthedocs.io/example_hello_world.html
import xlsxwriter

workbook = xlsxwriter.Workbook('hello_world.xlsx')
worksheet = workbook.add_worksheet()

worksheet.write('A1', 'Hello world')

workbook.close()