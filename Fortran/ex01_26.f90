program study
    ! 数组初步,同Python二维列表
    implicit none
    integer,dimension(1,5)::a
    a(1,1)=1
    a(1,2)=2
    a(1,3)=3
    a(1,4)=a(1,1)+a(1,2)+a(1,3)
    a(1,5)=a(1,1)*a(1,2)*a(1,3)
    print*,a

end program study