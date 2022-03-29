def solution(logs):
    answer=0
    for i in range(len(logs)):
        tmp=logs[i]
        flag=True
        #로그의 길이
        if (len(tmp) > 101):
            flag = False

        #공백 체크
        if (tmp[0] == ' '):
            flag = False

        tmp = tmp.split()
        # 입력 사항 체크
        if (len(tmp)==12 and tmp[0] != 'team_name' and tmp[3] != 'application_name' and tmp[6] != 'error_level' and tmp[9] != 'message'):
            flag = False

        #알파벳 체크
        if(len(tmp)==12 and (tmp[2].isalpha()==False or tmp[5].isalpha()==False or tmp[8].isalpha()==False or tmp[11].isalpha()==False)):
            flag = False

        for j in range(len(tmp)-1):
            #공백 체크
            if(tmp[j]==' ' and tmp[j+1]==' '):
                flag = False
                break

            #길이 체크
            if(len(tmp[0])>201):
                flag=False
                break

            if(len(tmp[j+1])>201):
                flag=False
                break

        if(flag==False):
            answer=answer+1

    return answer

print(solution(["team_name : db application_name : dbtest error_level : info message : test",
                "team_name : test application_name : I DONT CARE error_level : error message : x",
                "team_name : ThisIsJustForTest application_name : TestAndTestAndTestAndTest error_level : test message : IAlwaysTestingAndIWillTestForever",
                "team_name : oberervability application_name : LogViewer error_level : error"]))

print(solution(["team_name : MyTeam application_name : YourApp error_level : info messag : IndexOutOfRange",
                "no such file or directory",
                "team_name : recommend application_name : recommend error_level : info message : RecommendSucces11",
                "team_name : recommend application_name : recommend error_level : info message : Success!",
                "   team_name : db application_name : dbtest error_level : info message : test",
                "team_name     : db application_name : dbtest error_level : info message : test",
                "team_name : TeamTest application_name : TestApplication error_level : info message : ThereIsNoError"]))