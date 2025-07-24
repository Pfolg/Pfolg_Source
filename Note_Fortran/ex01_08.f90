! ==	.eq.	检查两个操作数的值是否相等，如果相等则条件成立。	(A == B) 不成立。
! /=	.ne.	检查两个操作数的值是否相等，如果值不相等则条件成立。	(A != B) 为 true。
! >	.gt.	检查左操作数的值是否大于右操作数的值，如果是，则条件为真。	(A > B) 不成立。
! <	.lt.	检查左操作数的值是否小于右操作数的值，如果是，则条件为真。	(A < B) 为 true。
! >=	.ge.	检查左操作数的值是否大于或等于右操作数的值，如果是，则条件为真。	(A >= B) 不成立。
! <=	.le.	检查左操作数的值是否小于或等于右操作数的值，如果是，则条件为真。	(A <= B) 为 true。

! 该程序检查关系运算符
implicit none  

! 变量声明
integer :: a, b

! 赋值
a = 10   
b = 20

if (a .eq. b) then
   print *, "Line 1 - a is equal to b"
else
   print *, "Line 1 - a is not equal to b"
end if

if (a > b) then
   print *, "Line 2 - a is greater than b"
else
   print *, "Line 2 - a is less than b"
end if

if (a <= b) then
   print *, "Line 3 - a is less than or equal to b"
else
   print *, "Line 3 - a is greater than b"
end if

a = 20   
b = 20

if (a .eq. b) then
   print *, "Line 4 - a is equal to b"
else
   print *, "Line 4 - a is not equal to b"
end if

if (a == b) then
    print *, "Line 5 - a is equal to b"
 else
    print *, "Line 5 - a is not equal to b"
 end if
end