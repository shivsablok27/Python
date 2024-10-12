'''
                      BINARY FILE HANDLING

• To open a file in binary format, add 'b' to the mode parameter.
• The "rb" mode opens the file in binary format for reading.
• The "wb" mode opens the file in binary format for writing.
• Like text files are opened with ".txt" format, the extension for binary file is ".dat"
  Example:  ob.open("stud.dat" , "wb")
  
• Unlike text files, binary files are not human-readable.
• When opened using any text editor, the data is unrecognizable.

• "Picke" Module is used in the binary file handling.
• So we have to import "Pickle module" in the beginning of the program.
• Python pickle module is used for serializing and de-serializing a Python object structure.
• Any object in Python can be pickled so that it can be saved on disk.
• What pickle does is that it “serializes” the object first before writing it to file.
• Pickling is a way to convert a python object (list, dict, etc.) into a character stream.

• The load() method of Python pickle module reads the pickled byte stream of one or more
  python objects from a file object. It is similar to the read() function used for txt files.
• It is used with "rb" mode.

Syntax:  python_object = pickle.load (file_object)

• The dump() function writes pickled object to a file. It is used with "wb" mode.
• It is similar to write() function used for txt files.

Syntax: pickle.dump (python_object , file_object)


'''