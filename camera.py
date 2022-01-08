import pytesseract
from PIL import Image

def checker(word):
   for x in word:
      if x.isdigit():
         return True

def fixing(word):
   if word[0] == "O":
      word = "0" + word[1:len(word)]
   if word.find("g") == -1:
      counter = -1
      for x in range(len(word)):
         if word[x] == "9":
            counter = x
      if counter != -1:
         word = str(word[:counter]) + "g"
   return word



def reader():
   pytesseract.pytesseract.tesseract_cmd = r'C:\Users\Jeffr\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'
   words = pytesseract.image_to_string(Image.open("Test.jpg"))

   calories = None
   fat = None
   cholesterol = None
   sodium = None
   carbohydrate = None
   sugar = None
   protein = None

   words = words.split()
   for x in range(len(words)):
      if words[x] == "Calories" and calories == None and (checker(words[x+1]) or words[x+1][0] == "O"):
         calories = words[x+1]
         calories = fixing(calories)
      elif words[x] == "Fat" and fat == None and checker(words[x+1]):
         fat = words[x + 1]
         fat = fixing(fat)
      elif words[x] == "Cholesterol" and cholesterol == None and (checker(words[x+1]) or words[x+1][0] == "O"):
         cholesterol = words[x + 1]
         cholesterol = fixing(cholesterol)
      elif words[x] == "Sodium" and sodium == None and (checker(words[x+1]) or words[x+1][0] == "O"):
         sodium = words[x + 1]
         sodium = fixing(sodium)
      elif words[x] == "Carbohydrate" and carbohydrate == None and (checker(words[x+1]) or words[x+1][0] == "O"):
         carbohydrate = words[x + 1]
         carbohydrate = fixing(carbohydrate)
      elif words[x] == "Sugars" and sugar == None and (checker(words[x+1]) or words[x+1][0] == "O"):
         sugar = words[x + 1]
         sugar = fixing(sugar)
      elif words[x] == "Protein" and protein == None and (checker(words[x+1]) or words[x+1][0] == "O"):
         protein = words[x + 1]
         protein = fixing(protein)


   print(calories,fat,cholesterol,sodium,carbohydrate,sugar,protein)

reader()


