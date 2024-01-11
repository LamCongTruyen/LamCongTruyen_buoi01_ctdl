n = int(input())#nhập số nguyên dương cần tính tổng các chữ số

def sum(n):#khởi tạo hàm tính tổng với biến n
    if n < 10:#đặt điều kiện dừng
        return n#neu n nho hon 10 thi tong can tinh bang chinh no
    else:
        return  sum(n%10)       +     sum(n//10)                #nếu không thì tổng bằng tổng của phần nguyên và phần dư của số đó sau khi chia cho 10
           #(phép chia lấy dư)   #(phép chia lấy nguyên)        #thực hiện chia 10 để lấy phần dư đến khi nào n nho hơn 10 thi dừng lại
    
a = sum(n) #gán kết quả của tổng cho biến a
print(f"tong cua cac chu so cua so nguyen duong {n} la: {a}")#in ra màn hình