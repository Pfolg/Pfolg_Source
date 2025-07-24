program gravitationalDisp

    ! 该程序计算重力下的垂直运动
    implicit none  
    
       ! 重力加速度
       real, parameter :: g = 9.80665
       
       ! variable declaration
       real :: s ! displacement   位移
       real :: t ! time  
       real :: u ! initial speed  初速度
       
       ! 赋值
       t = 5.0   
       u = 50  
       
       ! 移位
       s = u * t - g * (t**2) / 2  
       
       ! 输出
       print *, "Time = ", t
       print *, 'Displacement = ',s  
       
    end program gravitationalDisp