class SinhVien:
    def __init__(self, id, name, sex, major, gpa):
        self._id = id
        self._name = name
        self._sex = sex
        self._major = major
        self._gpa = gpa
        self._hocluc = self.XepLoaiHocLuc(gpa)  # Gán học lực ngay khi tạo đối tượng
    
    def XepLoaiHocLuc(self, gpa):
        if gpa >= 9.0:
            return "Xuất sắc"
        elif gpa >= 8.0:
            return "Giỏi"
        elif gpa >= 7.0:
            return "Khá"
        elif gpa >= 5.0:
            return "Trung bình"
        else:
            return "Yếu"