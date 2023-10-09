from PIL import Image

class Project:
    def __init__(self, name, description, images, details):
        self.name = name
        self.description = description
        self.images = images
        self.details = details

    def get_summary(self):
        return f"Project Name: {self.name}\nDescription: {self.description}\nNumber of Images: {len(self.images)}\nDetails: {self.details}"

    def show_images(self):
        for image_path in self.images:
            img = Image.open(image_path)
            img.show()

# 이미지 파일 경로 리스트 생성
image_paths = ["C:\\Users\\wkdal\\Desktop\\2023\\02. PROJECT\\06. COUPONE\\1.png",
               "C:\\Users\\wkdal\\Desktop\\2023\\02. PROJECT\\06. COUPONE\\2.png",
               "C:\\Users\\wkdal\\Desktop\\2023\\02. PROJECT\\06. COUPONE\\3.png",
               "C:\\Users\\wkdal\\Desktop\\2023\\02. PROJECT\\06. COUPONE\\4.png",
               "C:\\Users\\wkdal\\Desktop\\2023\\02. PROJECT\\06. COUPONE\\5.png",
               "C:\\Users\\wkdal\\Desktop\\2023\\02. PROJECT\\06. COUPONE\\6.png",
               "C:\\Users\\wkdal\\Desktop\\2023\\02. PROJECT\\06. COUPONE\\7.png",
               "C:\\Users\\wkdal\\Desktop\\2023\\02. PROJECT\\06. COUPONE\\8.png",
               "C:\\Users\\wkdal\\Desktop\\2023\\02. PROJECT\\06. COUPONE\\9.png",
               "C:\\Users\\wkdal\\Desktop\\2023\\02. PROJECT\\06. COUPONE\\10.png",
               "C:\\Users\\wkdal\\Desktop\\2023\\02. PROJECT\\06. COUPONE\\11.png",
               "C:\\Users\\wkdal\\Desktop\\2023\\02. PROJECT\\06. COUPONE\\12.png",
               "C:\\Users\\wkdal\\Desktop\\2023\\02. PROJECT\\06. COUPONE\\13.png",
               "C:\\Users\\wkdal\\Desktop\\2023\\02. PROJECT\\06. COUPONE\\14.png",
               "C:\\Users\\wkdal\\Desktop\\2023\\02. PROJECT\\06. COUPONE\\15.png",
               "C:\\Users\\wkdal\\Desktop\\2023\\02. PROJECT\\06. COUPONE\\16.png",
               "C:\\Users\\wkdal\\Desktop\\2023\\02. PROJECT\\06. COUPONE\\17.png",
               "C:\\Users\\wkdal\\Desktop\\2023\\02. PROJECT\\06. COUPONE\\18.png",
               "C:\\Users\\wkdal\\Desktop\\2023\\02. PROJECT\\06. COUPONE\\19.png",
               "C:\\Users\\wkdal\\Desktop\\2023\\02. PROJECT\\06. COUPONE\\20.png",
               "C:\\Users\\wkdal\\Desktop\\2023\\02. PROJECT\\06. COUPONE\\21.png",
               "C:\\Users\\wkdal\\Desktop\\2023\\02. PROJECT\\06. COUPONE\\22.png",
               "C:\\Users\\wkdal\\Desktop\\2023\\02. PROJECT\\06. COUPONE\\23.png",
               "C:\\Users\\wkdal\\Desktop\\2023\\02. PROJECT\\06. COUPONE\\24.png",
               "C:\\Users\\wkdal\\Desktop\\2023\\02. PROJECT\\06. COUPONE\\25.png",
               "C:\\Users\\wkdal\\Desktop\\2023\\02. PROJECT\\06. COUPONE\\26.png",
               "C:\\Users\\wkdal\\Desktop\\2023\\02. PROJECT\\06. COUPONE\\27.png",
               "C:\\Users\\wkdal\\Desktop\\2023\\02. PROJECT\\06. COUPONE\\28.png",
               "C:\\Users\\wkdal\\Desktop\\2023\\02. PROJECT\\06. COUPONE\\29.png",
               "C:\\Users\\wkdal\\Desktop\\2023\\02. PROJECT\\06. COUPONE\\30.png",
               "C:\\Users\\wkdal\\Desktop\\2023\\02. PROJECT\\06. COUPONE\\31.png",
               "C:\\Users\\wkdal\\Desktop\\2023\\02. PROJECT\\06. COUPONE\\32.png",
               "C:\\Users\\wkdal\\Desktop\\2023\\02. PROJECT\\06. COUPONE\\33.png",
               "C:\\Users\\wkdal\\Desktop\\2023\\02. PROJECT\\06. COUPONE\\34.png",
               "C:\\Users\\wkdal\\Desktop\\2023\\02. PROJECT\\06. COUPONE\\35.png",
               "C:\\Users\\wkdal\\Desktop\\2023\\02. PROJECT\\06. COUPONE\\36.png",
               "C:\\Users\\wkdal\\Desktop\\2023\\02. PROJECT\\06. COUPONE\\37.png",
               "C:\\Users\\wkdal\\Desktop\\2023\\02. PROJECT\\06. COUPONE\\38.png",
               "C:\\Users\\wkdal\\Desktop\\2023\\02. PROJECT\\06. COUPONE\\39.png",
               "C:\\Users\\wkdal\\Desktop\\2023\\02. PROJECT\\06. COUPONE\\40.png",
               "C:\\Users\\wkdal\\Desktop\\2023\\02. PROJECT\\06. COUPONE\\41.png",
               "C:\\Users\\wkdal\\Desktop\\2023\\02. PROJECT\\06. COUPONE\\42.png",
               "C:\\Users\\wkdal\\Desktop\\2023\\02. PROJECT\\06. COUPONE\\43.png",
               "C:\\Users\\wkdal\\Desktop\\2023\\02. PROJECT\\06. COUPONE\\44.png",


]

project1 = Project(
    "Regular Coupon or Matched Discount Coupon?",
    "How Do Coupons Affect Sales Revenue?\n",
    image_paths,  # 이미지 파일 경로 리스트 사용
    "Details of another project."
)

project2 = Project(
    "Another Project Name",
    "Description of another project.",
    ["C:\\Users\\wkdal\\Desktop\\2023\\02. PROJECT\\06. COUPONE\\1.png"],
    "Details of another project."
)


projects = [project1, project2]

