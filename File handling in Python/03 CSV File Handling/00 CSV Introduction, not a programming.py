'''
               _______INTRODUCTION TO CSV FILE HANDLING________
• The CSV is (Comma Separated Values) format is the most common import and
  export format used to store tabular data for spreadsheets and databases, e.g. MS Excel.
• File extension is .csv Spreadsheet file must be saved as any but in .csv format.
• csv module should be imported in the beginning of program.
                  
                  _____________READING A CSV FILE_____________
• After opening the csv file with the read mode, we will use reader() method of csv module
  that returns the reader object that iterates the lines in the specified csv document.
• Syntax: file_reader_object = csv.reader(file_object)
• The notepad file so formed will be having the spreadsheet data in csv i.e. comma separated
  form, which when reader by reader object gives output in the form of lists.
• Each row is considered as a single list.
• While indexing of the data takes place column wise.
• Acc. to Excel, 1st column at 0th index, second column at 1st index and so on....
• Only a loop has the permission to access data bytes one by one from a csv file.

                 ______________WHAT IS A DELIMITER?______________
• A delimiter is a sequence of one or more characters used to specify the boundary
  between separate, independent regions in plain text or other data streams.
• An example of a delimiter is the comma character, which acts as a field delimiter
  in a sequence of comma-separated values.
• By default, the csv delimiter is a comma (,)
• For using a different delimiter like '*', the following syntax is as follows:
  Syntax :  obr=csv.reader(ob,delimiter='*')
  
                _______________WRITING IN A CSV FILE_______________
• csv.writer class is used to insert data to the CSV file.
• This returns a writer object which converts the user’s data into a delimited string.
• A csv file object should be opened with newline='' otherwise newline characters
  inside the quoted fields will not be interpreted correctly, it may add unwanted newline lists.
Syntax :  file_object= open(file_name,'w',newline='') 
          file_writer_object = csv.writer(file_object, delimiter) # delimiter optional
• Write mode will here also work as same as in text and binary files,
  if file exists, overwriting takes place by deleting previous data, if not, it creates a new file.
• writerow(): This method writes a single row at a time.
  Syntax :  file_writer_object.writerow (_row data in the form of list_)
• writerows(): This method is used to write multiple rows at a time.
  Syntax :  file_writer_object.writerows(rows)
'''