program selectCase
    implicit none

    ! print *,"���"

    integer year,month,day,sday
    print*,"�������£�"
    read(*,*)year,month
    if(MOD(year,4).eq.0) then
        sday=29
    else
        sday=28
    end if

    select case(month)

        case(1,3,5,7,8,10,12)
            day=31
        case(2)
            day=sday
        case(4,6,9,11)
            day=30
        case default
            day=0
    end select
    print*,year,"��",month,"����",day,"��"
    print*,321/10



    end