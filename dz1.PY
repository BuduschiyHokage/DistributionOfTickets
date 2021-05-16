StrSum = [] #массив в который записываем численную сумму букв в строке
Tickets = [] #массив в который залетают билеты с возможными повторами 
TicketsWithoutCollisions = [] #массив в котором все повторяющиеся билеты начиная со второго попадания = 0
RecurringTickets = [] #массив в который залетают значения тех билетов которые в с[] = 0

quantity = int(input('введите число билетов: '))
key = int(input('введите параметр: '))

str_sum = 0
file_sum = 0
n = 0

try:
    with open('/home/hokage/Tickets/test_1', "r") as f:
        #считываем файл и получаем численную сумму строк и всего файла              
        for line in f.read():                       
            str_sum += ord(line)
            if line == '\n':
                StrSum.append(str_sum)
                n += 1
                file_sum += str_sum
                str_sum = 0
        i = 0
        f.seek(0)
        for x in range(quantity):
            TicketsWithoutCollisions.append(0)
        for line in f:
            ticket = ((file_sum % StrSum[i]) ^ key + i) % quantity + 1
            Tickets.append(ticket)
            if TicketsWithoutCollisions[ticket - 1] == 0:
                TicketsWithoutCollisions[ticket - 1] = ticket
            else:
                RecurringTickets.append(ticket)
            i += 1
            ticket = 0
        if quantity >= n:
            #очищаем массив Tickets от элементов массива d и очищаем массив d
            for i in Tickets:
                if len(RecurringTickets) != 0:
                    if i == RecurringTickets[0]:
                        Tickets.remove(i)
                        RecurringTickets.remove(i)
            if len(RecurringTickets) != 0:
                Tickets.remove(RecurringTickets[0])
            #добавляем в конец массива Tickets все неиспользованные номера билетов
            number = 1
            for i in TicketsWithoutCollisions:
                if i == 0:
                    Tickets.append(number)
                number += 1
            #выводим людей с номерами билетов
            i = 0
            f.seek(0)
            for line in f:
                print(line[0:len(line)-1],":", Tickets[i])
                i += 1
        else:
            i = 0
            f.seek(0)
            for line in f:
                print(line[0:len(line)-1],":", Tickets[i])
                i += 1
except FileNotFoundError:
    print("File not found!")



        
      

    


        
    
