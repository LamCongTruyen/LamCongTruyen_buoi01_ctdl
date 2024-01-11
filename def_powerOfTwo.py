def powerOfTwo(n):#định nghĩa hàm powerOfTwo
    if n == 0:#nếu n bằng 0(điều kiện dừng)
        return 1#trả về 1
    else:#khác với điều kiện if
        power = powerOfTwo(n-1)#gọi hàm là chính nó với biến n giảm đi 1 
        return power*2 #sau khi nhân với 2 và trả về chính giá trị đấy
    #khi n giảm xuống đến 0, các giá trị sẽ được trả về từ cuối lên đầu:
    #powerOfTwo(0) trả về 1
    #powerOfTwo(1) bằng powerOfTwo(0)*2 trả về 2
    #powerOfTwo(2) bằng powerOfTwo(1)*2 trả về 4
    #powerOfTwo(3) bằng powerOfTwo(2)*2 trả về 8
    #powerOfTwo(4) bằng powerOfTwo(3)*2 trả về 16
a = powerOfTwo(4)#gán giá trị sau khi trả về của hàm powerOfTwo(4) vào biến a
print(a)#in giá trị biến a ra màn hình
