#crear un libro de excel con openpyxl

from openpyxl import Workbook

workbook = Workbook()
# Crear una hoja de trabajo
workbook.save("./Tareas/practica_excel.xlsx")
