class Animal:
	__metaclass__ = ABCMeta
	@abstractmethod
	def say_something(self):
		return "I'm an animal!"
class Duck(Animal):
	def say_something(self):   
    	s = super(Duck, self).say_something()
    	return "%s - %s" % (s, "quack")
d=Duck()
print(d.say_something())
