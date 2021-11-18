if __name__ == '__main__':
    documents = [
        {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
        {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
        {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
    ]

    directories = {
        '1': ['2207 876234', '11-2'],
        '2': ['10006'],
        '3': []
    }

    def p_find_name_with_doc_num(num_to_find):
        no_doc = True
        for document in documents:
            if document['number'] == num_to_find:
                print(document['name'])
                no_doc = False
        if no_doc:
            print("Документ с таким номером не найден")   

    def s_find_shelf_with_doc_num(num_to_find):        
        no_doc = True
        for key in directories:
            if num_to_find in list(directories[key]):
                print(key)
                no_doc = False
        if no_doc:
            print("Документ с таким номером не найден")      

    def l_get_list_of_all_docs():
        for document in documents:
            print(f" {document['type']} {document['number']} {document['name']}")      

    def a_add_new_doc():        
        print("Ввод нового документа:")
        temp_doc = {}
        temp_doc.update({"type": input("Введите тип документа: ")})
        temp_doc.update({"number": input("Введите номер документа: ")})
        temp_doc.update({"name": input("Введите имя: ")})        
        dir_num = input("Введите номер полки: ")
        if dir_num in list(directories.keys()):            
            documents.append(temp_doc)          
            
            temp_dir = directories.get(dir_num)
            temp_dir.append(temp_doc["number"])
            print(">>", temp_dir)
            directories.update({dir_num : temp_dir})
        else:            
            yn = input("Полка не найдена, создать новую? (y/n) ")
            if yn == "y":
                documents.append(temp_doc)
                directories.update({dir_num : [temp_doc["number"]]}) 
            else:
                 print("Документ не внесён")
        
        
    def user_command():    
        command_char = input("Введите команду: ")
        if command_char == "p":
            p_find_name_with_doc_num(input("Введите номер документа: "))
        elif command_char == "s":
            s_find_shelf_with_doc_num(input("Введите номер документа: "))
        elif command_char == "l":               
            print("Зарегистрированные документы:")
            l_get_list_of_all_docs()  
        elif command_char == "a":
            a_add_new_doc()
        else:
            print("Команда не найдена")
        print()

    while True:
        user_command()
        
