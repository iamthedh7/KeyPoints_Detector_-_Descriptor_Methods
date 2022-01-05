<!-- Title -->
<h1 align="center"><b>----- KEY POINTS DETECTORS & DESCRIPTOR METHODS -----</b></h1>

============================================================================================

* METHOD 1: HARRIS

Hình bên trái là ảnh gốc, giữa là ảnh biểu thị cường độ Gradient theo chiều x, tiếp theo là biểu thị cường độ Gradient theo chiều y, cuối cùng là biểu thị cường độ Gradient theo cả chiều x và y.

![image](https://user-images.githubusercontent.com/81065789/148052662-081da42b-0686-48bd-9072-3db08f1df2a7.png)

Để xác định được một điểm là Corner (góc), chúng ta sẽ lấy tổng các giá trị Gradient theo chiều x và theo chiều y trong vùng đó:

![image](https://user-images.githubusercontent.com/81065789/148052875-50da8d89-8968-4e6e-b222-de27cdbb6fc9.png)

Nếu cả 2 giá trị này đều đủ lớn, thì chúng ta có thể định nghĩa vùng đó là một góc. Quá trình này được thực hiện cho mọi pixel của hình ảnh. Phương phá này hoạt động vì các vùng được gọi là góc sẽ có số lượng lớn Gradient theo chiều ngang và Gradient theo chiều dọc.

Để mở rộng phương thức này sang các góc tùy ý, trước tiên chúng ta cần tính toán biểu diễn cường độ Gradient của hình ảnh, và sau đó sử dụng cường độ Gradient này để xây dựng lên một ma trận M:

![image](https://user-images.githubusercontent.com/81065789/148053166-04e534d7-f447-4f39-899e-b14ebd7bffc7.png)

Sau khi ma trận M được định nghĩa, chúng ta sẽ sử dụng công thức sau để tính giá trị điểm số biểu thị mức độ của các góc.

![image](https://user-images.githubusercontent.com/81065789/148053429-2dcdf575-42b3-4160-8b9f-7f5659e8badf.png)

Sau đó, chúng ta có thể xem xét điều kiện sau:

      - Nếu |R| nhỏ thì đây là một khu vực phẳng, có nghĩa là không phải keypoint

      - Nếu R < 0 thì đây là một cạnh, và đây cũng không phải keypoint

      - Nếu |R| lớn thì đây chính là một keypoint
      
============================================================================================

# FLOATING-POINTS DESCRIPTORS (SIFT & SURF)

* METHOD 2: SIFT (NON-FREE trước kia, nhưng có sẵn trên máy local ở 2021)

Với Harris, chúng không thay đổi theo chiều xoay, có nghĩa là, ngay cả khi hình ảnh được xoay, chúng ta vẫn có thể tìm thấy các góc giống nhau. Đó là điều hiển nhiên vì các góc trong hình ảnh xoay cũng vẫn là các góc trong hình ảnh ban đầu, hình sau minh họa cho điều này với mỗi hình đều có 33 góc **_(kết quả thực nghiệm)_**:

![1](https://user-images.githubusercontent.com/81065789/148065886-43e17743-85bb-4073-adf7-b7a7b75e25e7.jpg)
![2](https://user-images.githubusercontent.com/81065789/148065896-b450c892-39ea-40b7-aa8b-8c0f9efecfd1.jpg)

Nhưng còn đối với phép Scaling thì sao? Ở tỉ lệ này có 1 góc nhưng ở tỷ lệ khác có còn là 1 góc nữa hay không? 

Ví dụ, hãy kiểm tra một hình ảnh đơn giản bên dưới:

![image](https://user-images.githubusercontent.com/81065789/148063926-e5373a0f-92ec-49f0-877e-c70016563d80.png)

Ảnh ban đầu cho ta một góc, nhưng ở tỉ lệ lớn hơn, nó lại có nhiều hơn là một góc. Đó là lí do SIFT ra đời (2004)!

Với SIFT, 2 hình với 2 tỉ lệ khác nhau sẽ cho ra 1 tập keypoints khác nhau:

917 keypoints: ![SIFTbig](https://user-images.githubusercontent.com/81065789/148076055-997693f2-80da-4c3d-9220-e764f42b8de8.jpg)

263 keypoints: ![SIFTsmall](https://user-images.githubusercontent.com/81065789/148076069-2b8f9c13-8924-404a-a8a8-c0077d65c433.jpg)

================================

METHOD 3: SURF (NON-FREE ở 2021)

Chúng ta dùng SIFT để phát hiện và mô tả keypoints nhưng tốc độ của nó tương đối chậm, người ta cần một phiên bản nâng cấp hơn, vì thế, vào năm 2006, SURF ra đời, cải thiện tốc độ cho SIFT.

Tóm lại, SURF bổ sung rất nhiều tính năng để cải thiện tốc độ trong từng bước thực hiện, do đó nó nhanh hơn SIFT. Phân tích cho thấy nó nhanh hơn _3 lần_ so với SIFT trong khi hiệu suất tương đương với SIFT. SURF xử lý tốt hình ảnh bị mờ và xoay, nhưng không tốt trong việc xử lý thay đổi điểm nhìn và thay đổi độ sáng.

Vì nó không miễn phí trong OpenCV tại thời điểm 2021 nên tôi không thể đánh giá hiệu suất và trình bày kết quả ở đây được. :(

============================================================================================

* METHOD 4: FAST

FAST keypoint detector được sử dụng để phát hiện các góc trong hình ảnh, được triển khai trong thư viện OpenCV và được áp dụng nhiều nhất cho các ứng dụng thời gian thực hoặc các thiết bị bị hạn chế tài nguyên, nơi không có nhiều thời gian tính toán hoặc sức mạnh để sử dụng các kĩ thuật dò tìm keypoints tiên tiến hơn. 

Cụ thể: FAST không tính và lưu trữ ma trận descriptor cho hình ảnh nhứ SIFT và SURF, nên không tốn dung lượng lưu trữ ma trận này, phù hợp cho bộ nhớ của các thiết bị di dộng.

Ý tưởng của FAST là để một pixel được coi là một góc phải có _**ít nhất n**_ các pixel liền kề dọc theo chu vi hình tròn có bán kính r, _**tất cả**_ đều sáng hơn hoặc tối hơn pixel trung tâm bởi một ngưỡng t nào đó.

Hãy cùng xem một ví dụ:

![3](https://user-images.githubusercontent.com/81065789/148164855-90fbdaba-9e20-4b7a-89bc-851a779ed2bb.png)

Ở đây, chúng ta muốn xem xét liệu pixel trung tâm có nên được coi là một điểm then chốt hay không? Ví dụ, pixel trung tâm = 32, để pixel này được coi là một điểm then chốt, nó phải có n = 12 pixel liền kề dọc theo đường biên của vòng tròn có giá trị đều lớn hơn 32 + t hoặc nhỏ hơn 32 - t. Giả sử rằng t = 16 cho ví dụ này.

Như chúng ta có thể thấy, chỉ có 8 pixel liền kề tối hơn (được đánh dấu bằng hình chữ nhật màu xanh lá cây, tất cả các pixel khác là hình chữ nhật màu đỏ) so với pixel trung tâm - do đó, pixel trung tâm không phải là keypoint

Một trường hợp khác:

![4](https://user-images.githubusercontent.com/81065789/148164868-c0765261-0227-40cd-af8a-6d43c9330469.png)

Chúng ta thấy có 14 pixel liền kề nhau và sáng hơn pixel trung tâm. Vì thế, pixel trung tâm này được coi là keypoint.

Chúng ta có thể thấy được là thuật toán bên trên tuy rất đơn giản, nhưng lại được sử dụng rất nhiều trong các ứng dụng Computer Vision hằng ngày cũng như các ứng dụng real-time, đòi hỏi tốc độ tính toán cao. Nhược điểm là nó không mạnh mẽ với mức độ nhiễu cao và phụ thuộc vào một ngưỡng.

Kết quả của thuật toán FAST sử dụng hàm cv2.FastFeatureDetector_create mặc định trong OpenCV v4.5.3:

![FAST_nonmaxSuppression](https://user-images.githubusercontent.com/81065789/148171386-21dac5d3-80d4-4b27-9957-63e4de482c0f.jpg)

============================================================================================
