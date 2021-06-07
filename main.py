class Kitchen:
    def __init__(self):
        self.microwave = Microwave()
        self.dishwasher = Dishwasher()
        self.microwave_methods = [f for f in dir(Microwave) if not f.startswith('_')]
        self.dishwasher_methods = [f for f in dir(Dishwasher) if not f.startswith('_')]

    def __getattr__(self, func):
        def method(*args):
            if func in self.microwave_methods:
                return getattr(self.microwave, func)(*args)
            elif func in self.dishwasher_methods:
                return getattr(self.dishwasher, func)(*args)
            else:
                raise AttributeError

        return method
class Microwave:
  def __init__(self):
    pass

  def heat_up_food(self):
    print("Food is being microwaved")

  def shutdown(self):
      print("Microwave is being shutdown")


class Dishwasher:
  def __init__(self):
    pass

  def wash_dishes(self):
    print("Dishwasher starting")

if __name__ == '__main__':
    kitchen = Kitchen()


    # Metodos chamados a partir da Kitchen mas contidos em Microwave
    kitchen.heat_up_food()
    kitchen.shutdown()
