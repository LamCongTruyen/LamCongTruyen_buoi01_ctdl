def firstMethod():#định nghĩa hàm 'firstMethod'
        secondMethod()#gọi hàm 'secondMethod'(bỏ qua bước in,nhảy đến thực hiện hàm 'secondMethod')
        print("I am the first Method")#sau đó in ra màn hình thông điệp 'I am the first Method'
def secondMethod():#định nghĩa hàm 'secondMethod'
        thirdMethod()#gọi hàm 'thirdMethod'(nhảy đến thực hiện hàm 'thirdMethod')
        print("I am the second Method")#in ra màn hình thông điệp 'I am the second Method'
def thirdMethod():#định nghĩa hàm 'thirdMethod'
        fourthMethod()#gọi hàm'fourthMethod'(nhảy đến thực hiện hàm 'fourthMethod')
        print("I am the third Method")#tương tự như cách giải thích ở lệnh print của hàm 'fourthMethod',sau khi in ra thông điệp 'I am the thirthMethod'
                                      #chương trình sẽ quay về lại lệnh in ở hàm 'secondMethod'
def fourthMethod():#định nghĩa hàm 'fourthMethod' 
        print("I am the fourth Method")#vì code chạy theo thứ tự gọi tuần tự cho nên tại đây sau khi gọi hàm fourth không còn hàm nào gọi nữa 
                                       #nên sẽ thực hiện lệnh in ra màn hình thông điệp 'i am the fourthMethod' và sau khi lệnh này được thực
                                       #hiện chương trình sẽ quay về lại lệnh in thông điệp 'I am the third Method',vì sau khi nhảy đến hàm 
                                       #'fourthMethod' vẫn còn 1 lệnh in chưa được thực hiện