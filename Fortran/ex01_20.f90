program y2024m9d18
    implicit none
    integer a,s,I
    a=0

    
    print*,"2024��9��18��16:09:38"
    do 
        if (a==60) exit
        if (mod(a,10)==0)print*,a
        a=a+1
    end do

    a=0
    s=0
    ! ��ѭ��������doѭ�����״�bug
    do 
        a=a+1
        if (mod(a,2)==0)cycle
        s=s+a
        
        if (a==101)exit
    end do
    print*,s

    ! ������doѭ�������Զ��Ƕ��
    write (*,*)(3,4,I=1,3)
    ! 3           4           3           4           3           4

    

    
end program y2024m9d18