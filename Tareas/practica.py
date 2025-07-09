try:
  document = open("Tareas/history.txt", "r")
  print(document.read())
except Exception as e:
  print(e)
finally:
  document.close()

  