program fenShuSHaiXUan
    ! сп╢М
    implicit none
    integer fenZI,fenMu,fzGW,fmSW,fzSW,fmGW
    do fenMu=12,99,1
        do fenZI=10,fenMu-1,1
            fzGW=mod(fenZI,10)
            fmGW=mod(fenMu,10)
            fmSW=fenMu/10
            fzSW=fenZI/10

            if (fenZI<fenMu .AND. (fzGW==fmSW) .and. (fenZI/fenMu)==(fzSW/fmGW)) print*,fenZI,"/",fenMu

        end do
    end do
    


end program fenShuSHaiXUan