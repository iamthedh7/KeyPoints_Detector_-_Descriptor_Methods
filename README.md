# KEY POINTS DETECTORS & DESCRIPTOR METHODS

## A/ FLOATING-POINTS DESCRIPTORS

### 1. Harris:

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

### 2. SIFT:

Với Harris, chúng không thay đổi theo chiều quay, có nghĩa là, ngay cả khi hình ảnh được xoay, chúng ta vẫn có thể tìm thấy các góc giống nhau. Đó là điều hiển nhiên vì các góc cũng vẫn là góc trong hình ảnh xoay. Hình minh họa sau với mỗi hình đều có 33 góc **_(kết quả thực nghiệm)_**:

![1](https://user-images.githubusercontent.com/81065789/148065886-43e17743-85bb-4073-adf7-b7a7b75e25e7.jpg)
![2](https://user-images.githubusercontent.com/81065789/148065896-b450c892-39ea-40b7-aa8b-8c0f9efecfd1.jpg)

Nhưng còn đối với phép Scaling thì sao? Ở tỉ lệ này có 1 góc nhưng ở tỷ lệ khác có còn là 1 góc nữa hay không? 

Ví dụ, hãy kiểm tra một hình ảnh đơn giản bên dưới:

![image](https://user-images.githubusercontent.com/81065789/148063926-e5373a0f-92ec-49f0-877e-c70016563d80.png)

Ảnh ban đầu cho ta một góc, nhưng ở tỉ lệ lớn hơn, nó lại có nhiều hơn là một góc. Đó là lí do SIFT ra đời (2004)!

Với SIFT, 2 hình với 2 tỉ lệ khác nhau sẽ cho ra 1 tập keypoints khác nhau:

917 keypoints: ![SIFTbig](https://user-images.githubusercontent.com/81065789/148076055-997693f2-80da-4c3d-9220-e764f42b8de8.jpg)

263 keypoints: ![SIFTsmall](https://user-images.githubusercontent.com/81065789/148076069-2b8f9c13-8924-404a-a8a8-c0077d65c433.jpg)

#### * MATCHING:

Ảnh gốc:

1.![book1](https://user-images.githubusercontent.com/81065789/148076657-4a2eb0c5-ae67-4c87-8011-6345430adb66.png)

2.![book2](https://user-images.githubusercontent.com/81065789/148076668-b44e1ffb-c5fa-46c4-b0c3-a0d55c88e96f.png)

Sau khi trích xuất được các keypoints từ 2 ảnh có độ tương đồng nhau, ta thử thực hiện Matching các features của 2 ảnh lại với nhau:

![SIFT_matches_50](https://user-images.githubusercontent.com/81065789/148076299-d142ef84-115e-445e-ad23-ec399d3f5e9b.jpg)

### 3. SURF (NON-FREE in 2021 :) ):

Chúng ta dùng SIFT để phát hiện và mô tả keypoints nhưng tốc độ của nó tương đối chậm, người ta cần một phiên bản nâng cấp hơn, vì thế, vào năm 2006, SURF ra đời, cải thiện tốc độ cho SIFT.

Tóm lại, SURF bổ sung rất nhiều tính năng để cải thiện tốc độ trong từng bước thực hiện, do đó nó nhanh hơn SIFT. Phân tích cho thấy nó nhanh hơn _3 lần_ so với SIFT trong khi hiệu suất tương đương với SIFT. SURF xử lý tốt hình ảnh bị mờ và xoay, nhưng không tốt trong việc xử lý thay đổi điểm nhìn và thay đổi độ sáng.

