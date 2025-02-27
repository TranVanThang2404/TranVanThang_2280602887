from QuanLySinhVien import QuanLySinhVien

qlsv = QuanLySinhVien()

while True:
    print("CHƯƠNG TRÌNH QUẢN LÝ SINH VIÊN")
    print("************************MENU************************")
    print("1. Thêm sinh viên")
    print("2. Cập nhật thông tin sinh viên theo ID")
    print("3. Xóa sinh viên theo ID")
    print("4. Tìm kiếm sinh viên theo tên")
    print("5. Sắp xếp sinh viên theo điểm trung bình")
    print("6. Sắp xếp sinh viên theo tên")
    print("7. Hiển thị danh sách sinh viên")
    print("0. Thoát chương trình")
    print("***************************************************")

    key = int(input("Nhập lựa chọn của bạn: "))
    if key == 1:
        print("\n1. Thêm sinh viên")
        qlsv.nhapSV()
        print("\nThêm sinh viên thành công.")
    elif key == 2:
        if qlsv.soLuongSV() > 0:
            print("\n2. Cập nhật thông tin sinh viên theo ID")
            ID = int(input("Nhập ID sinh viên cần cập nhật: "))
            qlsv.updateSV(ID)
        else:
            print("\nDanh sách sinh viên rỗng.")
    elif key == 3:
        if qlsv.soLuongSV() > 0:
            print("\n3. Xóa sinh viên theo ID")
            ID = int(input("Nhập ID sinh viên cần xóa: "))
            if qlsv.deleteByID(ID):
                print("\nXóa sinh viên thành công.")
            else:
                print("\nKhông tìm thấy sinh viên.")
        else:
            print("\nDanh sách sinh viên rỗng.")
    elif key == 4:
        if qlsv.soLuongSV() > 0:
            print("\n4. Tìm kiếm sinh viên theo tên")
            name = input("Nhập tên sinh viên cần tìm: ")
            listSV = qlsv.findByName(name)
            if len(listSV) > 0:
                print("\nDanh sách sinh viên tìm thấy:")
                qlsv.showSinhVien(listSV)
            else:
                print("\nKhông tìm thấy sinh viên.")
        else:
            print("\nDanh sách sinh viên rỗng.")
    elif key == 5:
        if qlsv.soLuongSV() > 0:
            print("\n5. Sắp xếp sinh viên theo điểm trung bình")
            qlsv.sortbyGPA()
            qlsv.showSinhVien(qlsv.getListSV())
        else:
            print("\nDanh sách sinh viên rỗng.")
    elif key == 6:
        if qlsv.soLuongSV() > 0:
            print("\n6. Sắp xếp sinh viên theo tên")
            qlsv.sortbyName()
            qlsv.showSinhVien(qlsv.getListSV())
        else:
            print("\nDanh sách sinh viên rỗng.")
    elif key == 7:
        if qlsv.soLuongSV() > 0:
            print("\n7. Hiển thị danh sách sinh viên")
            qlsv.showSinhVien(qlsv.getListSV())
        else:
            print("\nDanh sách sinh viên rỗng.")
    elif key == 0:
        print("\nBạn đã chọn thoát chương trình.")
        break
    else:
        print("\nLựa chọn không hợp lệ.")