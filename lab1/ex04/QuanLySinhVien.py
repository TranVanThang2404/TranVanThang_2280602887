from SinhVien import SinhVien

class QuanLySinhVien:
    listSV = []

    def generateID(self):
        maxId = 1
        if self.soLuongSV() > 0:
            maxId = self.listSV[0]._id
            for sv in self.listSV:
                if maxId < sv._id:
                    maxId = sv._id
            maxId += 1
        return maxId

    def soLuongSV(self):
        return len(self.listSV)

    def nhapSV(self):
        id = self.generateID()
        name = input("Nhập tên sinh viên: ")
        sex = input("Nhập giới tính: ")
        major = input("Nhập ngành học: ")
        gpa = float(input("Nhập điểm trung bình: "))
        sv = SinhVien(id, name, sex, major, gpa)
        self.listSV.append(sv)

    def updateSV(self, ID):
        sv = self.findByID(ID)
        if sv:
            sv._name = input("Nhập tên sinh viên mới: ")
            sv._sex = input("Nhập giới tính mới: ")
            sv._major = input("Nhập ngành học mới: ")
            sv._gpa = float(input("Nhập điểm trung bình mới: "))
            sv._hocluc = sv.XepLoaiHocLuc(sv._gpa)  # Cập nhật học lực
            print("Cập nhật thành công!")
        else:
            print("Không tìm thấy sinh viên.")

    def sortbyID(self):
        self.listSV.sort(key=lambda x: x._id)

    def sortbyName(self):
        self.listSV.sort(key=lambda x: x._name)

    def sortbyGPA(self):
        self.listSV.sort(key=lambda x: x._gpa)

    def findByID(self, ID):
        for sv in self.listSV:
            if sv._id == ID:
                return sv
        return None

    def findByName(self, name):
        result = []
        for sv in self.listSV:
            if sv._name == name:
                result.append(sv)
        return result

    def deleteByID(self, ID):
        sv = self.findByID(ID)
        if sv:
            self.listSV.remove(sv)
            return True
        return False

    def showSinhVien(self, listSV):
        print("{:<8} {:<18} {:<8} {:<8} {:<8} {:<8}".format("ID", "Tên", "Giới tính", "Ngành học", "Điểm TB", "Học lực"))
        for sv in listSV:
            print("{:<8} {:<18} {:<8} {:<8} {:<8} {:<8}".format(sv._id, sv._name, sv._sex, sv._major, sv._gpa, sv._hocluc))

    def getListSV(self):
        return self.listSV
