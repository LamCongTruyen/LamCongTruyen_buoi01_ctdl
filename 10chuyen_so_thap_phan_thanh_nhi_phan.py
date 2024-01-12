n = int(input())#nhap vao so n
def  DecimaltoBinary(n):#tạo hàm chia nhị phân
    if n <= 1:#đặt điều kiện nếu nhập n bé hơn 1 thì nhị phân bằng chính nó
        return n
    else:#nếu >1
        return n%2 + 10*DecimaltoBinary(n//2)#thực hiện đệ quy bằng cách lấy phần dư của phép chia lấy dư n cho 2 cộng cho phép nhân 10 với phần nguyên của phép chia n//2
a = DecimaltoBinary(n)
print(f"ma nhi phan cua so thap phan {n} la: {a}")#in ra màn hình