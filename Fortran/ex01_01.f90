program ex01_01
    
implicit none

character(15) string1  ! 定义长度为15的字符型变量
character(8) string2
character(25) add

string1="Good moring"  ! 赋值
string2="teacher"
add=string1//string2  ! 拼接

print *,add
write(*,*) add
string1(6:14)="afternoon"

add=string1//string2

write(*,*) add

end program ex01_01
