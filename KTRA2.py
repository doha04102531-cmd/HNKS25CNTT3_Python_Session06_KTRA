mat_khau = "123456"
limit = 3
count = 0

for dang_nhap in range(limit):
   input_mk = int(input('Vui lòng nhập mật khẩu: '))

if input_mk != mat_khau:
        print('Mật khẩu sai,vui lòng nhập lại!')
        count += 1

elif input_mk == mat_khau:
        print('Đăng nhập thành công')
        beark

if count == 3 :
    print('Tài khoản bị vô hiệu khóa!')







