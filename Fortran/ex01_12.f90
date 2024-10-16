program calculatesalary
    implicit none

    real salary,rate,flag,a
    integer hour

    print*,"请在下方输入工作时间："
    read*, hour
    rate=1.5
    flag=40
    a=100
    if (hour>flag) then
        salary=rate*(hour-flag)*a+flag*a
    else
        salary=hour*a
    end if

    print *,"salary=",salary

    end