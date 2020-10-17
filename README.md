# Data-Structures-in-Python
Python has four basic inbuilt data structures namely Lists, Dictionary, Tuple and Set. These almost cover 80% of the our real world data structures. 
This article will cover the above mentioned topics.  Above mentioned topics are divided into four sections below.     
Lists : Lists in Python are one of the most versatile collection object types available. The other two types are dictionaries and tuples, 
but they are really more like variations of lists.         Python lists do the work of most of the collection data structures found in other languages and 
since they are built-in, you don’t have to worry about manually creating them.         Lists can be used for any type of object, from numbers and strings to 
more lists.         They are accessed just like strings (e.g. slicing and concatenation) so they are simple to use and they’re variable length, i.e. they grow
and shrink automatically as they’re used.         In reality, Python lists are C arrays inside the Python interpreter and act just like an array of pointers.

Dictionary: In python, dictionary is similar to hash or maps in other languages. It consists of key value pairs. The value can be accessed by unique key in the dictionary.


##Data Structure Overview
Data structures are fundamental concepts of computer science which helps is writing efficient programs in any language. Python is a high-level, interpreted, interactive and object-oriented scripting language using which we can study the fundamentals of data structure in a simpler way as compared to other programming languages.

In this chapter we are going to study a short overview of some frequently used data structures in general and how they are related to some specific python data types. There are also some data structures specific to python which is listed as another category.

##General Data Structures
The various data structures in computer science are divided broadly into two categories shown below. We will discuss about each of the below data structures in detail in subsequent chapters.

#Liner Data Structures
These are the data structures which store the data elements in a sequential manner.

Array: It is a sequential arrangement of data elements paired with the index of the data element.
Linked List: Each data element contains a link to another element along with the data present in it.
Stack: It is a data structure which follows only to specific order of operation. LIFO(last in First Out) or FILO(First in Last Out).
Queue: It is similar to Stack but the order of operation is only FIFO(First In First Out).
Matrix: It is two dimensional data structure in which the data element is referred by a pair of indices.

#Non-Liner Data Structures
These are the data structures in which there is no sequential linking of data elements. Any pair or group of data elements can be linked to each other and can be accessed without a strict sequence.

Binary Tree: It is a data structure where each data element can be connected to maximum two other data elements and it starts with a root node.
Heap: It is a special case of Tree data structure where the data in the parent node is either strictly greater than/ equal to the child nodes or strictly less than it’s child nodes.
Hash Table: It is a data structure which is made of arrays associated with each other using a hash function. It retrieves values using keys rather than index from a data element.
Graph: .It is an arrangement of vertices and nodes where some of the nodes are connected to each other through links.

#Python Specific Data Structures
These data structures are specific to python language and they give greater flexibility in storing different types of data and faster processing in python environment.

List: It is similar to array with the exception that the data elements can be of different data types. You can have both numeric and string data in a python list.
Tuple: Tuples are similar to lists but they are immutable which means the values in a tuple cannot be modified they can only be read.
Dictionary: The dictionary contains Key-value pairs as its data elements.
