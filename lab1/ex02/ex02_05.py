sogiolam = float(input("Nhập số giờ làm mỗi tuần:  "))
luonggio = float(input("Nhập lương mỗi giờ:  "))
giotieuchuan = 44 
giovuotchuan = max(0, sogiolam - 44)
thuclinh = giotieuchuan * luonggio + luonggio * giovuotchuan * 1.5
print(f"Lương của bạn là: ", {thuclinh})