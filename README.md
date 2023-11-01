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

Tiến độ hiện tại với mạng Nơ-ron tế bào bậc nhất (CeNN) chạy GA lai
- Về ma trận đầu vào:
  - Ma trận đầu vào 10x10 luôn cho ra được bộ trọng số có thể dùng để lọc biên. 
  - Dùng ma trận đầu vào 12x12 trở lên thì chắc chắn sẽ bị lỗi phương trình vi phân.
  - Ma trận đầu vào 8x8 không gặp lỗi, tìm ra trọng số rất nhanh nhưng chỉ có 25% bộ trọng số tìm được là có thể dùng để lọc biên.
  - Ma trận đầu vào 6x6 trở xuống thì không cho ra bộ trọng số có thể lọc biên.
  - Nhận xét: Ma trận đầu vào 10x10 là tốt nhất (trong code [demo](/MangNoronTeBaoBacNhat.ipynb) thì ảnh đầu vào u2 là ma trận 10x10)
- Về bộ trọng số:
  - Các bộ trọng số có thể dùng để lọc biên nằm trong file [TrongSoBac1ToiUu](/TrongSoBac1ToiUu) (chỉ lưu trọng số sau khi chạy, không lưu trọng số ban đầu)
  - Từ bộ trọng số thứ nhất đến thứ 8 đều được chạy với bộ trọng số ban đầu ngẫu nhiên
  - Từ bộ thứ 9 trử đi, trọng số ban đầu được dùng là A=[[0,0,0],[0,2,0],[0,0,0]], B=[[0,0,0],[0,0,0],[0,0,0]], I=-1.
- Về các tham số khác:
  - Sai số E0: 4.0
  - Số bộ cha mẹ mỗi lần xét một trọng số: 20
  - Nhận xét: Việc tăng số lượng bộ cha mẹ sẽ làm tăng thời gian chạy của vòng lặp nhỏ (tối ưu một trọng số). Nhưng làm giảm số lần chạy của vòng lặp lớn (duyệt toàn bộ các trọng số trong quần thể). Con số tối ưu cho số lượng cha mẹ là khoảng 20.
- Kết luận chung: Kết quả tốt, tìm được nhiều bộ trọng số có thể lọc biên ảnh. Cần có thuật toán để chọn cha mẹ và điểm lai thay vì chọn ngẫu nhiên. Tạm thời đóng lại phần mạng Nơ-ron tế bào bậc nhất.

Tiến độ hiện tại với mạng Nơ-ron tế bào bậc hai (SOCNNs) chạy GA lai
- Về ma trận đầu vào: 
  - chạy được với ma trận 8x8 và 10x10 (chỉ cần giảm độ chênh lệch giữa t0 với t1 là sẽ giảm được tỉ lệ bị lỗi phương trình vi phân)
  - ma trận 10x10 thường xuyên gặp lỗi phương trình vi phân, ma trận 8x8 ít khi gặp lỗi
  - Nhận xét: lấy ma trận 8x8 làm đầu vào mặc định
- Về bộ trọng số: 
  - mọi bộ trọng số tìm đc với đầu vào 8x8 đều có thể lọc biên  => tối ưu hơn bậc nhất (đầu vào 8x8 bậc nhất chỉ cho ra 25% bộ trọng số lọc đc biên)
  - Nhận xét: Biên lọc đc từ bộ trọng số bậc 2 mịn thường mịn hơn so với bậc nhất, nhưng có nhiều bộ cho ra biên bị đứt quãng (có ảnh trong [TrongSoBac2ToiUu](/TrongSoBac2ToiUu))
- Về các tham số khác:
  - Sai số E0: 6.0
  - Số bộ cha mẹ: 2 (lúc đầu đặt bằng 5 nhưng rồi thấy không hiệu quả, nên chuyển về 2 thì tổng thời gian chạy giảm đi)
- Kết luận: 

