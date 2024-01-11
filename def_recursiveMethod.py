def  recursiveMethod(n):#khai báo một hàm đệ quy với biến n
    if n<1:#đặt điều kiện dừng cho hàm đệ quy
        print("n is less than 1")#nếu n nhập vào nhỏ hơn 1 sẽ in ra thông điệp 'n less than 1'
    else:#trong trường hợp điều kiện khác với điều kiện if
        recursiveMethod(n-1)#hàm sẽ gọi lại chính nó với biến n-1
        print(n)#sau đó in ra giá trị của n
        #ví dụ:khi nhập n =5,chương trình sẽ so sánh với 1, sau đó gọi hàm recursiveMethod(4) và in 5 ra màn hình.
        #sau đó chương trình lại so sánh biến trong hàm recursiveMethod hiện tại là 4 với 1,nếu vẫn lớn hơn sẽ gọi hàm recursiveMethod(3) và in 4 ra màn hình.
        #tiếp tục so sánh(lúc này biến n là 3) và gọi hàm recursiveMethod(2) vì 3 vẫn còn lớn hơn 1 kết hợp với in 3 ra màn hình.
        #tiếp tục cách giải thích như vậy đến khi n bằng 0, lúc này n nhỏ hơn 1(thõa điều kiện dừng)chương trình sẽ in ra màn hình thông điệp"less than 1".
        #kết quả là 1 dãy số từ lớn đến nhỏ được in lần lượt ra màn hình.