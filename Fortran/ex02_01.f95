program ex02_01
    ! where���÷�
    implicit none
    REAL :: numbers(10)

    ! ��ʼ������
    numbers = (/ 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0 /)

    ! ʹ��WHERE����޸�����
    WHERE (numbers > 5.0)
    numbers = 0.0
    ELSEWHERE (numbers < 3.0)
    numbers = -1.0
    END WHERE

    ! ������
    PRINT *, numbers

end program ex02_01