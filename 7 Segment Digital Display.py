list = [['###','# #','# #','# #','###'],['  #','  #','  #','  #','  #'],['###','  #','###','#  ','###'],['###','  #','###','  #','###'],['# #','# #','###','  #','  #'],['###','#  ','###','  #','###'],['###','#  ','###','# #','###'],['###','  #','  #','  #','  #'],['###','# #','###','# #','###'],['###','# #','###','  #','###']]   
val = input()


for i in range(5):
    k = 0
    while k<len(val):
        if val[k] == '0':
            print(list[0][i],end=" ")
            k+=1
        elif val[k] == '1':
            print(list[1][i],end=" ")
            k+=1
        elif val[k] == '2':
            print(list[2][i],end=" ")
            k+=1
        elif val[k] == '3':
            print(list[3][i],end=" ")
            k+=1
        elif val[k] == '4':
            print(list[4][i],end=" ")
            k+=1
        elif val[k] == '5':
            print(list[5][i],end=" ")
            k+=1
        elif val[k] == '6':
            print(list[6][i],end=" ")
            k+=1
        elif val[k] == '7':
            print(list[7][i],end=" ")
            k+=1
        elif val[k] == '8':
            print(list[8][i],end=" ")
            k+=1
        elif val[k] == '9':
            print(list[9][i],end=" ")
            k+=1

    print()
