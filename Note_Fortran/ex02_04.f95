program ex02_04
    implicit none
    integer::x=6
    select case(x)
    case(:1)
        print*,"xС�ڵ���1"
    case(7:)
        print*,"x����7"
    case default
        print*,"x����[1,7]"


    end select
end program ex02_04