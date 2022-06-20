T=int(input())

for _ in range(T):
    all_ani=input()
    all_ani_say=all_ani.split( )

    tmp=input()
    while tmp!='what does the fox say?':
        animal = tmp.split( )

        if animal[2] in all_ani_say:
            while animal[2] in all_ani_say:
                all_ani_say.remove(animal[2])
        else:
            continue

        tmp=input()

    answer=''
    for i in all_ani_say:
        answer=answer+i+' '

    print(answer)