my_list=[]
while True:
    print('welcome to our address book,please to find what you want')
    print('1. Add new contact')
    print('2. search by name')
    print('3. search by number ')
    print('4. Delet contact by name')
    print('5. delet contact by number')
    print('6. show all my_list')
    print('7. exit')
    
    choice= input ('pleas to enter your choice:')
    if choice=='1':
        name=input('enter name:')
        ctype=input('enter type:')
        number=input ('enter number:')
        
        exists= False
        for contact in my_list:
            if contact[2]==number:
                exists= True
                break
        if exists:
            print('number already exists, process.')
        else:
            my_list.append([name,ctype,number])
            print('contact added.')
    elif choice=='2':
        sarch_name=input('enter contact name to find:')
        found= False
        for contact in my_list:
            if sarch_name in contact[0]:
                print(contact)            
                found=True
        if not found:
            print('no matches found.')
            
    elif choice=='3':
        sarch_num=input ('enter contact number to find.')
        found=False
        for contact in my_list:
            if sarch_num == contact[2]:
               print(contact)
               found =True
        if not found :
            print('no matches found')
            
    elif choice=='4':
        del_name=input('enter name to delete:')
        found=False
        for i in range(len(my_list)):
            if my_list [i][0]==del_name:
                my_list.pop(i)
                print('contact deleted.')
                found=True
                break 
            if not found:
                print('contact not found.')
                
    elif choice=='5':
       del_num=input('enter number to delete')
       found=False
       for i in range(len(my_list)):
           if my_list[i][2]==del_num:
               my_list.pop(i)
               print('contact deleted.')
               found=True
               break
           if not found:
               print('contact not found.')
               
    elif choice=='6':
        if not my_list:
            print('no my_list available.')
        else:
            for contact in my_list:
                print(contact)
                
    elif choice=='7':
        print('good bye!')
        break
    
    else:
        print('invalid choice, please try again.')                                     
            