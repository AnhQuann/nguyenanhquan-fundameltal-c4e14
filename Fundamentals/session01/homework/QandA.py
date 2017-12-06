# Câu hỏi 1: How to check a variable’s type?
#   Trả lời:
        # Sử dụng hàm type.
        # Ví dụ:
        #     >>> type(123)
        #     <class 'int'>
        # Nghĩa là Python cho biết 123 thuộc kiểu integer
#
# Câu hỏi 2: In what cases, you will get SyntaxError from the compiler telling you that some of your variables have invalid names? Can you give 3 different examples of invalid names?
#   Trả lời:
#     Trường hợp 1: Tên biến không bắt đầu bằng chữ cái. Ví dụ: 22ThanhCong = "TechKids"
#     Trường hợp 2: Tên biến chứa kí tự đặc biệt hoặc không hợp lệ. Ví dụ: ILike$$$ = "I like money"
#     Trường hợp 3: Tên biến trùng với 1 trong khoảng 30 keywords của Python. Ví dụ: continue = "Tiep tuc"





# Calculates the area of a circle
radius = float(input("Radius? "))
print("Area =", radius*radius*3.14)



# converts Celsius (0C) into Fahrenheit (0F)
celcius = float(input("Enter the temprature in Celcius? "))
print(celcius, "(C) =", 1.8*celcius + 32, "(F)")
