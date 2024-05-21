import math

class Line:
    def __init__(self,length=1):
        self.__length =length
    def set_length(self,length):
        self.__length = length
    def get_length(self):
        return self.__length
    def area_square(line):
        """line클래스의 객체를 매개변수로받아
          length제곱의 정사각형의 넓이를 반환한다
        Args: line(Line)
        Returns: int or float: lengthdml wpra
         """
        return line.get_length()**2
    def area_circle(line):
        '''길이를 입력받아 언의 넓이를 구하는 함수
        Args: line(Line):반지름의 길이
        Returns:length제곱 곱하기 파이
        int or float: 원의 넓이를 반환한다'''
        return line.get_length()**2*math.pi
    def area_regular_triangle(line):
        return line.get_length()**2*math.sqrt(3)/4