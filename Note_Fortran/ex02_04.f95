program ex02_04
    implicit none
    integer::x=6
    select case(x)
    case(:1)
        print*,"x小于等于1"
    case(7:)
        print*,"x大于7"
    case default
        print*,"x属于[1,7]"


    end select
end program ex02_04