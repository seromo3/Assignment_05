#------------------------------------------#
# Title: CDInventory.py
# Desc: Script to store CD inventory in a list of dictionaries
# Change Log: (Who, When, What)
# SRomo, 2020-Aug-09, Created File
# SRomo, 2020-Aug-11, Added delete code
# SRomo, 2020-Aug-11, Updated append to write in the txt file
#------------------------------------------#

# Declare variables

strChoice = '' # User input
lstTbl = []  # list of dicts to hold data
dictRow = {} # dictionary of data row
strFileName = 'CDInventory.txt'  # data storage file
objFile = None  # file object

# Get user Input
print('The Magic CD Inventory\n')
while True:
    # 1. Display menu allowing the user to choose:
    print('[l] Load Inventory from file')
    print('[a] Add CD')
    print('[i] Display Current Inventory')
    print('[d] Delete CD from Inventory')
    print('[s] Save Inventory to file')
    print('[x] exit')
    
    strChoice = input('l, a, i, d, s or x: ').lower()  # convert choice to lower case at time of input
    print()

    if strChoice == 'x':
        # 5. Exit the program if the user chooses so
        break
   
    if strChoice == 'l':
        # read data from a file and append it to the in-memory list
        objFile = open(strFileName, 'r')
        for row in objFile:
            lstRow = row.strip().split(',')
            dictRow = {'id':lstRow[0],'album':lstRow[1],'artist':lstRow[2]}
            lstTbl.append(dictRow)
        objFile.close()
        
        pass
   
    elif strChoice == 'a':  # no elif necessary, as this code is only reached if strChoice is not 'exit'
        # 2. Add data to the table (2d-list) each time the user wants to add data
        strID = input('Enter an ID: ')
        strTitle = input('Enter the CD\'s Title: ')
        strArtist = input('Enter the Artist\'s Name: ')
    
        dictRow = {'id':strID,'album':strTitle,'artist':strArtist}
        lstTbl.append(dictRow)
        
        print('Your CD was added to inventory.\n')

        pass
    
    elif strChoice == 'i':
        # 3. Display the current data to the user each time the user wants to display the data
        if lstTbl == []:
            print('There\'s no data in the table.\n')
        
        else:
            print('ID, CD Title, Artist')
            for row in lstTbl:
                print(*row.values(), sep = ', ')
            print()
        
        pass
    
    elif strChoice == 'd':
        # Delete an entry from the tabl
        strID = input('Enter the ID of the CD you\'d like to remove: ')
        
        for row in lstTbl:
            if strID in row.values():
                lstTbl.remove(row)
            
        pass
    
    elif strChoice == 's':
        # 4. Save the data to a text file CDInventory.txt if the user chooses so
        objFile = open(strFileName, 'w')
        for row in lstTbl:
            strRow = ''
            for item in row.values():
                strRow += str(item) + ','
            strRow = strRow[:-1] + '\n'
            objFile.write(strRow)
        objFile.close()
        
        print('Your Inventory was saved to file.\n')
    
        pass
    
    else:
        print('Please choose either l, a, i, d, s or x!')

