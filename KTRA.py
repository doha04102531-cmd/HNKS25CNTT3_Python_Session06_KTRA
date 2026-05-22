don_gia = int(input('Hãy nhập vào đơn giá của sản phẩm: '))
so_luong = int(input('Hãy nhập vào số lượng sản phẩm muốn mua: '))

tong_tien = don_gia * so_luong
if tong_tien > 1000000:
    tong_tien = int(tong_tien -(tong_tien * 0.1))
elif tong_tien < 1000000:
    print("Đơn hàng của bạn chưa đủ điều kiện giảm giá!")

print(f'Số tiền quý khách cần thanh toán là: {tong_tien:,} VND')