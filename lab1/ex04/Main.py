from QuanLySinhVien import QuanLySinhVien

qlsv = QuanLySinhVien()

while (1 == 1):
    print("CHUONG TRINH QUAN LY SINH VIEN")
    print("************************MENU************************")
    print("1. Them sinh vien")
    print("2. Cap nhat thong tin sinh vien boi id")
    print("3. Xoa sinh vien boi id")
    print("4. Tim kiem sinh vien theo ten")
    print("5. Sap xep sinh vien theo diem trung binh")
    print("6. Sap xep sinh vien theo ten ")
    print("7. Hien thi danh sach sinh vien")
    print("0. Thoat chuong trinh")
    print("***************************************************")
    
    key = int(input("Nhap lua chon cua ban: "))
    if(key == 1):
        print("\n1. Them sinh vien")
        qlsv.nhapSV()
        print("\nThem sinh vien thanh cong.")
    elif(key == 2):
        if(qlsv.soLuongSV() > 0):
            print("\n2. Cap nhat thong tin sinh vien boi id")
            print("\nNhap ID: ")
            ID = int(input())
            qlsv.updateSV()
            print("\nCap nhat thong tin sinh vien thanh cong.")
        else:
            print("\nDanh sach sinh vien rong.")
    elif(key == 3):
        if(qlsv.soLuongSV() > 0):
            print("\n3. Xoa sinh vien boi id")
            print("\nNhap ID: ")
            ID = int(input())
            if(qlsv.deleteByID(ID)):
                print("\nXoa sinh vien thanh cong.")
            else:
                print("\nKhong tim thay sinh vien.")
        else:
            print("\nDanh sach sinh vien rong.")
    elif(key == 4):
        if(qlsv.soLuongSV() > 0):
            print("\n4. Tim kiem sinh vien theo ten")
            print("\nNhap ten: ")
            name = input()
            listSV = qlsv.findByName(name)
            if(len(listSV) > 0):
                print("\nDanh sach sinh vien tim thay:")
                print("\nNhap ten de tim kiem: ")
                name = input()
                searchResult = qlsv.findByName(name)
                qlsv.showListSV(searchResult)
            else:
                print("\nDanh sach sinh vien rong.")
    elif(key == 5):
        if(qlsv.soLuongSV() > 0):
            print("\n5. Sap xep sinh vien theo diem trung binh")
            qlsv.sortbyGPA()
            qlsv.showSinhVien(qlsv.getListSV())
        else:
            print("\nDanh sach sinh vien rong.")
    elif(key == 6):
        if(qlsv.soLuongSV() > 0):
            print("\n6. Sap xep sinh vien theo ten")
            qlsv.sortbyName()
            qlsv.showSinhVien(qlsv.getListSV())
        else:
            print("\nDanh sach sinh vien rong.")
    elif(key == 7):
        if(qlsv.soLuongSV() > 0):
            print("\n7. Hien thi danh sach sinh vien")
            qlsv.showSinhVien(qlsv.getListSV())
        else:
            print("\nDanh sach sinh vien rong.")
    elif(key == 0):
        print("\nBan da chon thoat chuong trinh.")
        break
    else:
        print("\nLua chon khong hop le.")
        
