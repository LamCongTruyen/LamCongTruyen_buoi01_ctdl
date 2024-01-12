
a = int(input())#nhập a(cơ số)
n = int(input())#nhập n(số lũy thừa)
def luythua(a,n):#tạo hàm đệ quy với biến là n
    if n == 0:#đặt điều kiện dừng nếu n bằng 0 trả về kết quả là 1
        return 1
    else:
        return a * luythua(a,n-1)#nếu không thõa thì gọi chính nó với biến n giảm đi 1 và nhân với n
    
b = luythua(a,n)#gán giá trị của hàm vào biến b
print(f"ket qua cua phep tinh la : {b}")#in ra màn hình
