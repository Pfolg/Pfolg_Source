program guessnumber
    
    integer::max_num=10,count=3,num,target_num,choice
    real::n
    print*,"��ѡ���淨��[1]Ĭ�ϣ�10/3����[2]�Զ��壺"
    read*,choice
    if ( .not. choice==1 )then
        print*,"���������ֵ���������","�ָ�����"
        read*,max_num,count
    end if
    ! print*,max_num,count
    
    call RANDOM_SEED()
    call RANDOM_NUMBER(n)
    target_num=INT(max_num*n)
    do i=1,count
        print*,"���������µ����֣�"
        read(*,*)num    
        if (num==target_num)then
            print*,"��ϲ�㣬�¶��ˣ�"
            exit
        else if (num>target_num)then
                if (i==count)then
                    print*,"���һ�ζ��´��ˣ�fw��"
                    print*,"���������",target_num
                    exit
                end if
                print*,"������˼�����µ����ִ���һ�㣡������",count-i,"�λ���"
                cycle
        else 
            if (i==count)then
                print*,"���һ�ζ��´��ˣ�fw��"
                print*,"���������",target_num
                exit
            end if
            print*,"������˼�����µ�����С��һ�㣡������",count-i,"�λ��᣺"
            cycle
        end if
    end do    
    print*,"(�������������س��˳�����)"
    read*,num
    
    end program guessnumber