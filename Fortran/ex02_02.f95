program ex02_02
    ! implicit none
    ! ��data��丳ֵ
    ! ��=��ֵ
    ! ��doѭ����ֵ
    ! һ��һ����
    ! �ۺ�ǰ�����read

    ! x=1,10,12,-5
    integer x
    real result
    x=1
    result=calculate(x)
    print*,"The result is ",result
end program ex02_02

function calculate(x) result(y)
    implicit none
    integer, intent(in) :: x
    real :: y
    print*,"function start"
    y=5*x**3-2*x**2+7*x+6
    print*,"function end"
    
end function calculate