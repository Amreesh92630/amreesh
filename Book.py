class Book:
	# Attributes
	#A book has a title , an author, No of pages in it
	def __init__(self,title,author,pages):
		print('A book created')
		self.title = title # book name
		self.author = author#book written by
		self.pages = pages # no of pages in  it

	# Methods
	def __str__(self):
		return "Title: %s , author: %s pages: %s"  %(self.title,self.author,self.pages)
	def __len__(self):
		return self.pages
	def __del__(self):
		print('The book has been destroyed')



book = Book('I am great','Amreesh Kumar',175)

print(book)
print(len(book))
del book
