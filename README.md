# machine_learning_quatity_water
<p>Xây dựng mô hình đánh giá chất lượng nguồn nước và đưa ra mô hình có tốt nhất</p>
<a href = 'https://www.kaggle.com/datasets/adityakadiwal/water-potability'>Dataset</a>
<p>Dữ liệu đầu vào có 10 hàng gồm 9 đặc trưng với 9 input và 1 output và có 3275 hàng.
</p>

<ol>
  <li>
    pH: PH là thông số quan trọng trong việc đánh giá cân bằng axit-bazơ của nước. Nó cũng là chỉ báo về tình trạng axit hoặc kiềm của trạng thái nước. WHO đã khuyến nghị giới hạn pH tối đa cho phép là từ 6.5 đến 8,5. Phạm vi điều tra hiện tại là 6,52–6,83, nằm trong phạm vi tiêu chuẩn của WHO.
  </li>
  <li>.Độ cứng: Độ cứng chủ yếu do muối canxi và magie gây ra. Những muối này được hòa tan từ các trầm tích địa chất mà nước di chuyển qua đó. Khoảng thời gian nước tiếp xúc với vật liệu tạo độ cứng giúp xác định độ cứng trong nước thô. Độ cứng ban đầu được định nghĩa là khả năng của nước làm kết tủa xà phòng do Canxi và Magie gây ra.
</li>
<li>Chất rắn (Tổng chất rắn hòa tan - TDS): Nước có khả năng hòa tan nhiều loại khoáng chất vô cơ và một số khoáng chất hữu cơ hoặc các muối như kali, canxi, natri, bicarbonat, clorua, magie, sunfat v.v.. Các khoáng chất này tạo ra không- muốn có mùi vị và màu sắc loãng khi xuất hiện trong nước. Đây là thông số quan trọng cho việc sử dụng nước. Nước có giá trị TDS cao chứng tỏ nước có độ khoáng hóa cao. Giới hạn mong muốn đối với TDS là 500 mg/l và giới hạn tối đa là 1000 mg/l được quy định cho mục đích uống rượu. </li>
  <li>Cloramin: Clo và cloramin là những chất khử trùng chính được sử dụng trong hệ thống nước công cộng. Cloramin thường được hình thành khi amoniac được thêm vào clo để xử lý nước uống. Mức clo lên tới 4 miligam mỗi lít (mg/L hoặc 4 phần triệu (ppm)) được coi là an toàn trong nước uống.
</li>
  <li>Sulfate: Sulfate là những chất xuất hiện tự nhiên được tìm thấy trong khoáng chất, đất và đá. Chúng có mặt trong không khí xung quanh, nước ngầm, thực vật và thực phẩm. Việc sử dụng sunfat thương mại chủ yếu là trong công nghiệp hóa chất. Nồng độ sunfat trong nước biển là khoảng 2.700 miligam mỗi lít (mg/L). Nó dao động từ 3 đến 30 mg/L trong hầu hết các nguồn cung cấp nước ngọt, mặc dù nồng độ cao hơn nhiều (1000 mg/L) được tìm thấy ở một số vị trí địa lý.
</li>
  <li>
    .Độ dẫn điện: Nước tinh khiết không phải là chất dẫn điện tốt mà là chất cách điện tốt. Tăng nồng độ ion giúp tăng cường độ dẫn điện của nước. Nói chung, lượng chất rắn hòa tan trong nước quyết định độ dẫn điện. Độ dẫn điện (EC) thực sự đo quá trình ion của dung dịch cho phép nó truyền dòng điện. Theo tiêu chuẩn của WHO, giá trị EC không được vượt quá 400 μS/cm.

  </li>
  <li>
    Organic_Carbon: Tổng lượng Carbon hữu cơ (TOC) trong nước nguồn đến từ quá trình phân hủy chất hữu cơ tự nhiên (NOM) cũng như các nguồn tổng hợp. TOC là thước đo tổng lượng carbon trong các hợp chất hữu cơ trong nước tinh khiết. Theo US EPA < 2 mg/L dưới dạng TOC trong nước đã qua xử lý/nước uống và < 4 mg/Lít trong nguồn nước được sử dụng để xử lý.
  </li>
  <li>
    Trihalomethanes: THM là hóa chất có thể tìm thấy trong nước được xử lý bằng clo. Nồng độ THM trong nước uống thay đổi tùy theo mức độ chất hữu cơ trong nước, lượng clo cần thiết để xử lý nước và nhiệt độ của nước đang được xử lý. Mức THM lên tới 80 ppm được coi là an toàn trong nước uống.
  </li>
  <li>
    .Độ đục: Độ đục của nước phụ thuộc vào lượng chất rắn có ở trạng thái lơ lửng. Nó là thước đo đặc tính phát sáng của nước và thử nghiệm được sử dụng để chỉ ra chất lượng xả thải đối với chất keo. Giá trị độ đục trung bình thu được tại Cơ sở Wondo Genet (0,98 NTU) thấp hơn giá trị khuyến nghị của WHO là 5,00 NTU.
  </li>
  <li>
    Khả năng uống được: Cho biết nước có an toàn cho con người hay không trong đó 1 có nghĩa là có thể uống được và 0 có nghĩa là không thể uống được.
  </li>
</ol>
<h3>Kết quả đánh giá chất lượng các mô hình sau huấn luyện</h3>
<table>
  <tr>
    <th>Model</th>
    <th>Accuracy</th>
  </tr>
  <tr>
    <th>SVM</th>
    <td>66%</td>
  </tr>
   <tr>
    <th>Logistic</th>
    <td>61%</td>
  </tr>
   <tr>
    <th>Naives Bayes</th>
    <td>62%</td>
  </tr>
   <tr>
    <th>Perceptron</th>
    <td>53%</td>
  </tr>
   <tr>
    <th>Ensemble Voting(svm,logistic,navie bayes)</th>
    <td>65%</td>
  </tr>
</table>
<p>Dữ liệu chất lượng nguồn nước khá là mất cân bằng,<br> Sau huấn luyện SVM mang lại độ chính xác cao nhất là 66% và chúng em sẽ dùng model này để đưa vào bài toán thực tế</p>
<p>Save Model dùng thư viện pickle để lưu model dưới dạng file nhị phân</p>
<img src =https://github.com/Nik211885/machine_learning_quatity_water/assets/119054771/e6474044-7d23-4f02-81b6-309c4480db9a>
<p>Load Model</p>
<img src =https://github.com/Nik211885/machine_learning_quatity_water/assets/119054771/324dcfd0-22df-4fb6-a4e2-804d11e71879>

<h3>Application</h3>
<p>UI</p>
<img src = https://github.com/Nik211885/machine_learning_quatity_water/assets/119054771/fe800858-e666-44f2-a741-7dd4866db919>
<p>Yêu cầu : <br>Các dữ liệu đầu vào phải là số và không được bỏ trống</p>
<p>Sau khi nhập các dữ liệu cần dự đoán ứng dụng sẽ chả về kết quả liệu chất lượng nước có thể uống được không</p>
