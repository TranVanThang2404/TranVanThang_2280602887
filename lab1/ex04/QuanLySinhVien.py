from SinhVien import SinhVien

class QuanLySinhVien:
    listSV = []
    
    def generateID(self):
        maxId = 1
        if (self.soLuongSV() > 0):
            maxId = self.listSV[0]._id
            for sv in self.listSV:
                if (maxId < sv._id):
                    maxId = sv._id
            maxId = maxId + 1
        return maxId
    
    def soLuongSV(self):
        return self.listSV.__len__()
    
    def nhapSV(self):
        id = self.generateID()
        name = input("Nhập tên sinh viên: ")
        sex = input("Nhập giới tính: ")
        major = input("Nhập ngành học: ")
        gpa = float(input("Nhập điểm trung bình: "))
        sv = SinhVien(id, name, sex, major, gpa)
        self.XepLoai(sv)
        self.listSV.append(sv)
        
    def updateSV(self):
        sv: SinhVien = self.timSVTheoID()
        if (sv != None):
            name = input("Nhập tên sinh viên: ")
            sex = input("Nhập giới tính: ")
            major = input("Nhập ngành học: ")
            gpa = float(input("Nhập điểm trung bình: "))
            sv._name = name
            sv._sex = sex
            sv._major = major
            sv._gpa = gpa
            self.XepLoai(sv)
        else:
            print("Không tìm thấy sinh viên.")
    
    def sortbyID(self):
        self.listSV.sort(key=lambda x: x._id, reverse=False)
        
    def sortbyName(self):
        self.listSV.sort(key=lambda x: x._name, reverse=False)
        
    def sortbyGPA(self):
        self.listSV.sort(key=lambda x: x._gpa, reverse=False)
        
    def findByID(self, ID):
        searchResult = None
        if(self.soLuongSV() > 0):
            for sv in self.listSV:
                if (sv._id == ID):
                    searchResult = sv
        return searchResult
    
    def findByName(self, name):
        listSV = []
        if(self.soLuongSV() > 0):
            for sv in self.listSV:
                if (sv._name == name):
                     listSV.append(sv)
        return listSV
    
    def deleteByID(self, ID):
        isDeleted = False
        sv = self.findByID(ID)
        if (sv != None):
            self.listSV.remove(sv)
            isDeleted = True
        return isDeleted
    
    def XepLoaiHocLuc(self, sv: SinhVien):
        if (gpa >= 9.0):
            return "Xuất sắc"
        elif (gpa >= 8.0):
            return "Giỏi"
        elif (gpa >= 7.0):
            return "Khá"
        elif (gpa >= 5.0):
            return "Trung bình"
        else:
            return "Yếu"
        
    def showSinhVien(self, listSV):
        print("{:<8} {:<18} {:<8} {:<8} {:<8} {:<8} ".format("ID", "Tên", "Giới tính", "Ngành học", "Điểm TB", "Học lực"))
        if(listSV.__len__() > 0):
            for sv in listSV:
                print("{:<8} {:<18} {:<8} {:<8} {:<8} {:<8} ".format(sv._id, sv._name, sv.sex, sv._major, sv._gpa, sv._hocLuc))
        print("\n")
        
    def getListSV(self):
        return self.listSV
    