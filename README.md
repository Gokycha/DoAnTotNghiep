Đây là Git của Phạm Duy Tuấn để làm đồ án tốt nghiệp. Nếu nó được Public thì nghĩa là tôi đã thành công :)))

Thời gian bắt đầu: 05/10/2023

Thời gian kết thúc (dự kiến): 12/2023

# ĐỒ ÁN TỐT NGHIỆP
**<br>Đề tài: Dùng thuật toán di truyền để tìm trọng số cho mạng nơ-ron tế bào</br>
<br>Sinh viên: Phạm Duy Tuấn</br>
<br>Mã sinh viên: B19DCCN618</br>
<br>Lớp: B19CNPM02</br>
<br>Giáo viên hướng dẫn: Nguyễn Quang Hoan</br>**

## Mục lục
<br>[Các thuật ngữ](#ThuatNgu)</br>
<br>[Tài liệu](#TaiLieu)</br>

===================================
<a name="ThuatNgu"></a>
## Các thuật ngữ
- Thuật toán di truyền
- Mạng nơ-ron tế bào (cellular neural networks)
- Trọng số trong mạng nơ-ron tế bào
- Tích chập hai ma trận (convolve)
- Phương trình vi phân thường: ODE

<a name="TaiLieu"></a>
## Các tài liệu
- [Phương pháp Adams để giải phương trình vi phân](https://mathworld.wolfram.com/AdamsMethod.html)
- [Github project tham khảo](https://github.com/ankitaggarwal011/PyCNN)


Thuật toán hiện tại đang được sử dụng:
- Xét lần lượt từng trọng số trong quần thể.
- Tối ưu trọng số đó.
- Chạy cho đến khi nào E <= E0

Thuật toán tối ưu một trọng số
- Tạo ngẫu nhiên S cặp cha mẹ.
- Với mỗi cặp cha mẹ, lai được một con, đưa con vào quần thể thay cho trọng số đang xét. Tính lại ma trận đầu ra và sai số.  
- Tìm ra con trong S cặp cha mạ mà khi thay vào quần thể cho ra trọng số nhỏ nhất.
- So sánh Emin với E (sai số hiện tại), nếu nhỏ hơn, cập nhật lại toàn bộ dữ liệu theo trọng số con. Nếu không, giữ nguyên toàn bộ.
