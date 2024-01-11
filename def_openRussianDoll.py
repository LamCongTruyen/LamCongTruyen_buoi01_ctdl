def openRussianDoll(doll):#đây là khai báo của hàm 'openRussianDoll' với biến đầu vào là 'doll'
        if doll == 1:#dây là một dòng lệnh điều kiện dừng,nếu số lượng(kích thước) búp bê cần mở bằng 1 thì dừng chương trình
            print("All dolls are opened")#in ra màn hình "tất cả búp bê đã được mở" nếu điều kiện trên thõa
        else:#khác với điều kiện if(n không bằng 1) thì nếu biến 'doll' không thõa điều kiện if thì tiếp tục thực hiện các dòng lệnh bên dưới(dòng lệnh đệ quy)
            openRussianDoll(doll-1)#hàm sẽ gọi lại chính nó(đệ quy) với biến doll giảm đi 1 cho đến khi bằng điều kiện dừng