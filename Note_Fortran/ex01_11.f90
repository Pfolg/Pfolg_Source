program dianliujisuan
    implicit none

    real U,R1,R2,R0,R,I

    U=100
    R1=20
    R2=50
    R0=100

    R=R0+R1*R2/(R1+R2)
    I=U/R

    print*,R,I

    !  114.285713      0.875000000  

    end