from ._anvil_designer import Form1Template
from anvil import *
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
      
def btnSort_click(self, **event_args):
    input_text = self.txtInput.text
    numbers = [int(x) for x in input_text.split()]

    insertion_sort(numbers)

    self.dataGrid.items = [{'number': num} for num in numbers]
  
class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.txtInput.text = " "
    self.dataGrid.items = []
    # Any code you write here will run before the form opens.

  def txtInput_change(self, **event_args):
    self.dataGrid.items = []

  def btnSort_click(self, **event_args):
    btnSort_click(self, **event_args)
  

