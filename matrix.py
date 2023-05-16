import numpy as np

def nhap_ma_tran():
    N = int(input("Nhập vào kích thước ma trận NxN: "))
    matrix = []
    for i in range(N):
        row = list(map(int, input(f"Nhập hàng {i+1}: ").split()))
        matrix.append(row)
    return np.array(matrix)

def hien_thi_ma_tran(matrix):
    print("Ma trận:")
    print(matrix)

def cong_hai_ma_tran():
    print("Nhập ma trận thứ nhất:")
    matrix1 = nhap_ma_tran()
    print("Nhập ma trận thứ hai:")
    matrix2 = nhap_ma_tran()
    
    result = matrix1 + matrix2
    print("Tổng hai ma trận:")
    print(result)

def nhan_hai_ma_tran():
    print("Nhập ma trận thứ nhất:")
    matrix1 = nhap_ma_tran()
    print("Nhập ma trận thứ hai:")
    matrix2 = nhap_ma_tran()
    
    result = np.dot(matrix1, matrix2)
    print("Tích hai ma trận:")
    print(result)

def tich_vo_huong():
    matrix = nhap_ma_tran()
    scalar = float(input("Nhập vào số thực: "))
    
    result = scalar * matrix
    print("Tích vô hướng:")
    print(result)

def tim_chuyen_vi():
    matrix = nhap_ma_tran()
    result = np.transpose(matrix)
    
    print("Ma trận chuyển vị:")
    print(result)

def tim_nghich_dao():
    matrix = nhap_ma_tran()
    try:
        result = np.linalg.inv(matrix)
        print("Ma trận nghịch đảo:")
        print(result)
    except np.linalg.LinAlgError:
        print("Ma trận không khả nghịch.")

def menu():
    while True:
        print("\n----- MENU LỰA CHỌN -----")
        print("1. Nhập vào ma trận")
        print("2. Hiển thị ma trận")
        print("3. Cộng hai ma trận")
        print("4. Nhân hai ma trận")
        print("5. Tích vô hướng 1 số thực và ma trận")
        print("6. Tìm ma trận chuyển vị")
        print("7. Tìm ma trận nghịch đảo")
        print("0. Thoát chương trình")
        
        choice = input("Chọn chức năng (0-7): ")
        
        if choice == '1':
            matrix = nhap_ma_tran()
        elif choice == '2':
            hien_thi_ma_tran(matrix)
        elif choice == '3':
            cong_hai_ma_tran()
        elif choice == '4':
            nhan_hai_ma_tran()
        elif choice == '5':
            tich_vo_huong()
        elif choice == '6':
            tim_chuyen_vi
def main():
    menu()

if __name__ == "__main__":
    main()
