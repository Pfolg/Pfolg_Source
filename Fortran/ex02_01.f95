program ex02_01
    ! where的用法
    implicit none
    REAL :: numbers(10)

    ! 初始化数组
    numbers = (/ 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0 /)

    ! 使用WHERE语句修改数组
    WHERE (numbers > 5.0)
    numbers = 0.0
    ELSEWHERE (numbers < 3.0)
    numbers = -1.0
    END WHERE

    ! 输出结果
    PRINT *, numbers

end program ex02_01