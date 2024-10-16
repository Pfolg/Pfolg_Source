program ex02_02
    ! implicit none
    ! 用data语句赋值
    ! 用=赋值
    ! 用do循环赋值
    ! 一个一个敲
    ! 综合前面的再read

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