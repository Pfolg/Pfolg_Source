program random_numbers
    ! 这是一个死循环程序
    implicit none
    integer :: j
    real :: rand_number
    character(len=36) :: x=""
    character :: keys(36)=(/"0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f","g","h",&
    "i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"/)
    print*,shape(keys),size(keys,1),size(keys)!,size(keys,2)

    ! 初始化随机数生成器，使用系统时间作为种子
    call random_seed()

    ! 生成并打印10个随机数
    do while(.TRUE.)
        x=""
        do j=1,36
            call random_number(rand_number)
            ! print *, 'Random number ', i, ': ', rand_number
            x(j:j)=keys(INT(rand_number*36)+1)
            ! print*,x
        end do
        print*,x
    end do
end program random_numbers
