def giaithua(n):#tạo hàm giai thừa với biến n
    if n == 0 or n ==1:#đặt điều kiện dừng
        return 1#trả về 1 nếu n bằng 1 hoặc 0
    else:
        return n*giaithua(n-1)#nếu điều kiện chưa thõa trả vè giá trị: n*n-1
    
a = giaithua(4)#khai báo biến n đồng thời gán hàm giaithua cho biến a 
print(f"giai thua cua {4} la : ")#in ra màn hình thông điệp và dùng f để nhúng giá trị 4 trực tiếp vào chuỗi 
print(a)#in ra màn hình kết quả