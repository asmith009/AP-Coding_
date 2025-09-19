# object is a construct for storing data and functions     #date = numbers string and boolenas etc.
# when creating an object we start with the class keyword.
# This acts like our object maker/our blueprint

class CarMaker:
    def __init__(self, name, color, seating, year, model, miles): #initializes the class or blueprint
     self.name = name
     self.color = color
     self.seating = seating
     self.year = year
     self.model = model
     self.miles = miles

    def printInfo(self):
      print('heres your car FAQS') # FACT
      print('name:'+ self.name)
      print('year:'+ str(self.year))
      print('miles:'+ str(self.miles))

    def widsheildwipers(self):
       print('when raining turn on')

    def airbag(self):
       print('when driving at a certian speed and collision occurs, open')
           
    def turnsignals(up, down):
        if up:
          print('turn')
        elif down:
          print('turn right')
        else:
          print('dont turn signals on')

    def bluetooth(year):
        if year > 2020:
          print('you have bluetooth')
        else:
          print('no bluetooth for this model')

carOption1 = CarMaker('carolla', 'black', '2', '2024', 'carolla', 20000) # creating actual car data

print(carOption1) # shows the location in computer memory

carOption1.printInfo() # shows me actual data
       




class PhoneMaker:
  def __init__(self, name, color, size, storage, cameras, ):
      self.name = name
      self.color = color
      self.size = size
      self.storage = storage
      self.cameras = cameras

  def printInfo(self)
     print('name:'+ self.name)
     print('color:'+ self.color)
     print('size'+ str(self.size))
     print('cameras'+ str(self.cameras))

  def background():
     UserInput = input('choose a wallpaper (pink, black, or yellow): ')
     if UserInput == 'pink':
        print('pink is now your background')

  def phoneCall():
     UserInput = input('ring ring ring, would you like to answer')

background()
  
 
  