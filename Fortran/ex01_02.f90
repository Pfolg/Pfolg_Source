program ex01_02
    implicit none

    REAL pi
    PARAMETER(pi=3.141592654)  ! 定义pi代表常量3.141592654
    write(*,*) sin(pi/6)
    write(*,*) sin(pi)

end