subroutine f_func(x,s)
! Let's compile this a module: myFuncs
    implicit none
    integer,parameter:: prec=selected_real_kind(15,307)
    integer, intent(in)::  x
    real(prec), intent(out):: s 
    real(prec), dimension(x,x)::jm
    integer i,j
    jm =0.0
    do i = 1,x
        do j = 1,x
            jm(i,j)=log(i+1.0)/1000.0**2 / (1.0+j)
        end do
    end do
    s=sum(jm)
    return
end subroutine f_func
