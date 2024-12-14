program guessnumber
    
    integer::max_num=10,count=3,num,target_num,choice
    real::n
    print*,"请选择玩法：[1]默认（10/3），[2]自定义："
    read*,choice
    if ( .not. choice==1 )then
        print*,"请输入最大值与次数（以","分隔）："
        read*,max_num,count
    end if
    ! print*,max_num,count
    
    call RANDOM_SEED()
    call RANDOM_NUMBER(n)
    target_num=INT(max_num*n)
    do i=1,count
        print*,"请输入您猜的数字："
        read(*,*)num    
        if (num==target_num)then
            print*,"恭喜你，猜对了！"
            exit
        else if (num>target_num)then
                if (i==count)then
                    print*,"最后一次都猜错了，fw！"
                    print*,"这个数字是",target_num
                    exit
                end if
                print*,"不好意思，您猜的数字大了一点！您还有",count-i,"次机会"
                cycle
        else 
            if (i==count)then
                print*,"最后一次都猜错了，fw！"
                print*,"这个数字是",target_num
                exit
            end if
            print*,"不好意思，您猜的数字小了一点！您还有",count-i,"次机会："
            cycle
        end if
    end do    
    print*,"(输入任意整数回车退出……)"
    read*,num
    
    end program guessnumber