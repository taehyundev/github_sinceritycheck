import pandas

def w_csv(path, data, name): 
    print(1)
    with open(path, 'w') as file:    # weather.csv 파일을 쓰기 모드로 열기
        print(1)
        file.write(name+'\n\n')                  # 컬럼 이름 추가
        for i in data:                                              # data를 반복하면서
            file.write('{0},{1}\n'.format(i[0], i[1])) 