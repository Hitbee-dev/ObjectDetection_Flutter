import glob

fnames = ['test', 'train', 'val']
for fname in fnames:
    file_name = [] # 파일 이름
    file_data = [] # 파일 내부 데이터
    names = ["CheerUp", "Stop",  "This",  "OneMore", "Ok",  "ThisMore",  "No", "Promise", "Victory", "Little",  "GoodLuck",  "Call",  "You"]
    file_path = f'C:/Users/HNU/Documents/github/ObjectDetection_Flutter/datasets/{fname}/labels/'
    file_name = glob.glob(file_path + '*.txt')

    for i, file in enumerate(file_name): # 파일 이름만 잘라내기
        file_name[i] = file.split('labels\\')[1]
    # print(file_name)

    for i in range(len(file_name)): # 파일 열어서 내부 데이터 읽기
        with open(file_path+file_name[i], 'r') as f:
            file_data.append(f.read())
    # print(file_data)

    for i in range(len(file_name)): # 파일 내부 데이터 변경
        buf = []
        result = ""
        for j in range(len(names)): # names 리스트에 있는 단어를 파일 내부 데이터에서 찾아서 변경
            if names[j] in file_name[i]:
                buf = file_data[i].split(' ')
                buf[0]=str(j)
                result = f"{buf[0]} {buf[1]} {buf[2]} {buf[3]} {buf[4]}" # 원래 형식으로 맞춰서 다시 저장

                with open(file_path+file_name[i], 'w') as f:
                    f.write(result)
                print(result)